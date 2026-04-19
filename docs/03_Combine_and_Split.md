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

The following metadata files are generated:

* `metadata/splits/combined_metadata.csv`
  Full dataset metadata containing all sources.

* `metadata/splits/train_metadata.csv`
  Training subset with balanced representation across all datasets and classes.

* `metadata/splits/test_metadata.csv`
  Independent test subset reserved for final evaluation.

Each file includes the following fields:

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

## Processing Workflow

This notebook executes a structured sequence of steps to construct the final dataset splits:

1. **Environment Setup and Verification**
   The Colab runtime is prepared by cloning the project repository, configuring paths, and verifying the availability of all required preprocessed metadata files.

2. **Metadata Consolidation**
   Metadata from all six datasets is loaded, standardized, and combined into a single unified table. Each entry is annotated with its source dataset and class label.

3. **Dataset Construction**
   The combined dataset is organized and shuffled to prepare for controlled partitioning.

4. **Balanced Train/Test Split**
   A fixed-count split is applied to ensure:

   * Equal representation across all datasets
   * Balanced class distribution
   * Strict separation between training and test data

5. **Output Generation and Validation**
   Final metadata files are written to disk, and validation checks confirm dataset sizes, balance, and integrity.

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

## Role in the Overall Pipeline

This notebook defines the dataset partitions used throughout the remainder of the pipeline. It ensures that training and evaluation are conducted on properly balanced and independent data.

All subsequent steps—feature extraction, normalization, model training, and evaluation—operate based on these split definitions.

---

## Next Step

➡️ [04A Extract Gradient Features](04A_Extract_Gradient_Features.md)


