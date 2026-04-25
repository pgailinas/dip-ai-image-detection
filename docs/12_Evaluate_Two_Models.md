---
title: 12 Evaluate Two Models
parent: 6. Full Training Tutorial
nav_order: 1
---

# 12 Evaluate Two Models

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/12_Evaluate_Two_Models.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook performs the **final independent evaluation** of the trained
classifiers using the normalized Digital Image Processing (DIP) feature vectors.

The following models are evaluated:

* RBF Support Vector Machine (RBF SVM)
* Multi-Layer Perceptron (MLP)

Both models are applied to the **held-out test dataset**, ensuring an unbiased
assessment of model performance.

---

## Inputs

* Normalized test feature vectors:

  * `metadata/vectors/test_feature_vectors_normalized.csv`

* Trained model files:

  * `metadata/models/final_rbf_svm_model.pkl`
  * `metadata/models/final_mlp_model.pkl`

* Project configuration file:

  * `project_config.py`

---

## Outputs

All evaluation outputs are saved to `metadata/results/`:

* `final_test_results.csv`
  Complete evaluation metrics for both models.

* `final_test_results.json`
  Structured representation of evaluation metrics.

* `final_confusion_matrix_mlp.csv`

* `final_confusion_matrix_rbf_svm.csv`

* `final_roc_points_mlp.csv`

* `final_roc_points_rbf_svm.csv`

* `final_comparison_summary.csv`
  Side-by-side comparison of model performance.

---

## Main Tasks

* Load normalized test dataset
* Validate dataset integrity
* Prepare feature matrix and label vector
* Load trained models
* Generate predictions and class probabilities
* Compute evaluation metrics (Accuracy, Precision, Recall, F1-score, ROC-AUC)
* Generate confusion matrices
* Compute ROC curves
* Compare model performance
* Save evaluation outputs

---

## Processing Workflow

This notebook executes a structured sequence of steps to evaluate trained models on unseen data:

1. **Environment Setup and Data Loading**
   The runtime environment is initialized, required libraries are imported, and the normalized test dataset is loaded.

2. **Data Validation and Preparation**
   The test dataset is verified for:

   * Correct structure and feature dimensionality
   * Absence of missing values
     Feature matrices and labels are prepared for evaluation.

3. **Model Loading**
   Trained classifier models are loaded from stored `.pkl` files.

4. **Prediction Generation**
   Each model produces predicted class labels and class probabilities for the test dataset.

5. **Metric Computation**
   Evaluation metrics are computed, including accuracy, precision, recall, F1-score, and ROC-AUC.

6. **Diagnostic Analysis**
   Additional evaluation artifacts are generated:

   * Confusion matrices
   * ROC curve data

7. **Model Comparison**
   Results are aggregated into comparison tables to enable direct performance assessment between classifiers.

8. **Output Generation and Validation**
   All evaluation artifacts are saved, and validation checks confirm output completeness and consistency.

---

## Notes and Design Choices

* **Independent test evaluation:**
  The test dataset is never used during training or validation.

* **Positive class definition:**
  The AI-generated class is treated as the positive class for all metrics.

* **Two-model comparison:**
  Both MLP and RBF SVM are evaluated to provide a robust comparison.

* **Consistent feature pipeline:**
  The same 25 normalized DIP features are used across all stages.

---

## Role in the Overall Pipeline

This notebook represents the **final evaluation stage** of the pipeline.

It measures real-world model performance on unseen data and produces the
results used for reporting, analysis, and conclusions.

---

## Next Step

➡️ [13 Feature Level Analysis](13_Feature_Level_Analysis.md)

