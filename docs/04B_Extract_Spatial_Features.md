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

> **Note:** Running notebooks in Google Colab requires a Google account. The preprocessed image archive is downloaded automatically from public Google Drive during execution if needed.

---

## Purpose

Extract spatial-domain features from preprocessed images to capture intensity distribution, texture, and structural complexity.

## Inputs

- `train_metadata.csv`, `test_metadata.csv` — dataset metadata  
- Public Google Drive preprocessed image archive — `All_Sources_preprocessed.zip`  
- Shared project configuration — `src/project_config.py`

## Outputs

- `train_spatial_features.csv`, `test_spatial_features.csv` — spatial feature datasets (N samples × 9 features)  

## Processing Summary

- Load subset metadata  
- Download and extract preprocessed image archive if needed  
- Access preprocessed images using metadata filenames  
- Compute spatial-domain statistics  
- Extract intensity and texture descriptors  
- Combine features with metadata  
- Save spatial feature datasets  

## Notes

- Processing is performed separately for training and test subsets  
- Image access is metadata-driven using filenames  
- Spatial features capture intensity, contrast, and texture characteristics  
- Feature extraction operates on locally extracted images within the Colab runtime environment  

## Next Notebook

➡️ [04C Extract Frequency Features](04C_Extract_Frequency_Features.md)

