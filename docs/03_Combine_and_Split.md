---
title: 03 Combine and Split
parent: 1. Dataset Tutorial
nav_order: 3
---

# 03 Combine and Split

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/03_Combine_and_Split.ipynb)

---

## Purpose

This notebook combines all preprocessed dataset metadata into a single unified table and performs a controlled split into training and test datasets.

The split is designed to preserve class balance and ensure equal representation from all six source datasets. The resulting training set is used for model development and cross-validation, while the test set is held out for final independent evaluation.

## Inputs

- Preprocessed metadata CSV files:
  - `imgn_preprocessed_metadata.csv`
  - `coco_preprocessed_metadata.csv`
  - `open_preprocessed_metadata.csv`
  - `diff_preprocessed_metadata.csv`
  - `sdxl_preprocessed_metadata.csv`
  - `mj_preprocessed_metadata.csv`

- Project configuration file:
  - `project_config.py`

## Outputs

- Combined dataset metadata:
  - `combined_metadata.csv`

- Split datasets:
  - `train_metadata.csv`
  - `test_metadata.csv`

Each CSV contains:
- `filename`
- `class_label`
- `source_dataset`
- `subset` (train or test)

## Main Tasks

- Load preprocessed metadata for all datasets
- Concatenate metadata into a single table
- Shuffle and organize dataset entries
- Perform a balanced train/test split
- Ensure equal representation across datasets and classes
- Save combined and split metadata tables

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a high-level description of dataset combination and splitting strategy, including assumptions and outputs.

### Cell 1: Import Libraries and Configuration
Loads required libraries and imports shared configuration settings such as file paths, split ratios, and dataset parameters.

### Cell 2: Load Preprocessed Metadata
Reads all preprocessed metadata CSV files and prepares them for combination.

### Cell 3: Combine Metadata Tables
Concatenates all dataset metadata into a single unified DataFrame representing the full dataset.

### Cell 4: Shuffle Combined Dataset
Randomizes the order of entries to eliminate any ordering bias prior to splitting.

### Cell 5: Perform Balanced Train/Test Split
Splits the dataset into training and test subsets while:
- Maintaining class balance (real vs AI)
- Preserving equal representation from each dataset source

### Cell 6: Assign Subset Labels
Adds a `subset` column to indicate whether each sample belongs to the training or test set.

### Cell 7: Validate Split Integrity
Verifies that:
- Class distributions are balanced
- Each dataset is proportionally represented
- Total counts match expected values

### Cell 8: Save Combined and Split Metadata
Writes the combined dataset and the train/test splits to CSV files for use in subsequent pipeline stages.

## Notes and Design Choices

- **Metadata-only splitting:**  
  No image files are moved or duplicated; dataset partitions are defined entirely through metadata.

- **Balanced dataset design:**  
  Equal representation is maintained across both class labels and dataset sources.

- **Two-way split with cross-validation:**  
  A dedicated validation set is not created. Instead, model validation is performed using cross-validation on the training set, while the test set remains untouched for final evaluation.

- **Reproducibility:**  
  Shuffling and splitting operations are controlled to ensure consistent results across runs.

## Files Produced

- `combined_metadata.csv` — Full dataset metadata (all sources)
- `train_metadata.csv` — Training subset metadata
- `test_metadata.csv` — Test subset metadata

## Role in the Overall Pipeline

This notebook defines the dataset partitions used throughout the remainder of the pipeline. It ensures that training and evaluation are conducted on properly balanced and independent data.

All subsequent steps—feature extraction, normalization, model training, and evaluation—operate based on these split definitions.

## Next Step

➡️ [04A Extract Gradient Features](04A_Extract_Gradient_Features.md)
