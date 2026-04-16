---
title: "03 Combine and Split"
parent: "1. Dataset Tutorial"
nav_order: 3
---

# 03 Combine and Split

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/03_Combine_and_Split.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook combines all preprocessed dataset metadata into a single unified table and performs a controlled split into training and test datasets.

The split preserves class balance and ensures equal representation from all six source datasets. The resulting training set is used for model development and cross-validation, while the test set is held out for final independent evaluation.

---

## Inputs

* Preprocessed metadata CSV files (from GitHub repository):

  * `metadata/preprocessed/imgn_preprocessed_metadata.csv`
  * `metadata/preprocessed/coco_preprocessed_metadata.csv`
  * `metadata/preprocessed/open_preprocessed_metadata.csv`
  * `metadata/preprocessed/diff_preprocessed_metadata.csv`
  * `metadata/preprocessed/sdxl_preprocessed_metadata.csv`
  * `metadata/preprocessed/mj_preprocessed_metadata.csv`

* Project configuration file:

  * `src/project_config.py`

---

## Outputs

* Combined dataset metadata:

  * `metadata/splits/combined_metadata.csv`

* Split datasets:

  * `metadata/splits/train_metadata.csv`
  * `metadata/splits/test_metadata.csv`

Each CSV contains:

* `filename`
* `class_label`
* `source_dataset`
* `subset` (train or test)

---

## Main Tasks

* Clone the GitHub repository into the Colab runtime
* Load preprocessed metadata for all datasets
* Concatenate metadata into a single table
* Shuffle and organize dataset entries
* Perform a balanced train/test split
* Ensure equal representation across datasets and classes
* Save combined and split metadata tables
* Validate output file integrity and dataset sizes

---

## Cell-by-Cell Description

### Startup (Environment + Verification)

* Clone the GitHub repository into the Colab runtime
* Configure access to `src/project_config.py`
* Define local input/output directories
* Verify all required metadata CSV files are present

---

### Cell 1: Define Paths

* Define local runtime paths for:

  * input metadata (`metadata/preprocessed`)
  * output metadata (`metadata/splits`)

---

### Cell 2: Dataset Configuration

* Define dataset-specific parameters:

  * CSV filenames
  * source dataset names
  * class labels

---

### Cell 3: Combine Metadata Tables

* Load all preprocessed metadata CSV files
* Add:

  * `source_dataset`
  * `class_label`
  * `image_path`
* Combine into a single unified DataFrame
* Save `combined_metadata.csv`

---

### Cell 4: Split, Save, and Validate Metadata

* Shuffle each dataset independently
* Perform exact-count train/test splits:

  * 2400 training samples per dataset
  * 600 test samples per dataset
* Combine all splits into final training and test datasets
* Shuffle each subset independently
* Save:

  * `train_metadata.csv`
  * `test_metadata.csv`
* Validate:

  * dataset sizes
  * class balance
  * dataset representation
  * file existence and shapes

---

## Notes and Design Choices

* **Metadata-only splitting:**
  No image files are moved or duplicated; dataset partitions are defined entirely through metadata.

* **Balanced dataset design:**
  Equal representation is maintained across both class labels and dataset sources.

* **Two-way split with cross-validation:**
  A dedicated validation set is not created. Instead, model validation is performed using cross-validation on the training set, while the test set remains untouched for final evaluation.

* **GitHub-based workflow:**
  All required files are sourced from the GitHub repository, and processing occurs within the Colab local runtime.

* **Reproducibility:**
  Shuffling and splitting operations use a fixed random seed to ensure consistent results across runs.

---

## Files Produced

* `combined_metadata.csv` — Full dataset metadata (all sources)
* `train_metadata.csv` — Training subset metadata
* `test_metadata.csv` — Test subset metadata

---

## Role in the Overall Pipeline

This notebook defines the dataset partitions used throughout the remainder of the pipeline. It ensures that training and evaluation are conducted on properly balanced and independent data.

All subsequent steps—feature extraction, normalization, model training, and evaluation—operate based on these split definitions.

---

## Next Step

➡️ [04A Extract Gradient Features](04A_Extract_Gradient_Features.md)

