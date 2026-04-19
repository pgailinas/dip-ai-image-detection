---
title: 11 Further Results
parent: 6. Full Training Tutorial
nav_order: 2
---

# 11 Further Results

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/11_Further_Results.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook explores additional experiments and analyses beyond the core pipeline to better understand the behavior and effectiveness of the DIP feature-based classification approach.

These experiments investigate the contribution of individual features, compare simplified models to the full feature set, and provide further insight into model performance and generalization.

---

## Inputs

* Normalized feature vector CSV files:

  * `train_feature_vectors_normalized.csv`
  * `test_feature_vectors_normalized.csv`

* Trained model configurations (optional reuse)

* Project configuration file:

  * `project_config.py`

---

## Outputs

The following exploratory analysis results are generated:

* Single-feature model evaluation metrics:

  * Accuracy
  * Precision
  * Recall
  * F1-score
  * ROC-AUC

* Comparative performance tables

* Optional plots and summary visualizations

---

## Main Tasks

* Evaluate models using individual DIP features
* Compare single-feature performance against full feature set
* Analyze feature importance and discriminative power
* Explore model behavior across different datasets
* Summarize insights and observations

---

## Processing Workflow

This notebook executes a structured sequence of exploratory analysis steps:

1. **Environment Setup and Data Loading**
   The runtime environment is initialized, required libraries are imported, and normalized training and test datasets are loaded.

2. **Data Preparation**
   Feature matrices and labels are separated to enable both full-model and feature-level evaluations.

3. **Single-Feature Model Training**
   Models are trained using one feature at a time to isolate the predictive contribution of individual DIP features.

4. **Performance Evaluation**
   Each single-feature model is evaluated using standard metrics, including accuracy, precision, recall, F1-score, and ROC-AUC.

5. **Comparison with Full Feature Model**
   Single-feature performance is compared against the full feature set to assess the benefit of combining multiple features.

6. **Analysis and Interpretation**
   Results are analyzed to identify the most informative features and to understand trends in model behavior.

7. **Result Summarization**
   Key findings are summarized, highlighting insights into feature importance and overall model effectiveness.

---

## Notes and Design Choices

* **Feature-level analysis:**
  Evaluating individual features provides insight into their relative importance.

* **Comparison to full model:**
  Demonstrates the benefit of combining multiple complementary features.

* **Exploratory focus:**
  This notebook is intended for analysis and insight rather than pipeline execution.

* **Interpretability:**
  Results help explain why the DIP feature-based approach is effective.

---

## Role in the Overall Pipeline

This notebook extends the core pipeline by providing deeper analysis and validation of the feature design. It supports the overall conclusions of the project and strengthens the justification for the chosen methodology.

---

## Next Step

➡️ [Thanks For Trying This Tutorial](Thanks_For_Trying_This_Tutorial.md)

