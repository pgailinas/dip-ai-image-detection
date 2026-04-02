# 05 Build Feature Vectors

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/05_Build_Feature_Vectors.ipynb)

---

## Overview

This notebook combines extracted feature sets into unified feature vectors and prepares datasets for machine learning.

---

## Objectives

* Merge feature sets
* Align features across datasets
* Separate features and labels
* Normalize features
* Prepare training inputs

---

## Workflow

1. Load metadata splits
2. Load feature CSVs
3. Merge features
4. Separate X and y
5. Align features
6. Handle missing values
7. Normalize features
8. Save outputs

---

## Notebook Structure

### Cell 0 — Overview

Defines purpose and expected outputs. 

### Cell 1 — Imports

Loads pandas, numpy, sklearn utilities. 

### Cell 2 — Load Metadata

Loads train, validation, and test metadata. 

### Cell 3 — Load Feature CSVs

Loads gradient, spatial, and frequency features. 

### Cell 4 — Merge Feature Sets

Joins feature tables into unified dataset. 

### Cell 5 — Separate Features and Labels

Extracts:

* X (features)
* y (labels) 

### Cell 6 — Feature Alignment

Ensures consistent feature ordering across datasets. 

### Cell 7 — Handle Missing Values

Checks and resolves NaNs or inconsistencies. 

### Cell 8 — Normalize Features

Applies standard scaling using training data only. 

### Cell 9 — Save Scaler

Stores normalization parameters for reuse. 

### Cell 10 — Final Outputs

Generates X_train, X_validation, X_test and labels. 

### Cell 11 — Validation Checks

Verifies shapes and scaling correctness. 

---

## Outputs

* X_train, X_validation, X_test
* y_train, y_validation, y_test
* Scaler parameters

---

## Key Design Features

* Unified feature vector construction
* Training-only normalization
* Robust feature alignment

---

## Next Step

➡️ **06 Normalize and Prepare Inputs**


