---
title: 04A Extract Gradient Features
parent: 2. Model Description Tutorial
nav_order: 1
---

# 04A Extract Gradient Features

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/04A_Extract_Gradient_Features.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

> **Note:** Running notebooks in Google Colab requires a Google account. The preprocessed image archive is downloaded automatically from public Google Drive during execution if needed.

---

## Purpose

Extract gradient-based features from preprocessed images to capture edge structure and directional information.

## Inputs

- `train_metadata.csv`, `test_metadata.csv` — dataset metadata  
- Public Google Drive preprocessed image archive — `All_Sources_preprocessed.zip`  
- Shared project configuration — `src/project_config.py`

## Outputs

- `train_gradient_features.csv`, `test_gradient_features.csv` — gradient feature datasets (N samples × 8 features)  

## Processing Summary

- Load subset metadata  
- Download and extract preprocessed image archive if needed  
- Access preprocessed images using metadata filenames  
- Compute gradient magnitude and orientation  
- Extract statistical descriptors from gradient data  
- Combine features with metadata  
- Save gradient feature datasets  

## Notes

- Processing is performed separately for training and test subsets  
- Image access is metadata-driven using filenames  
- Gradient features capture edge strength and directional structure  
- Feature extraction operates on locally extracted images within the Colab runtime environment  

## Next Notebook

➡️ [04B Extract Spatial Features](04B_Extract_Spatial_Features.md)

