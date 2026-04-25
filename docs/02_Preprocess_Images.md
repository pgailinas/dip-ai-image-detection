---
title: 02 Preprocess Images
parent: 1. Dataset Tutorial
nav_order: 2
---

# 02 Preprocess Images

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/02_Preprocess_Images.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

Preprocess raw images from a selected dataset source into a standardized format for feature extraction.

## Inputs

- Selected dataset source — one dataset processed per run  
- Raw dataset ZIP files — source-specific image archives  

## Outputs

- Preprocessed images — stored in `/content/preprocessed/<dataset>/images/`  
- Preprocessed metadata CSV — `<dataset>_preprocessed_metadata.csv`  

## Processing Summary

- Select dataset source  
- Extract raw image archive  
- Resize images to standard dimensions  
- Convert images to grayscale  
- Save processed images with original filenames  
- Generate metadata for processed images  
- Validate output consistency  

## Notes

- Only one dataset source is processed per run  
- Processed images are stored in the Colab runtime and are not persisted  
- Filenames are preserved between raw and processed datasets  
- Validation ensures image counts match metadata records  

## Next Notebook

➡️ **03 Combine and Split**
