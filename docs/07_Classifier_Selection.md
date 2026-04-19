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

This notebook evaluates a range of candidate classifiers using the normalized DIP feature vectors and identifies the **top-performing models** based on cross-validation performance.

Rather than selecting a single classifier, this notebook selects the **top two classifiers** and carries them forward for further training and final independent evaluation.

---

## Inputs

* Normalized feature vector CSV file:

  * `train_feature_vectors_normalized.csv`

* Project configuration file:

  * `project_config.py`

---

## Outputs

The following evaluation results and model configurations are generated:

* `classifier_comparison_baseline.csv`
  Cross-validation results for all candidate classifiers.

* `classifier_comparison_tuned.csv`
  Performance results after controlled hyperparameter tuning.

* `best_classifier_config.json`
  Configuration details for the selected top two classifiers.

---

## Main Tasks

* Load normalized feature vectors
* Validate dataset integrity
* Separate features and labels
* Define candidate classifiers
* Perform cross-validation
* Evaluate models using multiple metrics
* Rank classifiers based on performance
* Apply controlled hyperparameter tuning
* Select and save the **top two classifiers**

---

## Processing Workflow

This notebook executes a structured sequence of steps to identify the strongest classifier candidates:

1. **Environment Setup and Data Loading**
   Required libraries are imported, and the normalized training dataset is loaded for analysis.

2. **Data Validation and Preparation**
   The dataset is verified for:

   * Missing values
   * Class balance
   * Correct feature dimensionality
     Feature matrices and target labels are separated and prepared for model input.

3. **Candidate Model Definition**
   A set of diverse classifier types is defined, along with a stratified k-fold cross-validation strategy and evaluation metrics.

4. **Baseline Model Evaluation**
   Each classifier is evaluated using cross-validation, producing performance metrics including accuracy, precision, recall, F1-score, and ROC-AUC.

5. **Performance Aggregation and Ranking**
   Results are compiled and ranked, with ROC-AUC serving as the primary selection criterion.

6. **Controlled Hyperparameter Tuning**
   Top-performing classifiers are further refined using targeted, small-grid hyperparameter tuning to improve performance.

7. **Model Selection and Output Generation**
   The top two classifiers are selected based on tuned performance, and all results and configurations are saved for downstream use.

---

## Notes and Design Choices

* **Cross-validation approach:**
  Stratified k-fold cross-validation ensures stable and reliable performance estimates.

* **Multiple evaluation metrics:**
  Models are evaluated using accuracy, precision, recall, F1-score, and ROC-AUC.

* **ROC-AUC prioritization:**
  ROC-AUC is used as the primary ranking metric due to its robustness in binary classification.

* **Controlled tuning:**
  Hyperparameter tuning uses small, targeted grids rather than exhaustive search.

* **Multi-model selection:**
  The top two classifiers are selected to:

  * reduce sensitivity to small performance differences
  * enable comparison across model types
  * improve experimental robustness

---

## Role in the Overall Pipeline

This notebook identifies the strongest classifier candidates for the DIP feature representation and prepares them for final training.

The selected classifiers are trained and evaluated in subsequent notebooks.

---

## Next Step

➡️ [08 Train Two Classifiers](08_Train_Two_Classifiers.md)


