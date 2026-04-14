---
title: 03 Combine and Split
nav_order: 3
---

# 03 Combine and Split

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/03_Combine_and_Split.ipynb)

---

## Overview

This notebook combines all preprocessed datasets into a unified dataset and creates balanced, leakage-aware train/validation/test splits.

---

## Objectives

* Combine datasets into a single structure
* Maintain class and source balance
* Prevent cross-split contamination
* Create reproducible 70 / 15 / 15 splits

---

## Workflow

1. Load all dataset metadata
2. Standardize schema
3. Combine datasets
4. Shuffle within sources
5. Split each dataset independently
6. Merge splits
7. Final shuffle
8. Save outputs
9. Validate distributions

---

## Notebook Structure

### Cell 0 — Overview

Defines dataset combination strategy and emphasizes leakage prevention. 

### Cell 1 — Imports

Loads required libraries (pandas, numpy, os). 

### Cell 2 — Dataset Paths

Defines input metadata CSV paths and output file locations. 

### Cell 3 — Load Metadata

Loads all dataset CSVs and verifies structure. 

### Cell 4 — Standardize Columns

Ensures consistent schema across datasets. 

### Cell 5 — Combine Datasets

Concatenates all datasets into a unified DataFrame. 

### Cell 6 — Shuffle Within Source

Shuffles data independently per dataset to avoid ordering bias. 

### Cell 7 — Split Each Source

Applies 70 / 15 / 15 split per dataset source. 

### Cell 8 — Merge Splits

Combines per-source splits into final train/validation/test datasets. 

### Cell 9 — Final Shuffle

Randomizes each subset independently. 

### Cell 10 — Add Subset Labels

Adds subset column (train / validate / test). 

### Cell 11 — Save Outputs

Writes combined and split CSV files. 

### Cell 12 — Validation Checks

Verifies dataset sizes and balance. 

### Cell 13 — Distribution Reporting

Displays dataset breakdown by subset, class, and source. 

---

## Outputs

* combined_metadata.csv
* train_metadata.csv (8400)
* validate_metadata.csv (1800)
* test_metadata.csv (1800)

---

## Key Design Features

* Source-aware splitting prevents leakage
* Balanced class and dataset representation
* Reproducible dataset construction

---

## Next Step

➡️ [04A Extract Gradient Features](04A_Extract_Gradient_Features.md)
