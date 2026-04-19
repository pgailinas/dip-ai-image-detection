---
title: 13 Feature-Level Analysis
parent: 6. Full Training Tutorial
nav_order: 2
---

# 13 Feature-Level Analysis

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/11A_Feature_Level_Analysis.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook evaluates the predictive power of individual DIP features by training classifiers using one feature at a time and comparing performance against the full feature set.

The goal is to understand the relative importance and discriminative capability of each feature.

---

## Inputs

* Normalized feature vector CSV files:

  * `train_feature_vectors_normalized.csv`
  * `test_feature_vectors_normalized.csv`

* Project configuration file:

  * `project_config.py`

---

## Outputs

The following analysis results are generated:

* Single-feature model performance metrics:

  * Accuracy
  * Precision
  * Recall
  * F1-score
  * ROC-AUC

* Comparative performance tables against full feature model

---

## Main Tasks

* Load normalized feature vectors
* Isolate individual features
* Train classifiers using single features
* Evaluate model performance
* Compare against full feature model
* Analyze feature importance

---

## Processing Workflow

1. **Data Loading and Preparation**
   Load normalized datasets and separate features and labels.

2. **Single-Feature Model Training**
   Train classifiers using one feature at a time.

3. **Performance Evaluation**
   Compute standard classification metrics for each feature.

4. **Comparison with Full Feature Model**
   Compare individual feature performance against the full feature set.

5. **Analysis and Interpretation**
   Identify features with strong predictive capability and assess their contribution.

---

## Notes and Design Choices

* **Feature-level analysis:**
  Evaluating individual features provides insight into their relative importance.

* **Comparison to full model:**
  Demonstrates the benefit of combining multiple complementary features.

* **Interpretability:**
  Results help explain the effectiveness of the DIP feature design.

---

## Role in the Overall Pipeline

This notebook provides insight into feature importance and supports interpretation of model behavior.

---

## Next Step

➡️ [14 Source-Pair Analysis](14_Source_Pair_Analysis.md)


