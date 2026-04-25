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

Combine gradient, spatial, and frequency-domain features into unified feature vectors for each image.

## Inputs

- `train_gradient_features.csv`, `test_gradient_features.csv` — gradient feature values per image (N samples × 8 features)
- `train_spatial_features.csv`, `test_spatial_features.csv` — spatial feature values per image (N samples × 9 features)
- `train_frequency_features.csv`, `test_frequency_features.csv` — frequency-domain feature values per image (N samples × 8 features)

## Outputs

- `train_feature_vectors.csv` — combined feature vectors for training dataset (N samples × 25 features)
- `test_feature_vectors.csv` — combined feature vectors for test dataset (N samples × 25 features)

## Processing Summary

- Load feature datasets for train and test subsets
- Verify alignment across feature groups
- Merge feature groups using shared metadata
- Validate structure and completeness
- Save combined feature vector datasets

## Notes

- This notebook performs **data merging only** (no feature extraction)
- Dataset integrity is enforced through strict alignment checks
- Training and test datasets remain fully separated
- Output files are written to the Colab runtime environment

## Next Notebook

➡️ [06 Normalize and Prepare Inputs](06_Normalize_and_Prepare_Inputs.md)

