---
title: 01 Build Dataset
parent: 1. Dataset Tutorial
nav_order: 1
---

# 01 Build Dataset

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/01_Build_Dataset.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

Build a raw image dataset from a selected source, including validation, deduplication, and metadata generation.

## Inputs

- Selected dataset source — one of: ImageNet_1K_256, MS_COCO_2017, DiffusionDB, SDXL_Generated_10K, MidJourney  

## Outputs

- Raw images — stored in `data/raw/<SOURCE_DATASET>/images/`  
- Raw metadata CSV — `<dataset_code>_raw_metadata.csv`  
- Hash files — source and global deduplication records  

## Processing Summary

- Select dataset source  
- Retrieve candidate image records  
- Apply size and duplicate filtering  
- Assign standardized filenames  
- Save images and metadata  
- Track progress and verify dataset integrity  

## Notes

- This notebook is optional if datasets are already available  
- Only one dataset source is processed per run  
- Hash-based deduplication ensures uniqueness across datasets  
- A reset option enables clean rebuilding of a dataset source  

## Next Notebook

➡️ [02 Preprocess Images](02_Preprocess_Images.md)

