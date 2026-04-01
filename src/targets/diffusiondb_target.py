from typing import List, Dict
from datasets import load_dataset

DIFFUSIONDB_CONFIG = "2m_random_5k"

def load_source_dataset(seed: int = 42):
    ds = load_dataset(
        "poloclub/diffusiondb",
        DIFFUSIONDB_CONFIG,
        split="train",
        trust_remote_code=True
    )
    ds = ds.shuffle(seed=seed)
    return ds

from typing import List, Dict

def get_candidate_records(
    ds,
    batch_size: int = 1000,
    batch_id: int = 0
) -> List[Dict]:

    # Compute slice range (0-based batch_id)
    start = (batch_id - 1) * batch_size
    end = min(start + batch_size, len(ds))

    if start >= len(ds):
        return []

    records = []

    for idx in range(start, end):
        try:
            item = ds[idx]

            # Ensure image exists
            if "image" not in item or item["image"] is None:
                continue

            records.append({
                "source_id": f"diffusiondb_{idx}",
                "source_ref": f"huggingface://poloclub/diffusiondb/{DIFFUSIONDB_CONFIG}/{idx}",
                "image_obj": item["image"]
            })

        except Exception as e:
            print(f"Skipping index {idx}: {e}")
            continue

    return records
