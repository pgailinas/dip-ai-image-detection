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

Evaluate model generalization across dataset combinations by comparing performance on real vs AI source pairings and a combined real-vs-AI experiment. This analysis provides insight into how well DIP-based features generalize across different image sources and generative models.

---

## Inputs

- `train_feature_vectors_normalized.csv`, `test_feature_vectors_normalized.csv` — normalized feature vectors (N samples × 26 features)

---

## Outputs

- Source-pair and combined-model performance metrics:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
  - ROC AUC
- ROC curve data (FPR, TPR, thresholds) for all evaluated models
- Comparative results table sorted by ROC AUC
- ROC curve comparison plot across all experiments
- Saved outputs:
  - `source_pair_results.csv`
  - `source_pair_roc_curves.png`

---

## Processing Summary

- Load normalized feature vectors and validate dataset structure
- Define source-pair experiments across all configured real and AI dataset combinations
- Construct balanced datasets for each source-pair experiment
- Train one classifier per source pair using the fixed tuned MLP configuration
- Construct and train a combined real-vs-AI classifier using all configured sources
- Evaluate all trained models using standard classification metrics and ROC analysis
- Aggregate and sort results by ROC AUC
- Visualize ROC curves to compare classification behavior across thresholds
- Save results and plots for downstream use

---

## Notes

- Experiments evaluate sensitivity to dataset selection and source variability
- Each source pair maintains strict class balance (real vs AI)
- The same tuned model configuration is used for all experiments to isolate dataset effects
- The combined model provides a broader measure of overall generalization capability
- Results highlight which source combinations are easier or harder to distinguish
- ROC curves provide deeper insight into classification performance beyond single-value metrics

---

## Next Notebook

➡️ [Results & Insights](7.%20Results%20&%20Insights.html)

