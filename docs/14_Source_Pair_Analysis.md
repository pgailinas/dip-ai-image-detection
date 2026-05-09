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

Evaluate model generalization across dataset combinations by comparing performance on real vs AI source pairings. This analysis provides insight into how well DIP-based features generalize across different image sources and generative models.

---

## Inputs

- `train_feature_vectors_normalized.csv`, `test_feature_vectors_normalized.csv` — normalized feature vectors (N samples × 26 features)

---

## Outputs

- Source-pair performance metrics (Accuracy, Precision, Recall, F1, ROC AUC)  
- ROC curve data (FPR, TPR, thresholds) for each source-pair model  
- Comparative results table sorted by ROC AUC  
- ROC curve comparison plot across all source-pair experiments  
- Saved outputs:
  - `source_pair_results.csv`
  - `source_pair_roc_curves.png`

---

## Processing Summary

- Load normalized feature vectors and validate dataset structure  
- Define source-pair experiments across all dataset permutations (3 real × 3 AI = 9 combinations)  
- Construct balanced datasets for each source pair  
- Train a classifier using the fixed tuned MLP configuration for each pairing  
- Evaluate model performance using standard metrics and ROC curves  
- Aggregate and sort results by ROC AUC  
- Visualize ROC curves to compare classification behavior across thresholds  
- Save results and plots for downstream use  

---

## Notes

- Experiments evaluate sensitivity to dataset selection and source variability  
- Each source pair maintains strict class balance (real vs AI)  
- The same tuned model configuration is used for all experiments to isolate dataset effects  
- Results highlight which source combinations are easier or harder to distinguish  
- ROC curves provide deeper insight into classification performance beyond single-value metrics  

---

## Next Notebook

➡️ [Results & Insights](7._Results_&_Insights.md)

