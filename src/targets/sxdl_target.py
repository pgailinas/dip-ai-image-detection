from typing import List, Dict
from datasets import load_dataset

SDXL_DATASET_NAME = "ash12321/sdxl-generated-10k"
SDXL_SPLIT = "train"


def load_source_dataset(seed: int = 42):
    """
    Load the SDXL Generated 10K dataset and shuffle once for randomized order.
    """
    ds = load_dataset(
        SDXL_DATASET_NAME,
        split=SDXL_SPLIT
    )
    ds = ds.shuffle(seed=seed)
    return ds


def get_candidate_records(ds, batch_size: int = 200, batch_id: int = 1) -> List[Dict]:
    """
    Return one batch of standardized candidate records.

    Uses 1-based batch indexing to remain consistent with the driver notebook:
        batch_id = 1 -> first batch
        batch_id = 2 -> second batch
    """
    start = (batch_id - 1) * batch_size
    end = min(start + batch_size, len(ds))

    if start >= len(ds):
        return []

    records = []

    for idx in range(start, end):
        item = ds[idx]

        records.append({
            "source_id": f"sdxl_{item['index']}",
            "source_ref": f"huggingface://{SDXL_DATASET_NAME}/{SDXL_SPLIT}/{item['index']}",
            "image_obj": item["image"]
        })

    return records
    
