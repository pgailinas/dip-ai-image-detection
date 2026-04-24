---
title: 03 Combine and Split
parent: 1. Dataset Tutorial
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

This notebook combines preprocessed metadata from all dataset sources and creates balanced **train** and **test** splits for downstream machine learning tasks.

---

## Inputs

The notebook uses preprocessed metadata CSV files generated in Notebook 02:

* `metadata/preprocessed/imgn_preprocessed_metadata.csv`
* `metadata/preprocessed/coco_preprocessed_metadata.csv`
* `metadata/preprocessed/open_preprocessed_metadata.csv`
* `metadata/preprocessed/diff_preprocessed_metadata.csv`
* `metadata/preprocessed/sdxl_preprocessed_metadata.csv`
* `metadata/preprocessed/midj_preprocessed_metadata.csv`

All file paths and dataset definitions are provided by `project_config.py`.

---

## Outputs

The following files are generated:

* `metadata/splits/combined_metadata.csv`
* `metadata/splits/train_metadata.csv`
* `metadata/splits/test_metadata.csv`

---

## Workflow Overview

1. **Environment Setup**
   - Load configuration
   - Verify required input files

2. **Define Paths**
   - Set input/output directories from config

3. **Dataset Configuration**
   - Dynamically build dataset definitions from config

4. **Combine Metadata**
   - Load all CSV files
   - Add `source_dataset` and `class_label`
   - Merge into a single dataset

5. **Train/Test Split**
   - Shuffle each dataset independently
   - Split into:
     - 2400 training samples
     - 600 testing samples
   - Combine splits across all datasets
   - Shuffle final train and test sets

6. **Save and Validate**
   - Save combined, train, and test CSV files
   - Validate sizes and distributions

---

## Expected Dataset Sizes

| Dataset | Rows |
|--------|-----|
| Combined | 18,000 |
| Train | 14,400 |
| Test | 3,600 |

---

## Notes

* Splits are **balanced across datasets and class labels**
* Uses a fixed random seed for reproducibility
* Operates entirely on metadata (no image processing)
* Prepares data for feature extraction and model training

---

## Next Step

➡️ [04A Extract Gradient Features](04A_Extract_Gradient_Features.md)
