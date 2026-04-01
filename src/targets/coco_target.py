from typing import List, Dict, Optional
import io
import requests

from datasets import load_dataset
from PIL import Image, UnidentifiedImageError


COCO_DATASET_NAME = "phiyodr/coco2017"
COCO_SPLIT = "train"
COCO_URL_FIELD = "coco_url"
COCO_ID_FIELDS = ["image_id", "id", "cocoid", "file_name"]

REQUEST_TIMEOUT = 20
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; dataset-builder/1.0)"
}


def load_source_dataset(seed: int = 42):
    """
    Load the MS COCO 2017 training split as a streaming Hugging Face dataset
    and shuffle it once for randomized sampling order.
    """
    ds = load_dataset(
        COCO_DATASET_NAME,
        split=COCO_SPLIT,
        streaming=True
    )
    ds = ds.shuffle(seed=seed)
    return ds


def extract_coco_source_id(item: Dict, fallback_idx: int) -> str:
    """
    Pick a stable identifier from a COCO record when possible.
    Falls back to the running index if no better ID field is present.
    """
    for key in COCO_ID_FIELDS:
        if key in item and item[key] is not None:
            return str(item[key])

    return f"coco_{fallback_idx}"


def download_image_bytes(url: str, timeout: int = REQUEST_TIMEOUT) -> Optional[bytes]:
    """
    Download raw image bytes from a COCO image URL.
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


def get_candidate_records(ds, batch_size: int = 200, batch_id: int = 1) -> List[Dict]:
    """
    Return one batch of standardized COCO candidate records.

    Uses 1-based batch indexing to remain consistent with your driver notebook:
        batch_id = 1 -> first batch
        batch_id = 2 -> second batch

    Because the dataset is streaming, this function rebuilds an iterator each
    call and advances until the requested batch range is reached.
    """
    start = (batch_id - 1) * batch_size
    end = start + batch_size

    records = []
    ds_iter = iter(ds)

    for idx, item in enumerate(ds_iter):
        if idx < start:
            continue
        if idx >= end:
            break

        image_url = item.get(COCO_URL_FIELD, None)
        if not image_url:
            continue

        img_bytes = download_image_bytes(image_url)
        if img_bytes is None:
            continue

        image_obj = open_image_from_bytes(img_bytes)
        if image_obj is None:
            continue

        records.append({
            "source_id": extract_coco_source_id(item, idx),
            "source_ref": image_url,
            "image_obj": image_obj,
        })

    return records
    
