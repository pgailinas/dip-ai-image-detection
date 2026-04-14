---
title: 09 Validate Tune Two Models
parent: 4. Basic Testing Tutorial
nav_order: 1
---

# 09 Validate Tune Two Models

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/09_Validate_Tune_Two_Models.ipynb)

---

## Purpose

This notebook evaluates the performance of the two trained classifiers—**RBF SVM** and **MLP**—on the held-out test dataset.

The goal is to assess how well each model generalizes to unseen data using a fully independent test set. Performance is measured using multiple evaluation metrics and summarized through confusion matrices and ROC analysis.

## Inputs

- Normalized feature vector CSV file:
  - `test_feature_vectors_normalized.csv`

- Trained model files:
  - `best_rbf_svm_model.pkl`
  - `best_mlp_model.pkl`

- Project configuration file:
  - `project_config.py`

## Outputs

- Evaluation metrics for both models:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - ROC-AUC

- Confusion matrices

- ROC curves (optional plots)

- Evaluation summary file (if saved)

## Main Tasks

- Load normalized test feature vectors
- Separate features and labels
- Load trained models
- Generate predictions for both models
- Compute evaluation metrics
- Construct confusion matrices
- Compare model performance
- Optionally save evaluation results

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a summary of evaluation objectives, including the use of a held-out test set and comparison of two models.

### Cell 1: Import Libraries and Configuration
Loads required libraries (e.g., scikit-learn, Pandas, NumPy, Matplotlib) and imports shared configuration settings.

### Cell 2: Load Test Dataset
Reads the normalized test feature vector CSV file and prepares feature and label arrays.

### Cell 3: Load Trained Models
Loads the previously saved RBF SVM and MLP models from disk.

### Cell 4: Generate Predictions
Applies both models to the test data to obtain predicted labels and probability scores.

### Cell 5: Compute Evaluation Metrics
Calculates performance metrics for both models, including accuracy, precision, recall, F1-score, and ROC-AUC.

### Cell 6: Generate Confusion Matrices
Constructs confusion matrices to visualize classification performance and error types.

### Cell 7: Plot ROC Curves (Optional)
Generates ROC curves to compare model discrimination capability across thresholds.

### Cell 8: Compare Model Performance
Summarizes and compares evaluation results to identify the best-performing model.

### Cell 9: Save Evaluation Results (Optional)
Writes evaluation metrics and results to file for documentation and reporting.

## Notes and Design Choices

- **Independent test evaluation:**  
  The test dataset is not used during training or tuning, ensuring an unbiased estimate of model performance.

- **Multiple evaluation metrics:**  
  A range of metrics is used to provide a comprehensive assessment of classifier performance.

- **Model comparison:**  
  Both RBF SVM and MLP are evaluated to determine which model generalizes best.

- **Confusion matrix analysis:**  
  Provides insight into classification errors, including false positives and false negatives.

## Files Produced

- Evaluation results (optional CSV or JSON file)
- Confusion matrix outputs (plots or arrays)
- ROC curve plots (if generated)

## Role in the Overall Pipeline

This notebook provides the final evaluation of the trained models using an independent test dataset. It represents the culmination of the pipeline and produces the performance results reported for the project.

## Next Step

➡️ [10 Further Results](10_Further_Results.md)

