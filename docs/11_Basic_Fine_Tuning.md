---
title: 09 Validate and Tune Two Models
parent: 3. Model Optimization Tutorial
nav_order: 3
---

# 09 Validate and Tune Two Models

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/09_Validate_and_Tune_Two_Models.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook performs **validation and comparison** of the two selected
classifiers using the normalized Digital Image Processing (DIP) feature vectors.

The focus is on evaluating the retained models:

* RBF Support Vector Machine (RBF SVM)
* Multi-Layer Perceptron (MLP)

Both classifiers are evaluated using a consistent stratified cross-validation
framework to compare their performance prior to final independent testing.

---

## Inputs

* Normalized training feature vectors:

  * `metadata/vectors/train_feature_vectors_normalized.csv`

* Project configuration file:

  * `project_config.py`

Classifier configurations are defined within this notebook based on
results from Notebook 07 and the finalized model design.

---

## Outputs

All validation results are saved to `metadata/results/`:

* `cross_validation_results.csv`
  Full cross-validation performance summary.

* `classifier_comparison_tuned.csv`
  Condensed comparison of key performance metrics.

---

## Main Tasks

* Load normalized training feature vectors
* Validate dataset integrity
* Separate features and labels
* Define selected classifier configurations
* Perform stratified k-fold cross-validation
* Evaluate models using multiple performance metrics
* Compare validation performance
* Save validation outputs

---

## Processing Workflow

This notebook executes a structured sequence of steps to validate and compare the selected classifiers:

1. **Environment Setup and Data Loading**
   The runtime environment is initialized, required libraries are imported, and the normalized training dataset is loaded.

2. **Data Validation and Preparation**
   The dataset is verified for:

   * Correct metadata structure
   * Expected feature dimensionality
   * Absence of missing values
     Feature matrices and labels are prepared for evaluation.

3. **Classifier Configuration Definition**
   The two selected classifiers are defined using their tuned hyperparameters established in prior steps.

4. **Cross-Validation Evaluation**
   Both classifiers are evaluated using stratified k-fold cross-validation, producing performance metrics across multiple evaluation criteria.

5. **Performance Aggregation and Comparison**
   Results are compiled and compared, with emphasis on ROC-AUC and overall consistency across folds.

6. **Output Generation and Validation**
   Validation results are saved to disk, and checks are performed to confirm output integrity and consistency.

---

## Notes and Design Choices

* **Two-model validation approach:**
  Both RBF SVM and MLP are evaluated to preserve a fair comparison prior to final testing.

* **In-notebook configuration:**
  Classifier parameters are defined directly in this notebook based on prior selection results.

* **Cross-validation framework:**
  Stratified k-fold cross-validation ensures consistent and unbiased evaluation.

* **Separation of concerns:**
  This notebook evaluates model behavior using training data only.
  Final evaluation on unseen test data is performed in a later notebook.

---

## Role in the Overall Pipeline

This notebook represents the **validation and tuning stage** of the pipeline.

It evaluates the selected classifiers using consistent procedures and
produces performance summaries that inform interpretation of final test results.

---

## Next Step

➡️ [10 Evaluate Two Models](10_Evaluate_Two_Models.md)

