from typing import List, Dict
from datasets import load_dataset

IMAGENET_DATASET_NAME = "benjamin-paine/imagenet-1k-256x256"
IMAGENET_SPLIT = "train"
IMAGENET_SEED = 42


def load_source_dataset(seed: int = 42):
    """
    Load the ImageNet-1K-256 dataset as a streaming Hugging Face dataset,
    then shuffle it once for randomized sampling order.
    """
    ds = load_dataset(
        IMAGENET_DATASET_NAME,
        split=IMAGENET_SPLIT,
        streaming=True
    )
    ds = ds.shuffle(seed=seed)
    return ds


def extract_imagenet_source_id(item: Dict, fallback_idx: int) -> str:
    """
    Pick a stable identifier from the ImageNet record when possible.
    Falls back to the running index if no explicit ID field is present.
    """
    if "id" in item and item["id"] is not None:
        return str(item["id"])

    return f"imagenet_{fallback_idx}"


def get_candidate_records(ds, batch_size: int = 200, batch_id: int = 1) -> List[Dict]:
    """
    Return one batch of standardized candidate records.

    This function uses 1-based batch indexing to remain consistent with
    your original notebook behavior:
        batch_id = 1 -> first batch
        batch_id = 2 -> second batch

    Because the dataset is streaming, we advance the iterator until the
    requested batch is reached.
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

        image_obj = item.get("image", None)

        records.append({
            "source_id": extract_imagenet_source_id(item, idx),
            "source_ref": f"huggingface://{IMAGENET_DATASET_NAME}/{IMAGENET_SPLIT}",
            "image_obj": image_obj,
        })

    return records
    
