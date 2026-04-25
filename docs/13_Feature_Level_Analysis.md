---
title: 13 Feature-Level Analysis
parent: 6. Full Training Tutorial
nav_order: 2
---

# 13 Feature-Level Analysis

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/13_Feature_Level_Analysis.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

Evaluate the predictive contribution of individual DIP features by comparing single-feature models to the full feature set.

## Inputs

- `train_feature_vectors_normalized.csv`, `test_feature_vectors_normalized.csv` — normalized feature vectors (N samples × 25 features)

## Outputs

- Single-feature performance metrics — evaluation results for models trained on individual features  
- Feature comparison summaries — performance comparison against the full feature model  

## Processing Summary

- Load normalized feature vectors  
- Separate feature columns and class labels  
- Train classifiers using individual features  
- Evaluate model performance for each feature  
- Compare results against full feature model  
- Summarize feature contributions  

## Notes

- Single-feature models isolate the contribution of each feature  
- Performance is compared against the full feature set for context  
- Results provide insight into feature importance and model behavior  

## Next Notebook

➡️ [14 Source Pair Analysis](14_Source_Pair_Analysis.md)

