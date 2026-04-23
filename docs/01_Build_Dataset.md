---
title: 01 Build Dataset
parent: 1. Dataset Tutorial
nav_order: 1
---

# 01 Build Dataset

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/01_Build_Dataset.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook provides an **optional, reproducible method** for building a raw image dataset from a **single selected source**.

It retrieves candidate images, applies validation and deduplication, assigns standardized filenames, and generates raw metadata for accepted images.

A **source reset mechanism** enables clean rebuilding of any dataset source without manual file cleanup.

---

## Inputs

* Selected dataset source (chosen interactively):

  * ImageNet_1K_256
  * MS_COCO_2017
  * DiffusionDB
  * SDXL_Generated_10K
  * MidJourney
  * OpenImages *(not supported due to size)*

* Project configuration:

  * `project_config.py`

---

## Reset-Based Workflow (Key Feature)

This notebook uses a **forward-only execution model**.

An optional reset step allows rebuilding a dataset cleanly:

### Reset Step

When enabled, the notebook:

* Removes the current source hashes from the global hash set
* Deletes:

  * source hash JSON
  * raw metadata CSV
  * source image directory
* Recreates required directories

This ensures:

* no duplicate rejection from prior runs
* deterministic rebuild behavior
* no need to rerun earlier cells

---

## Outputs

For the selected dataset source:

### Images

```text
data/raw/<SOURCE_DATASET>/images/
```

---

### Raw Metadata CSV

```text
data/metadata/original/<dataset_code>_raw_metadata.csv
```

---

### Hash Files

```text
data/metadata/hashes/<dataset_code>_source_hashes.json
data/metadata/hashes/global_hashes.json
```

---

## Main Tasks

* Select dataset source or skip execution
* Load dataset-specific module
* Retrieve candidate image records
* Apply:

  * size filtering (≥256×256)
  * duplicate filtering (SHA-256, source + global)
* Assign standardized filenames
* Generate metadata rows
* Build dataset in batches
* Track progress and performance
* Verify output consistency

---

## Processing Workflow

1. **Environment Setup**
   Load configuration and initialize paths.

2. **Dataset Selection**
   Choose dataset source or skip execution.

3. **Target Module Loading**
   Load dataset logic from `src/datasets/`.

4. **Common Configuration**
   Define dataset-specific paths and files.

5. **Reset Source State (Optional)**
   Cleanly remove prior dataset state.

6. **Metadata Initialization**
   Create raw metadata CSV with header.

7. **Hash Initialization**
   Load source and global hash sets.

8. **Utility Setup**
   Initialize filename, validation, and append utilities.

9. **Dataset Loading**
   Load dataset for iteration.

10. **Candidate Processing**
    For each image:

* normalize format
* enforce size constraint
* compute SHA-256 hash
* reject duplicates
* assign filename
* save image
* append metadata

11. **Batch Processing**
    Iterate until target count is reached.

12. **Progress Tracking**
    Display batch statistics and progress.

13. **Verification**
    Ensure image count matches metadata rows.

14. **Final Summary**
    Report dataset statistics and completion.

---

## Supported Datasets

| Target Name | Dataset         | Class |
| ----------- | --------------- | ----- |
| imagenet    | ImageNet_1K_256 | real  |
| coco        | MS_COCO_2017    | real  |
| openimages  | OpenImages      | real  |
| diffusiondb | DiffusionDB     | ai    |
| sdxl        | SDXL Generated  | ai    |
| midjourney  | MidJourney      | ai    |

**OpenImages is intentionally excluded** due to its very large size (>20 GB).

---

## Expected Size

* ~3000 accepted images per dataset
* ~18,000 images total across the full project

---

## Notes and Design Choices

* **Optional notebook**
  Can be skipped if datasets already exist

* **Single-source execution**
  One dataset processed per run

* **Reset-based rebuild model**
  Eliminates manual cleanup and ordering issues

* **Hash-based deduplication**
  Ensures uniqueness within and across sources

* **Deterministic pipeline**
  Same inputs produce the same outputs

* **Local/GitHub-based workflow**
  No dependency on Google Drive

* **No preprocessing performed**
  Preprocessing occurs in the next notebook

---

## Role in the Overall Pipeline

This notebook provides an **optional dataset construction stage**.

It can be used to:

* build datasets from source APIs
* regenerate datasets
* validate filtering and deduplication

The pipeline can proceed using prebuilt datasets without running this notebook.

---

## Next Step

➡️ [02 Preprocess Images](02_Preprocess_Images.md)



