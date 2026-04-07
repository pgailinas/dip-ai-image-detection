from typing import List, Dict, Optional, Tuple
import io
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from datasets import load_dataset
from PIL import Image, UnidentifiedImageError

OPENIMAGES_DATASET_NAME = "bitmind/open-images-v7"
OPENIMAGES_SPLIT = "train"
OPENIMAGES_STREAM = True

OPENIMAGES_URL_FIELDS = [
    "image_url",
    "url",
    "original_url",
    "source_url",
]
OPENIMAGES_ID_FIELDS = [
    "image_id",
    "id",
    "imageid",
    "openimages_id",
]

REQUEST_TIMEOUT = 20
MAX_WORKERS = 4
SHUFFLE_BUFFER_SIZE = 500

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; dataset-builder/1.0)"
}


def load_source_dataset(seed: int = 42):
    """
    Load the Open Images V7 training split as a streaming Hugging Face dataset
    and shuffle it with a modest buffer to limit RAM usage.
    """
    ds = load_dataset(
        OPENIMAGES_DATASET_NAME,
        split=OPENIMAGES_SPLIT,
        streaming=OPENIMAGES_STREAM,
    )
    ds = ds.shuffle(seed=seed, buffer_size=SHUFFLE_BUFFER_SIZE)
    return ds


def extract_openimages_source_id(item: Dict, fallback_idx: int) -> str:
    """
    Pick a stable identifier from an Open Images record when possible.
    Falls back to the running index if no better ID field is present.
    """
    for key in OPENIMAGES_ID_FIELDS:
        if key in item and item[key] is not None:
            return str(item[key])

    return f"openimages_{fallback_idx}"


def extract_image_url(item: Dict) -> Optional[str]:
    """
    Return the first usable image URL field from a metadata row.
    """
    for key in OPENIMAGES_URL_FIELDS:
        value = item.get(key)
        if isinstance(value, str) and value.startswith(("http://", "https://")):
            return value

    image_value = item.get("image")
    if isinstance(image_value, str) and image_value.startswith(("http://", "https://")):
        return image_value

    return None


def download_image_bytes(url: str, timeout: int = REQUEST_TIMEOUT) -> Optional[bytes]:
    """
    Download raw image bytes from a remote Open Images URL.
    """
    try:
        r = requests.get(url, headers=HEADERS, timeout=timeout)
        r.raise_for_status()
        return r.content
    except Exception:
        return None


def open_image_from_bytes(img_bytes: bytes) -> Optional[Image.Image]:
    """
    Open raw image bytes as a PIL image.
    """
    try:
        img = Image.open(io.BytesIO(img_bytes))
        img.load()
        return img
    except (UnidentifiedImageError, OSError):
        return None


def _fetch_record(idx: int, item: Dict) -> Optional[Tuple[int, Dict]]:
    """
    Download and decode one Open Images record.
    Returns (idx, standardized_record) or None if unusable.
    """
    image_url = extract_image_url(item)
    if not image_url:
        return None

    img_bytes = download_image_bytes(image_url)
    if img_bytes is None:
        return None

    image_obj = open_image_from_bytes(img_bytes)
    if image_obj is None:
        return None

    record = {
        "source_id": extract_openimages_source_id(item, idx),
        "source_ref": image_url,
        "image_obj": image_obj,
    }
    return idx, record


def get_candidate_records(ds, batch_size: int = 10, batch_id: int = 1) -> List[Dict]:
    """
    Return one batch of standardized Open Images candidate records.

    Uses 1-based batch indexing:
        batch_id = 1 -> first batch
        batch_id = 2 -> second batch

    Keeps RAM lower by limiting batch size and thread count.
    Preserves original order of accepted records within the batch.
    """
    start = (batch_id - 1) * batch_size
    end = start + batch_size

    raw_items: List[Tuple[int, Dict]] = []
    ds_iter = iter(ds)

    for idx, item in enumerate(ds_iter):
        if idx < start:
            continue
        if idx >= end:
            break
        raw_items.append((idx, item))

    if not raw_items:
        return []

    results_by_idx: Dict[int, Dict] = {}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_map = {
            executor.submit(_fetch_record, idx, item): idx
            for idx, item in raw_items
        }

        for future in as_completed(future_map):
            result = future.result()
            if result is None:
                continue
            idx, record = result
            results_by_idx[idx] = record

    ordered_indices = sorted(results_by_idx.keys())
    records = [results_by_idx[idx] for idx in ordered_indices]
    return records
