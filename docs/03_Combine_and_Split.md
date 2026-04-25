---
title: 03 Combine and Split
parent: 1. Dataset Tutorial
nav_order: 3
---

# 03 Combine and Split

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/03_Combine_and_Split.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

Combine preprocessed metadata from all dataset sources and create balanced training and test splits.

## Inputs

- `imgn_preprocessed_metadata.csv`, `coco_preprocessed_metadata.csv`, `open_preprocessed_metadata.csv` — real image metadata  
- `diff_preprocessed_metadata.csv`, `sdxl_preprocessed_metadata.csv`, `midj_preprocessed_metadata.csv` — AI-generated image metadata  

## Outputs

- `combined_metadata.csv` — merged dataset metadata  
- `train_metadata.csv` — training split metadata  
- `test_metadata.csv` — test split metadata  

## Processing Summary

- Load preprocessed metadata from all dataset sources  
- Assign class labels and dataset identifiers  
- Combine metadata into a unified dataset  
- Shuffle and split each dataset into train and test subsets  
- Merge and shuffle final training and test datasets  
- Save split metadata files  

## Notes

- Splits are balanced across dataset sources and class labels  
- A fixed random seed ensures reproducible splits  
- Processing operates on metadata only (no image data)  

## Next Notebook

➡️ [04A Extract Gradient Features](04A_Extract_Gradient_Features.md)
