---
title: 14 Source-Pair Analysis
parent: 6. Full Training Tutorial
nav_order: 3
---

# 14 Source-Pair Analysis

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/14_Source_Pair_Analysis.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

Evaluate model generalization across dataset combinations by comparing performance on different real and AI source pairings.

## Inputs

- `train_feature_vectors_normalized.csv`, `test_feature_vectors_normalized.csv` — normalized feature vectors (N samples × 25 features)

## Outputs

- Source-pair performance metrics — evaluation results for each dataset combination  
- Comparative analysis summaries — performance comparison across all experiments  

## Processing Summary

- Define source pair combinations  
- Construct balanced datasets for each experiment  
- Train classifiers for each source pairing  
- Evaluate model performance  
- Aggregate and compare results  
- Analyze generalization behavior  

## Notes

- Experiments evaluate sensitivity to dataset selection  
- Each source pair maintains balanced class representation  
- Results provide insight into model robustness and generalization  

## Next Notebook

➡️ **Thanks For Trying This Tutorial**

