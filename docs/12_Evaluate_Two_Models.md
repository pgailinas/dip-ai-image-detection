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

This notebook performs the **final independent evaluation** of the trained classifiers using the normalized **25-dimensional Digital Image Processing (DIP) feature vectors**.

The following models are evaluated:

* RBF Support Vector Machine (RBF SVM)
* Multi-Layer Perceptron (MLP)

Both models are applied to the **held-out test dataset**, ensuring an unbiased assessment of model performance.

---

## Inputs

* Normalized test feature vectors:

  * `metadata/vectors/test_feature_vectors_normalized.csv`

* Trained model files:

  * `metadata/models/final_rbf_svm_model.pkl`
  * `metadata/models/final_mlp_model.pkl`

* Project configuration file:

  * `src/project_config.py`

---

## Outputs

All evaluation outputs are saved using **config-controlled paths** under `metadata/results/`:

* `final_test_results.csv`  
  Complete evaluation metrics for both models

* `final_test_results.json`  
  Structured representation of evaluation metrics

* `final_confusion_matrix_mlp.csv`  
* `final_confusion_matrix_rbf_svm.csv`

* `final_roc_points_mlp.csv`  
* `final_roc_points_rbf_svm.csv`

* `final_comparison_summary.csv`  
  Side-by-side comparison of model performance

---

## Main Tasks

* Load normalized test dataset  
* Validate dataset integrity  
* Prepare feature matrix (`X_test`) and label vector (`y_test`)  
* Load trained models  
* Generate predictions and class probabilities  
* Compute evaluation metrics (Accuracy, Precision, Recall, F1-score, ROC-AUC)  
* Generate confusion matrices (counts and normalized)  
* Compute ROC curves  
* Compare model performance  
* Save evaluation outputs  

---

## Processing Workflow

This notebook executes a structured sequence of steps to evaluate trained models on unseen data:

### 1. Environment Setup and Verification
The runtime environment is initialized, required libraries are imported, and all paths are loaded from `project_config.py`. Required input files are verified before execution proceeds.

### 2. Data Loading
The normalized test dataset is loaded from disk and basic dataset information is displayed.

### 3. Data Validation and Preparation
The test dataset is verified for:

* Correct metadata structure  
* Expected feature dimensionality (**25 features**)  
* Valid class labels and subset values  
* Absence of missing values  

Feature matrices and encoded labels are prepared for evaluation.

### 4. Model Loading
The trained MLP and RBF SVM models are loaded from stored `.pkl` files.

### 5. Prediction Generation
Each model generates:

* Predicted class labels  
* Class probability estimates  

The correct probability column corresponding to the AI class is extracted for ROC analysis.

### 6. Metric Computation
Evaluation metrics are computed:

* Accuracy  
* Precision  
* Recall  
* F1-score  
* ROC-AUC  

The AI-generated class is treated as the positive class.

### 7. Confusion Matrix Analysis
Confusion matrices are computed for both models:

* Raw count matrices  
* Row-normalized matrices  

Optional visualization is controlled by the `VERBOSE` flag.

### 8. ROC Curve Analysis
ROC curves are computed for both models and optionally visualized.  
ROC point data is also prepared for export.

### 9. Model Comparison
Final evaluation results are aggregated into:

* Sorted results table  
* Report-friendly comparison table  

### 10. Output Generation
All evaluation artifacts are saved:

* Metrics (CSV + JSON)  
* Confusion matrices  
* ROC curve points  
* Final comparison summary  

Validation checks confirm successful output generation.

---

## Notes and Design Choices

* **Independent test evaluation:**  
  The test dataset is never used during training, validation, or tuning.

* **Positive class definition:**  
  The AI-generated class is treated as the positive class for all metrics.

* **Two-model comparison:**  
  Both MLP and RBF SVM are evaluated to provide a robust comparison.

* **Consistent feature pipeline:**  
  The same 25 normalized DIP features are used across all stages.

* **Configuration-driven design:**  
  All file paths and constants are controlled through `project_config.py`.

* **VERBOSE control:**  
  Optional outputs (tables, plots, detailed diagnostics) are controlled via the `VERBOSE` flag.

* **Fail-safe validation:**  
  Multiple validation checks ensure dataset integrity, correct label encoding, and consistency of predictions.

---

## Role in the Overall Pipeline

This notebook represents the **final evaluation stage** of the pipeline.

It answers the key question:

> How well do the trained classifiers generalize to completely unseen data?

The results produced here are used directly for:

* performance reporting  
* comparative analysis  
* final project conclusions  

---

## Next Step

➡️ [13 Feature Level Analysis](13_Feature_Level_Analysis.md)

