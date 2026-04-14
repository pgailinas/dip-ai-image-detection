---
title: 05 Build Feature Vectors
nav_order: 7
---

# 05 Build Feature Vectors

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/05_Build_Feature_Vectors.ipynb)

---

## Purpose

This notebook combines the three groups of extracted features—gradient, spatial, and frequency—into unified feature vectors for each image.

The result is a structured dataset containing a **26-dimensional DIP feature vector** per image, which serves as the input to downstream normalization and classifier training steps.

## Inputs

- Gradient feature CSV files:
  - `train_gradient_features.csv`
  - `test_gradient_features.csv`

- Spatial feature CSV files:
  - `train_spatial_features.csv`
  - `test_spatial_features.csv`

- Frequency feature CSV files:
  - `train_frequency_features.csv`
  - `test_frequency_features.csv`

- Project configuration file:
  - `project_config.py`

## Outputs

- Combined feature vector CSV files:
  - `train_feature_vectors.csv`
  - `test_feature_vectors.csv`

Each CSV contains:
- `filename`
- `class_label`
- `source_dataset`
- `subset`
- 26 DIP feature columns

## Main Tasks

- Load feature tables from all three feature groups
- Align datasets using common identifiers
- Merge feature sets into unified tables
- Verify feature completeness and consistency
- Save combined feature vector CSV files

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a summary of feature vector construction, including purpose, inputs, and outputs.

### Cell 1: Import Libraries and Configuration
Loads required libraries (e.g., Pandas, NumPy) and imports shared configuration settings.

### Cell 2: Load Feature Tables
Reads gradient, spatial, and frequency feature CSV files for both training and test datasets.

### Cell 3: Verify Alignment of Feature Tables
Ensures that all feature tables share consistent ordering and matching identifiers (filename, class label, dataset, subset).

### Cell 4: Merge Feature Groups
Combines gradient, spatial, and frequency features into a single DataFrame for each dataset (train and test).

### Cell 5: Construct Final Feature Vectors
Assembles the full feature vector representation by concatenating all feature columns into a unified structure.

### Cell 6: Validate Feature Vector Tables
Verifies:
- Correct number of rows
- Presence of all 26 feature columns
- No missing or duplicated entries
- Consistency between training and test sets

### Cell 7: Save Feature Vector CSV Files
Writes the final training and test feature vector tables to CSV files for downstream processing.

## Notes and Design Choices

- **Modular feature design:**  
  Features are extracted in separate groups and combined in this step to maintain modularity and flexibility.

- **Consistent alignment:**  
  Strict alignment across feature tables ensures that all features correspond to the correct image samples.

- **Fixed feature dimensionality:**  
  Each image is represented by a 26-dimensional feature vector, enabling consistent input to machine learning models.

- **Metadata preservation:**  
  Identifiers such as filename, class label, and dataset source are retained alongside feature values.

## Files Produced

- `train_feature_vectors.csv` — Combined feature vectors for training set
- `test_feature_vectors.csv` — Combined feature vectors for test set

## Role in the Overall Pipeline

This notebook produces the final feature representation used as input to the classifier. It serves as the bridge between feature extraction and model preparation.

All subsequent steps operate directly on these feature vector tables.

## Next Step

➡️ [06 Normalize and Prepare Inputs](06_Normalize_and_Prepare_Inputs.md)

