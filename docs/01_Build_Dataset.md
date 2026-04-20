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

This notebook provides an **optional method** for building a raw image dataset from a **single selected source**.

It retrieves candidate images, applies validation and deduplication, assigns standardized filenames, and generates raw metadata for accepted images.

This notebook can also operate in a **demo mode**, where the dataset is treated as new but no files are written.

---

## Inputs

* Selected dataset source (chosen interactively):

  * ImageNet
  * MS COCO 2017
  * DiffusionDB
  * SDXL-generated images
  * MidJourney images

* Project configuration file:

  * `project_config.py`

---

## Modes of Operation

The notebook supports two modes:

### Persistent Mode (`PERSIST_OUTPUTS = True`)
* Images are saved to disk
* Metadata CSV files are written
* Hash files are updated

### Demo Mode (`PERSIST_OUTPUTS = False`)
* Existing datasets are ignored
* No files are written
* Metadata and hashes are stored in memory only

This allows safe testing and demonstration without modifying existing data.

---

## Outputs

### Persistent Mode

For the selected dataset source:

* Images:
  * `data/raw/<SOURCE_DATASET>/images/`

* Metadata:
  * `data/metadata/[dataset_code]_raw_metadata.csv`

* Hash files:
  * `data/metadata/[target_name]_source_hashes.json`
  * `data/metadata/global_hashes.json`

### Demo Mode

* No files are written
* Metadata rows and hash sets exist in memory only

---

## Main Tasks

* Select dataset source or skip execution
* Load target-specific dataset module
* Retrieve candidate image records
* Apply:
  * size filtering (≥256×256)
  * duplicate filtering (SHA-256, source + global)
* Assign standardized filenames
* Generate metadata rows for accepted images
* Build dataset iteratively in batches
* Track progress and performance

---

## Processing Workflow

1. **Environment Setup**
   Initialize runtime, paths, and execution mode.

2. **Dataset Selection**
   Choose one dataset source or skip execution.

3. **Target Module Loading**
   Load dataset-specific logic from `src/targets/`.

4. **Configuration**
   Define dataset paths, metadata files, and hash tracking.

5. **Utilities Initialization**
   Prepare:
   * metadata handling
   * hash tracking
   * filename generation
   * image validation

6. **Dataset Loading**
   Load source dataset into memory or iterable form.

7. **Candidate Processing**
   For each candidate image:
   * normalize format
   * enforce size constraints
   * compute SHA-256 hash
   * reject duplicates
   * assign filename
   * generate metadata row

8. **Batch Processing**
   Iterate through dataset using:
   * module-based indexing, or
   * notebook-side iteration (for iterable datasets)

9. **Progress Tracking**
   Display:
   * accepted image count
   * batch statistics
   * progress bar

10. **Verification**
    Validate:
    * image vs metadata consistency (persistent mode)
    * metadata vs hash consistency (demo mode)

11. **Final Summary**
    Report:
    * total processed images
    * accepted images
    * acceptance rate
    * sample metadata rows (demo mode)

---

## Supported Datasets

| Target Name | Dataset            | Class |
|------------|--------------------|-------|
| imagenet   | ImageNet_1K_256    | real  |
| coco       | MS_COCO_2017       | real  |
| diffusiondb| DiffusionDB        | ai    |
| sdxl       | SDXL Generated     | ai    |
| midjourney | MidJourney         | ai    |

**OpenImages is not supported** due to its very large size (>20 GB).

---

## Expected Size

* ~3000 accepted images per dataset
* ~15,000 images across Notebook 01 sources
* ~18,000 images total across full project

---

## Notes and Design Choices

* **Optional notebook**
  Users may skip this step and proceed directly to preprocessing.

* **Single-source processing**
  Only one dataset is handled per run for clarity and control.

* **Demo mode support**
  Enables safe experimentation without modifying stored datasets.

* **Hash-based deduplication**
  Ensures dataset uniqueness both within and across sources.

* **Flexible dataset handling**
  Supports both indexed datasets and streaming/iterable datasets.

* **No preprocessing performed**
  All image preprocessing occurs in the next notebook.

---

## Role in the Overall Pipeline

This notebook provides an **optional dataset construction step**.

It can be used to:
* build datasets from source APIs
* regenerate datasets
* test filtering and deduplication logic

However, the main pipeline can proceed using existing datasets without running this notebook.

---

## Next Step

➡️ [02 Preprocess Images](02_Preprocess_Images.md)


