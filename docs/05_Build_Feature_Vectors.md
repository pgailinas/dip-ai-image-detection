---
title: 05 Build Feature Vectors
parent: 2. Model Description Tutorial
nav_order: 4
---

# 05 Build Feature Vectors

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/05_Build_Feature_Vectors.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg"
         alt="Open in Colab"
         style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

Combine gradient, spatial, and frequency-domain feature groups into unified **feature vectors** for each image.

---

## Inputs

### Training Data
- `train_gradient_features.csv` — gradient features (N × 8)  
- `train_spatial_features.csv` — spatial features (N × 9)  
- `train_frequency_features.csv` — frequency features (N × 8)  

### Test Data
- `test_gradient_features.csv` — gradient features (N × 8)  
- `test_spatial_features.csv` — spatial features (N × 9)  
- `test_frequency_features.csv` — frequency features (N × 8)  

---

## Outputs

* `train_feature_vectors.csv` — combined feature vectors (N samples × 25 features)
* `test_feature_vectors.csv` — combined feature vectors for test dataset

---

## Key Steps

1. Load feature datasets for train and test subsets
2. Verify alignment across feature groups
3. Merge feature groups using shared metadata
4. Validate structure and completeness
5. Save combined feature vector datasets

---

## Notes

* This notebook performs **data merging only** (no feature extraction)
* Dataset integrity is enforced through strict alignment checks
* Training and test datasets remain fully separated
* Output files are written to the Colab runtime environment

---

## Next Step

➡️ **06 Normalize and Prepare Inputs**




