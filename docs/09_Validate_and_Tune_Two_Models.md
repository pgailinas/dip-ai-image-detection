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

- RBF Support Vector Machine (RBF SVM)  
- Multi-Layer Perceptron (MLP)  

Both classifiers are evaluated using a consistent stratified cross-validation  
framework to compare their performance prior to final independent testing.

---

## Inputs

- Normalized training feature vectors:
  - `metadata/vectors/train_feature_vectors_normalized.csv`

- Project configuration file:
  - `project_config.py`

Classifier configurations are defined within this notebook based on  
results from Notebook 07 and the finalized model design.

---

## Outputs

All outputs are saved to `metadata/results/`:

- `cross_validation_results.csv` — Full cross-validation performance summary  
- `classifier_comparison_tuned.csv` — Condensed comparison of key metrics  

---

## Main Tasks

- Load normalized training feature vectors  
- Validate dataset integrity  
- Separate features and labels  
- Define selected classifier configurations  
- Perform stratified k-fold cross-validation  
- Evaluate models using multiple performance metrics  
- Compare validation performance  
- Save validation outputs  

---

## Cell-by-Cell Description

### Cell 0: Notebook Summary
Provides an overview of validation objectives and workflow.

### Startup Cell
Initializes environment, sets project paths, and verifies required input files.

### Cell 1: Import Required Libraries
Loads required libraries including NumPy, pandas, and scikit-learn.

### Cell 2: Load Normalized Training Data
Reads the normalized training dataset and displays structure information.

### Cell 3: Validate Training Data
Performs sanity checks including:
- metadata column verification  
- feature count validation (25 features)  
- missing value checks  
- label consistency  
- preparation of `X_train` and `y_train`  

### Cell 4: Define Classifier Configurations
Defines the two selected classifiers and their tuned hyperparameters.

### Cell 5: Cross-Validate Classifiers
Evaluates both classifiers using stratified k-fold cross-validation across multiple performance metrics.

### Cell 6: Summarize and Compare Results
Aggregates and compares validation performance, prioritizing ROC-AUC.

### Cell 7: Save Validation Outputs
Saves cross-validation results and comparison tables to `metadata/results/`.

### Cell 8: Validation Output Sanity Check
Reloads saved files and verifies correctness of outputs.

---

## Notes and Design Choices

- **Two-model validation approach:**  
  Both RBF SVM and MLP are evaluated to preserve a fair comparison prior to final testing.

- **In-notebook configuration:**  
  Classifier parameters are defined directly in this notebook based on prior selection results.

- **Cross-validation framework:**  
  Stratified k-fold cross-validation ensures consistent and unbiased evaluation.

- **Separation of concerns:**  
  This notebook evaluates model behavior using training data only.  
  Final evaluation on unseen test data is performed in a later notebook.

---

## Files Produced

### `metadata/results/`
- `cross_validation_results.csv` — Full cross-validation performance summary  
- `classifier_comparison_tuned.csv` — Condensed comparison table  

---

## Role in the Overall Pipeline

This notebook represents the **validation and tuning stage** of the pipeline.

It evaluates the selected classifiers using consistent procedures and  
produces performance summaries that inform interpretation of final test results.

---

## Next Step

➡️ `10_Evaluate_Two_Models.md`



