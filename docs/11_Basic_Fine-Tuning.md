---
title: 11 Basic Fine-Tuning
parent: 5. Basic Fine-Tuning Tutorial
nav_order: 1
---

# 11 Basic Fine-Tuning

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/11_Basic_Fine-Tuning.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook performs **controlled hyperparameter tuning** of the baseline classifier to improve performance while preserving the original Digital Image Processing (DIP) feature-based approach.

The goal is to demonstrate that performance gains can be achieved through modest model refinement without altering the feature engineering methodology.

---

## Inputs

* Training feature vectors:

  * `metadata/vectors/train_feature_vectors.csv`

* Test feature vectors:

  * `metadata/vectors/test_feature_vectors.csv`

* Project configuration file:

  * `src/project_config.py`

---

## Outputs

All tuning results are generated within the notebook and saved using **config-controlled paths**:

* Cross-validation performance summaries  
* Best model configuration  
* Final test set evaluation metrics:

  * Accuracy  
  * Precision  
  * Recall  
  * F1-score  
  * ROC AUC  

* Confusion matrix  
* ROC curve  

Saved output files:

* `metadata/results/fine_tuning_results.csv`  
* `metadata/results/best_model_config.json`  
* `metadata/results/tuned_model_results.csv`  
* `metadata/models/scaler.pkl`  

> Note: Outputs are written to local runtime storage and are not persisted unless explicitly saved.

---

## Main Tasks

* Load training and test feature vectors  
* Validate dataset structure and integrity  
* Separate features and labels  
* Normalize feature values  
* Define candidate model configurations  
* Perform stratified k-fold cross-validation on training data  
* Select the best-performing configuration  
* Retrain the model on full training data  
* Evaluate the tuned model on the test set  
* Compare tuned results with baseline performance  

---

## Processing Workflow

This notebook executes a structured sequence of steps:

### 1. Environment Setup and Data Loading  
The runtime environment is initialized, the repository is loaded, and datasets are accessed using paths defined in `project_config.py`.

### 2. Data Validation and Preparation  
The datasets are verified for:

* Correct metadata structure  
* Expected feature dimensionality (**25 features**)  
* Valid class labels and subset separation  
* Absence of missing values  

Feature matrices (`X`) and labels (`y`) are prepared.

### 3. Feature Normalization  
Feature values are normalized:

* Fit on training data only  
* Applied to both training and test sets  
* Saved for reuse in later notebooks  

### 4. Model Configuration Definition  
A small set of candidate MLP configurations is defined, including variations in:

* Hidden layer structure  
* Regularization strength (`alpha`)  

### 5. Cross-Validation Evaluation (Training Data Only)  
Stratified k-fold cross-validation is performed on the training dataset:

* Accuracy  
* Precision  
* Recall  
* F1-score  
* ROC AUC  

Model selection is based primarily on **ROC AUC**, with **F1-score** as a secondary metric.

### 6. Model Selection  
The best-performing configuration is selected based on cross-validation results and saved for reproducibility.

### 7. Final Model Training  
The selected model is retrained using the full normalized training dataset.  
Training time and convergence behavior are recorded.

### 8. Final Evaluation (Test Set)  
The tuned model is evaluated on the independent test dataset to measure generalization performance.

### 9. Results Display  
Cross-validation summaries and final test metrics are presented.  
Visualizations (confusion matrix and ROC curve) are optionally displayed based on the `VERBOSE` flag.

### 10. Output Generation  
Cross-validation results, best configuration, and final evaluation metrics are saved using config-defined paths.

### 11. Baseline Comparison  
The tuned model performance is compared directly against baseline results from Notebook 10, if available.

---

## Notes and Design Choices

* **Controlled tuning approach:**  
  Only a small number of hyperparameters are varied to maintain interpretability and reduce overfitting risk.

* **Training/test separation:**  
  Cross-validation is performed exclusively on training data. The test set is used only once for final evaluation.

* **Model consistency:**  
  The Multi-Layer Perceptron (MLP) remains the primary classifier to maintain consistency with the baseline evaluation.

* **Performance metrics:**  
  ROC AUC is emphasized as the primary metric, with F1-score used as a secondary indicator.

* **Configuration-driven design:**  
  All file paths, dataset sizes, and constants are controlled via `project_config.py`.

* **VERBOSE control:**  
  Optional outputs (tables, detailed logs, visualizations) are controlled using the `VERBOSE` flag.

* **Model complexity:**  
  The best-performing configuration may be a relatively simple model, indicating that the engineered DIP features form a well-structured feature space.

* **Convergence behavior:**  
  The selected tuned model may still reach the iteration limit; this does not invalidate evaluation.

* **Reproducibility:**  
  Fixed random seeds ensure consistent and repeatable results.

---

## Role in the Overall Pipeline

This notebook represents the **model refinement stage** of the pipeline.

It answers the key question:

> Can the performance of the DIP feature-based approach be improved through controlled tuning of the classifier?

The results are compared directly against the baseline established in the Basic Testing notebook.

---

## Next Step

➡️ [12 Evaluate Two Models](12_Evaluate_Two_Models.md)

