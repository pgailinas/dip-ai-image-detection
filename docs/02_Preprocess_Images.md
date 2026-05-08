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

> **Note:** Running notebooks in Google Colab requires a Google account. Dataset ZIP archives are downloaded automatically from publicly shared Google Drive links during execution.

---

## Purpose

Preprocess raw images from a selected dataset source into a standardized format for feature extraction.

## Inputs

- Selected dataset source — one dataset processed per run  
- Public Google Drive ZIP archives — source-specific image datasets  
- Shared project configuration — `src/project_config.py`

## Outputs

- Preprocessed images — stored in `data/preprocessed/<dataset>/images/`  
- Preprocessed metadata CSV — `metadata/preprocessed/<dataset>_preprocessed_metadata.csv`

## Processing Summary

- Select dataset source  
- Download dataset ZIP archive from public Google Drive  
- Extract raw image archive into the Colab runtime  
- Resize images to standard dimensions  
- Convert images to grayscale  
- Save processed images with original filenames  
- Generate metadata for processed images  
- Validate output consistency  

## Notes

- Only one dataset source is processed per run  
- ZIP archives are downloaded temporarily into the Colab runtime environment  
- OpenImages is excluded because of large archive size constraints  
- Filenames are preserved between raw and processed datasets  
- Validation ensures image counts match metadata records  

## Next Notebook

➡️ [03 Combine and Split](03_Combine_and_Split.md)

