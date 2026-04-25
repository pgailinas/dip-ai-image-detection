---
title: 04B Extract Spatial Features
parent: 2. Model Description Tutorial
nav_order: 2
---

# 04B Extract Spatial Features

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/04B_Extract_Spatial_Features.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

Extract spatial-domain features from preprocessed images to capture intensity distribution, texture, and structural complexity.

## Inputs

- `train_metadata.csv`, `test_metadata.csv` — dataset metadata  
- Preprocessed images — accessed using metadata filenames  

## Outputs

- `train_spatial_features.csv`, `test_spatial_features.csv` — spatial feature datasets (N samples × 9 features)  

## Processing Summary

- Load subset metadata  
- Access preprocessed images using metadata  
- Compute spatial-domain statistics  
- Extract intensity and texture descriptors  
- Combine features with metadata  
- Save spatial feature datasets  

## Notes

- Processing is performed separately for training and test subsets  
- Image access is metadata-driven using filenames  
- Spatial features capture intensity, contrast, and texture characteristics  
- Output files are written to the Colab runtime environment  

## Next Notebook

➡️ [04C Extract Frequency Features](04C_Extract_Frequency_Features.md)

