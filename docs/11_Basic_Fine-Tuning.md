---
title: 11 Basic Fine-Tuning
parent: 5. Basic Fine-Tuning Tutorial
nav_order: 1
---

# 11 Basic Fine-Tuning

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/11_Basic_Fine_Tuning.ipynb" target="_blank" rel="noopener noreferrer">
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

All tuning results are generated within the notebook and may optionally be saved:

* Cross-validation performance summaries
* Best model configuration
* Final test set evaluation metrics:

  * Accuracy
  * Precision
  * Recall
  * F1-score
  * ROC AUC

Optional saved outputs:

* `metadata/results/fine_tuning_results.csv`
* `metadata/results/best_model_config.json`

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

---

## Processing Workflow

This notebook executes a structured sequence of steps:

1. **Environment Setup and Data Loading**  
   The runtime environment is initialized, required libraries are imported, and training and test datasets are loaded.

2. **Data Validation and Preparation**  
   The datasets are verified for:

   * Correct metadata structure  
   * Expected feature dimensionality  
   * Absence of missing values  

   Feature matrices (`X`) and labels (`y`) are prepared.

3. **Feature Normalization**  
   Feature values are normalized to ensure consistent scaling across all dimensions.

4. **Model Configuration Definition**  
   A set of candidate configurations for the Multi-Layer Perceptron (MLP) is defined, including variations in:

   * Hidden layer structure  
   * Regularization strength (alpha)  
   * Learning rate (optional)

5. **Cross-Validation Evaluation (Training Data Only)**  
   Stratified k-fold cross-validation is performed on the training dataset to evaluate each configuration.

6. **Model Selection**  
   The best-performing configuration is selected based on evaluation metrics, with emphasis on ROC AUC and F1-score.

7. **Final Model Training**  
   The selected model is retrained using the full training dataset.

8. **Final Evaluation (Test Set)**  
   The tuned model is evaluated on the independent test dataset to measure generalization performance.

---

## Notes and Design Choices

* **Controlled tuning approach:**  
  Only a small number of hyperparameters are varied to maintain interpretability and avoid overfitting.

* **Training/test separation:**  
  Cross-validation is performed exclusively on training data. The test set is used only once for final evaluation.

* **Model consistency:**  
  The Multi-Layer Perceptron (MLP) remains the primary classifier to maintain consistency with the baseline evaluation.

* **Performance metrics:**  
  ROC AUC is emphasized as the primary metric, with F1-score used as a secondary indicator.

* **Reproducibility:**  
  Fixed random seeds are used to ensure consistent and repeatable results.

---

## Role in the Overall Pipeline

This notebook represents the **model refinement stage** of the pipeline.

It answers the key question:

> Can the performance of the DIP feature-based approach be improved through controlled tuning of the classifier?

The results are compared against the baseline established in the Basic Testing notebook.

---

## Next Step

➡️ [05 Build Feature Vectors](05_Build_Feature_Vectors.md)

