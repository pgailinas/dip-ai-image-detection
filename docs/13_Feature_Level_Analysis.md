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

Evaluate the predictive contribution of individual DIP features and feature groups by comparing single-feature and group-level models against the full feature set.

---

## Inputs

- `train_feature_vectors_normalized.csv`, `test_feature_vectors_normalized.csv` — normalized feature vectors (N samples × 25 features)

---

## Outputs

- Single-feature performance metrics — evaluation results for models trained on individual features  
- Top-feature comparison table — compact comparison against the full-feature model  
- Feature-group comparison table — Gradient-Based, Spatial, and Frequency-Domain performance vs full model  
- Ranked feature-level results — sorted by ROC AUC  
- Saved CSV and JSON outputs for downstream analysis and reporting  

---

## Processing Summary

- Load normalized feature vectors  
- Separate feature columns and class labels  
- Train classifier using the full feature set (baseline)  
- Train classifiers using individual features  
- Rank features based on performance (ROC AUC)  
- Compare top-performing features against the full model  
- Train classifiers using feature groups:
  - Gradient-Based  
  - Spatial  
  - Frequency-Domain  
- Compare feature-group performance against the full model  
- Generate visualization of single-feature performance  
- Save results for reporting and reuse  

---

## Notes

- Single-feature models isolate the contribution of each feature  
- Feature-group models evaluate the contribution of feature domains  
- The full feature model consistently outperforms individual features and feature groups  
- Results demonstrate that combining complementary DIP features improves classification performance  
- The current implementation uses 25 features; `Mid Frequency Energy Ratio` is not included and is planned for future restoration  

---

## Next Notebook

➡️ [14 Source Pair Analysis](14_Source_Pair_Analysis.md)

