---
title: 10 Evaluate Two Models
parent: 3. Model Optimization Tutorial
nav_order: 4
---

# 10 Evaluate Two Models

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/10_Evaluate_Two_Models.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook performs the **final independent evaluation** of the trained  
classifiers using the normalized Digital Image Processing (DIP) feature vectors.

The following models are evaluated:

- RBF Support Vector Machine (RBF SVM)  
- Multi-Layer Perceptron (MLP)  

Both models are applied to the **held-out test dataset**, ensuring an unbiased  
assessment of model performance.

---

## Inputs

- Normalized test feature vectors:
  - `metadata/vectors/test_feature_vectors_normalized.csv`

- Trained model files:
  - `metadata/models/final_rbf_svm_model.pkl`
  - `metadata/models/final_mlp_model.pkl`

- Project configuration file:
  - `project_config.py`

---

## Outputs

All outputs are saved to `metadata/results/`:

- `final_test_results.csv` — Full evaluation metrics  
- `final_test_results.json` — Metrics in structured format  
- `final_confusion_matrix_mlp.csv` — MLP confusion matrix  
- `final_confusion_matrix_rbf_svm.csv` — RBF SVM confusion matrix  
- `final_roc_points_mlp.csv` — MLP ROC curve data  
- `final_roc_points_rbf_svm.csv` — RBF SVM ROC curve data  
- `final_comparison_summary.csv` — Side-by-side model comparison  

---

## Main Tasks

- Load normalized test dataset  
- Validate dataset integrity  
- Prepare feature matrix and label vector  
- Load trained models  
- Generate predictions and class probabilities  
- Compute evaluation metrics (Accuracy, Precision, Recall, F1-score, ROC-AUC)  
- Generate confusion matrices  
- Compute ROC curves  
- Compare model performance  
- Save evaluation outputs  

---

## Cell-by-Cell Description

### Cell 0: Notebook Summary
Provides an overview of evaluation objectives and workflow.

### Startup Cell
Initializes environment, sets project paths, and verifies required input files.

### Cell 1: Import Required Libraries
Loads required libraries including NumPy, pandas, and scikit-learn.

### Cell 2: Load Test Data
Reads the normalized test dataset and displays structure information.

### Cell 3: Validate Test Data
Performs sanity checks and prepares `X_test` and `y_test`.

### Cell 4: Load Trained Models
Loads `.pkl` model files from `metadata/models/`.

### Cell 5: Generate Predictions
Computes predicted labels and class probabilities.

### Cell 6: Compute Evaluation Metrics
Calculates accuracy, precision, recall, F1-score, and ROC-AUC.

### Cell 7: Confusion Matrices
Generates and visualizes confusion matrices (counts and normalized).

### Cell 8: ROC Curves
Computes and plots ROC curves for both models.

### Cell 9: Final Comparison Summary
Builds summary tables for direct model comparison.

### Cell 10: Save Outputs
Saves all evaluation artifacts to `metadata/results/`.

---

## Notes and Design Choices

- **Independent test evaluation:**  
  The test dataset is never used during training or validation.

- **Positive class definition:**  
  The AI-generated class is treated as the positive class for all metrics.

- **Two-model comparison:**  
  Both MLP and RBF SVM are evaluated to provide a robust comparison.

- **Consistent feature pipeline:**  
  The same 25 normalized DIP features are used across all stages.

---

## Files Produced

### `metadata/results/`

- `final_test_results.csv`  
- `final_test_results.json`  
- `final_confusion_matrix_mlp.csv`  
- `final_confusion_matrix_rbf_svm.csv`  
- `final_roc_points_mlp.csv`  
- `final_roc_points_rbf_svm.csv`  
- `final_comparison_summary.csv`  

---

## Role in the Overall Pipeline

This notebook represents the **final evaluation stage** of the pipeline.

It measures real-world model performance on unseen data and produces the  
results used for reporting, analysis, and conclusions.

---

## Next Step

➡️ `11_Further_Results.md`



