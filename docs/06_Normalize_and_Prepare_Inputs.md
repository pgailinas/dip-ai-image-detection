---
title: 06 Normalize and Prepare Inputs
parent: 2. Model Description Tutorial
nav_order: 5
---

# 06 Normalize and Prepare Inputs

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/06_Normalize_and_Prepare_Inputs.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg"
         alt="Open in Colab"
         style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

Normalize feature vectors and prepare final classifier input datasets.

## Inputs

- `train_feature_vectors.csv`, `test_feature_vectors.csv` — combined feature vectors (N samples × 25 features)

## Outputs

- `train_feature_vectors_normalized.csv`, `test_feature_vectors_normalized.csv` — normalized feature vectors (N samples × 25 features)
- `scaler.pkl` — fitted normalization model

## Processing Summary

- Load feature vector datasets
- Separate metadata and feature columns
- Fit normalization transform on training data
- Apply transform to training and test datasets
- Recombine metadata with normalized features
- Validate outputs and save datasets

## Notes

- Normalization is fit only on training data to prevent data leakage
- The same transform is applied to both training and test datasets
- Metadata columns are preserved and excluded from normalization
- Output files are written to the Colab runtime environment

## Next Notebook

➡️ **07 Classifier Selection**




