---
title: 04C Extract Frequency Features
parent: 2. Model Description Tutorial
nav_order: 3
---

# 04C Extract Frequency Features

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/04C_Extract_Frequency_Features.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

Extract frequency-domain features from preprocessed images to capture spectral energy distribution and structural patterns.

## Inputs

- `train_metadata.csv`, `test_metadata.csv` — dataset metadata  
- Preprocessed images — accessed using metadata filenames  

## Outputs

- `train_frequency_features.csv`, `test_frequency_features.csv` — frequency feature datasets (N samples × 8 features)  

## Processing Summary

- Load subset metadata  
- Access preprocessed images using metadata  
- Transform images to frequency domain  
- Extract spectral and radial descriptors  
- Combine features with metadata  
- Save frequency feature datasets  

## Notes

- Processing is performed separately for training and test subsets  
- Image access is metadata-driven using filenames  
- Frequency features capture spectral energy and structural patterns  
- Output files are written to the Colab runtime environment  

## Next Notebook

➡️ [05 Build Feature Vectors](05_Build_Feature_Vectors.md)

