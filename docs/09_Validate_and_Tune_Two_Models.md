---
title: 09 Validate and Compare Models
parent: 4. Basic Testing Tutorial
nav_order: 1
---

# 09 Validate and Compare Models

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/09_Validate_and_Compare_Models.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook performs the **final independent evaluation** of the trained classifiers—**RBF SVM** and **MLP**—on the held-out test dataset.

The goal is to assess how well each model generalizes to unseen data using a fully independent test set. Performance is measured using multiple evaluation metrics and visualized through confusion matrices and ROC curves.

---

## Inputs

- Normalized feature vector CSV file:
  - `test_feature_vectors_normalized.csv`

- Trained model files (from Notebook 08):
  - `model_rbf_svm.pkl`
  - `model_mlp.pkl`

- Supporting model artifacts:
  - `trained_model_configs.json`
  - `cross_validation_results.csv`

- Project configuration file:
  - `project_config.py`

---

## Outputs

- Final evaluation metrics for both models:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - ROC-AUC

- Confusion matrices (raw and normalized)

- ROC curve comparison

- Saved evaluation outputs (in `metadata/models/`):

  - `final_test_results.csv`
  - `final_test_results.json`
  - `confusion_matrix_mlp.csv`
  - `confusion_matrix_rbf_svm.csv`
  - `roc_points_mlp.csv`
  - `roc_points_rbf_svm.csv`

---

## Main Tasks

- Load normalized test feature vectors
- Validate dataset integrity
- Separate features and labels
- Load trained classifier models
- Generate predictions and probability scores
- Compute evaluation metrics
- Construct confusion matrices (side-by-side comparison)
- Generate ROC curves
- Summarize model performance
- Save evaluation results for reporting

---

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a summary of evaluation objectives and workflow.

### Cell 1: Import Required Libraries
Loads required libraries (NumPy, pandas, scikit-learn, matplotlib, seaborn).

### Cell 2: Load Test Data and Model Artifacts
Loads normalized test dataset, trained models, and supporting metadata files.

### Cell 3: Validate Test Data
Performs sanity checks:
- metadata column verification
- feature count validation (25 features)
- missing value checks
- label consistency
- test subset validation

### Cell 4: Generate Predictions
Applies both models to the test dataset to generate:
- predicted class labels
- class probabilities for ROC analysis

### Cell 5: Compute Evaluation Metrics
Calculates final test-set metrics:
- accuracy
- precision
- recall
- F1-score
- ROC-AUC

### Cell 6: Confusion Matrix Analysis
Generates and displays:
- confusion matrices (counts)
- normalized confusion matrices
- side-by-side visual comparison

### Cell 7: ROC Curve Analysis
Generates ROC curves for both models and compares their performance.

### Cell 8: Results Summary
Creates summary tables:
- model comparison table (sorted by ROC-AUC)
- transposed metrics table (report-friendly format)

### Cell 9: Save Evaluation Outputs
Saves:
- final evaluation metrics
- confusion matrices
- ROC curve points
- summary tables for reporting

---

## Notes and Design Choices

- **Independent test evaluation:**  
  The test dataset is never used during training or model selection, ensuring an unbiased estimate of performance.

- **Two-model comparison:**  
  Both RBF SVM and MLP are evaluated to provide a meaningful comparison between model types.

- **Consistent evaluation framework:**  
  Both models are evaluated using identical data and metrics.

- **Side-by-side visualization:**  
  Confusion matrices are displayed side-by-side for direct comparison of classification behavior.

- **Reproducibility:**  
  All outputs are saved for documentation and future analysis.

---

## Files Produced

All outputs are saved under:
    metadata/models


Files include:

- `final_test_results.csv` — final performance summary  
- `final_test_results.json` — metrics in structured format  
- `confusion_matrix_mlp.csv` — MLP confusion matrix  
- `confusion_matrix_rbf_svm.csv` — RBF SVM confusion matrix  
- `roc_points_mlp.csv` — ROC curve points (MLP)  
- `roc_points_rbf_svm.csv` — ROC curve points (RBF SVM)  

---

## Role in the Overall Pipeline

This notebook represents the **final evaluation stage** of the pipeline.

It uses the trained models from Notebook 08 and evaluates them on an independent test dataset to produce the final performance results reported in the project.

---

## Next Step

➡️ [10 Further Results](10_Further_Results.md)



