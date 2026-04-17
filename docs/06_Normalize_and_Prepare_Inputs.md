---
title: 06 Normalize and Prepare Inputs
parent: 2. Model Description Tutorial
nav_order: 5
---

# 06 Normalize and Prepare Inputs

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/06_Normalize_and_Prepare_Inputs.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook normalizes the combined DIP feature vectors and prepares the final classifier input datasets.

Normalization ensures that all features are on a comparable scale, which is essential for many machine learning algorithms. The normalization transform is fit using only the training data and then applied to both training and test sets to prevent data leakage.

## Inputs

- Feature vector CSV files:
  - `metadata/vectors/train_feature_vectors.csv`
  - `metadata/vectors/test_feature_vectors.csv`

- Project configuration file:
  - `project_config.py`

## Outputs

- Normalized feature vector CSV files:
  - `metadata/vectors/train_feature_vectors_normalized.csv`
  - `metadata/vectors/test_feature_vectors_normalized.csv`

- Fitted scaler object:
  - `metadata/models/scaler.pkl`

Each normalized CSV contains:
- `filename`
- `class_label`
- `source_dataset`
- `subset`
- 25 normalized DIP feature columns

## Main Tasks

- Load feature vector tables
- Separate metadata from feature columns
- Fit normalization transform on training data
- Apply normalization to training and test sets
- Recombine metadata with normalized features
- Validate output structure
- Save normalized datasets and scaler

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a summary of normalization and input preparation, including purpose, inputs, and outputs.

### Cell 1: Import Libraries and Configuration
Loads required libraries (e.g., Pandas, NumPy, scikit-learn) and imports shared configuration settings.

### Cell 2: Define Input and Output Paths
Defines file paths for input feature vectors, normalized outputs, and scaler storage.

### Cell 3: Load Feature Vector Tables
Reads the training and test feature vector CSV files produced in the previous step.

### Cell 4: Validate Structure and Define Columns
Validates dataset structure, defines metadata columns, and identifies feature columns.

### Cell 5: Separate Metadata and Feature Columns
Splits metadata fields (filename, class label, dataset source, subset) from the numeric feature columns to ensure normalization is applied only to classifier inputs.

### Cell 6: Fit Scaler on Training Features
Fits the normalization transform (e.g., StandardScaler) using only the training feature data to avoid information leakage.

### Cell 7: Transform Training and Test Features
Applies the fitted scaler to both training and test feature sets.

### Cell 8: Recombine Metadata with Normalized Features
Reattaches metadata columns to the normalized feature values, restoring the complete dataset structure.

### Cell 9: Save Normalized Feature Vectors and Scaler
Writes normalized CSV files and saves the fitted scaler object for reuse in evaluation and future inference.

### Cell 10: Validate Normalized Outputs
Verifies:
- Correct number of rows and columns
- Presence of all expected feature columns
- Consistency between training and test datasets

## Notes and Design Choices

- **No data leakage:**  
  The scaler is fit exclusively on training data and then applied to the test set.

- **Feature scaling requirement:**  
  Normalization ensures that features with different ranges contribute appropriately to model training.

- **Reusable preprocessing:**  
  Saving the scaler enables consistent transformation during evaluation and deployment.

- **Metadata preservation:**  
  Metadata columns are handled separately and recombined after normalization.

## Files Produced

- `metadata/vectors/train_feature_vectors_normalized.csv` — Normalized training features
- `metadata/vectors/test_feature_vectors_normalized.csv` — Normalized test features
- `metadata/models/scaler.pkl` — Saved normalization model

## Role in the Overall Pipeline

This notebook prepares the final inputs used for classifier training and evaluation. It ensures that feature data is properly scaled and ready for machine learning algorithms.

## Next Step

➡️ [07 Classifier Selection](07_Classifier_Selection.md)

