from typing import Dict, Any, List
from itertools import islice

from datasets import load_dataset

MIDJOURNEY_DATASET_NAME = "bitmind/GenImage_MidJourney"
MIDJOURNEY_SPLIT = "train"
MIDJOURNEY_STREAM = True
MIDJOURNEY_SHUFFLE_BUFFER = 1000
MIDJOURNEY_PARQUET_GLOB = "hf://datasets/bitmind/GenImage_MidJourney/**/*.parquet"


def load_source_dataset():
    import os
    from datasets import load_dataset

    # Midjourney-specific fix for large parquet shards
    os.environ["HF_HUB_DOWNLOAD_TIMEOUT"] = "120"
    os.environ["HF_HUB_ETAG_TIMEOUT"] = "120"

    return load_dataset(
        "parquet",
        data_files={
            "train": "hf://datasets/bitmind/GenImage_MidJourney/**/*.parquet"
        },
        split=MIDJOURNEY_SPLIT,
        streaming=MIDJOURNEY_STREAM
    )

    if seed is not None:
        ds = ds.shuffle(seed=seed, buffer_size=MIDJOURNEY_SHUFFLE_BUFFER)

    return ds



def extract_midjourney_source_id(item: Dict[str, Any], fallback_idx: int) -> str:
    """
    Pick a stable identifier from the dataset record when possible.
    Falls back to the running index if no explicit ID field is present.
    """
    for key in ["id", "image_id", "index", "idx", "file_name", "filename"]:
        if key in item and item[key] is not None:
            return str(item[key])

    return f"midjourney_{fallback_idx}"



def get_candidate_records(ds, batch_size: int = 200, batch_id: int = 1) -> List[Dict[str, Any]]:
    """
    Return a batch of standardized candidate records from a streaming dataset.

    Each record contains:
      - source_id   : stable-ish identifier for bookkeeping
      - source_ref  : Hugging Face style reference string
      - image_obj   : decoded PIL image object supplied by the dataset loader
    """
    if batch_id < 1:
        raise ValueError("batch_id must be >= 1")
    if batch_size < 1:
        raise ValueError("batch_size must be >= 1")

    start = (batch_id - 1) * batch_size
    stop = start + batch_size

    batch_items = list(islice(ds, start, stop))

    records: List[Dict[str, Any]] = []
    for offset, item in enumerate(batch_items):
        idx = start + offset
        source_id = extract_midjourney_source_id(item, idx)
        records.append(
            {
                "source_id": source_id,
                "source_ref": f"huggingface://{MIDJOURNEY_DATASET_NAME}/{MIDJOURNEY_SPLIT}/{source_id}",
                "image_obj": item["image"],
            }
        )

    return records
