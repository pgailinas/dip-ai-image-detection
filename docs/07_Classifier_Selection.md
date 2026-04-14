---
title: 07 Compare Candidate Classifiers
parent: 3. Model Optimization Tutorial
nav_order: 1
---

# 07 Classifier Selection

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/07_Classifier_Selection.ipynb)

---

## Purpose

This notebook evaluates a range of candidate classifiers using the normalized DIP feature vectors and selects the best-performing models based on cross-validation performance.

The goal is to identify which classifier types are most effective at distinguishing real images from AI-generated images prior to detailed tuning and final training.

## Inputs

- Normalized feature vector CSV files:
  - `train_feature_vectors_normalized.csv`
  - `test_feature_vectors_normalized.csv`

- Project configuration file:
  - `project_config.py`

## Outputs

- Baseline classifier comparison results:
  - `baseline_model_results.csv`

This CSV contains performance metrics for each classifier:
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

## Main Tasks

- Load normalized feature vectors
- Separate features and labels
- Define candidate classifiers
- Perform cross-validation
- Evaluate models using multiple metrics
- Rank classifiers based on performance
- Save comparison results

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a summary of classifier selection objectives, including evaluation approach and expected outputs.

### Cell 1: Import Libraries and Configuration
Loads required libraries (e.g., scikit-learn, Pandas, NumPy) and imports shared configuration settings.

### Cell 2: Load Normalized Feature Vectors
Reads the normalized training dataset and prepares feature and label arrays.

### Cell 3: Prepare Training Data
Separates input features (`X_train`) and target labels (`y_train`) for use in model evaluation.

### Cell 4: Define Candidate Classifiers
Specifies a set of candidate classifiers (e.g., MLP, RBF SVM, Random Forest, Logistic Regression) to be evaluated.

### Cell 5: Perform Cross-Validation
Applies stratified k-fold cross-validation to each classifier to ensure robust performance estimation.

### Cell 6: Compute Evaluation Metrics
Calculates performance metrics for each classifier, including accuracy, precision, recall, F1-score, and ROC-AUC.

### Cell 7: Rank Classifier Performance
Aggregates and ranks classifier results based on cross-validation metrics, typically prioritizing ROC-AUC.

### Cell 8: Save Baseline Results
Writes the classifier comparison results to a CSV file for reference and further analysis.

## Notes and Design Choices

- **Cross-validation approach:**  
  Stratified k-fold cross-validation is used to ensure stable and reliable performance estimates.

- **Multiple evaluation metrics:**  
  Performance is assessed using a range of metrics to provide a comprehensive view of classifier behavior.

- **ROC-AUC prioritization:**  
  ROC-AUC is emphasized as a primary metric due to its robustness in binary classification tasks.

- **Model diversity:**  
  A variety of classifier types are evaluated to explore different modeling approaches.

## Files Produced

- `baseline_model_results.csv` — Cross-validation performance summary for all candidate classifiers

## Role in the Overall Pipeline

This notebook identifies the most promising classifier types for the DIP feature representation. The selected models are then further tuned and trained in the next stage.

## Next Step

➡️ [08 Train Two Classifiers](08_Train_Two_Classifiers.md)
