---
title: 07 Compare Candidate Classifiers
parent: 3. Model Optimization Tutorial
nav_order: 1
---

# 07 Classifier Selection

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/07_Classifier_Selection.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

Evaluate candidate classifiers using normalized DIP feature vectors and select the top two classifiers for continued training and evaluation.

## Inputs

- `train_feature_vectors_normalized.csv` — normalized training feature vectors (N samples × 25 features)

## Outputs

- `classifier_comparison_baseline.csv` — baseline cross-validation results for candidate classifiers
- `classifier_comparison_tuned.csv` — tuned cross-validation results for selected classifiers
- `best_model_config.json` — configuration details for the selected top classifiers

## Processing Summary

- Load normalized training feature vectors
- Separate feature columns and class labels
- Define candidate classifiers and evaluation metrics
- Evaluate classifiers using stratified cross-validation
- Apply controlled hyperparameter tuning
- Save comparison results and selected model configuration

## Notes

- The held-out test dataset is not used in this notebook
- ROC-AUC is used as the primary classifier ranking metric
- The top two classifiers are carried forward for additional training and evaluation
- A notebook-level `VERBOSE` flag controls optional diagnostic output

## Next Notebook

➡️ [08 Train Two Classifiers](08_Train_Two_Classifiers.md)
