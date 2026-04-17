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

- Normalized feature vector CSV file:
  - `train_feature_vectors_normalized.csv`

- Project configuration file:
  - `project_config.py`

---

## Outputs

- Baseline classifier comparison results:
  - `classifier_comparison_baseline.csv`

- Tuned classifier comparison results:
  - `classifier_comparison_tuned.csv`

- Top classifier configurations:
  - `best_classifier_config.json`

---

## Main Tasks

- Load normalized feature vectors
- Validate dataset integrity
- Separate features and labels
- Define candidate classifiers
- Perform cross-validation
- Evaluate models using multiple metrics
- Rank classifiers based on performance
- Apply controlled hyperparameter tuning
- Select and save the **top two classifiers**

---

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a summary of classifier selection objectives, including evaluation methodology and outputs.

### Cell 1: Import Required Libraries
Loads required libraries including NumPy, pandas, and scikit-learn classifiers.

### Cell 2: Load Normalized Training Data
Reads the normalized training dataset and displays sample rows and column names.

### Cell 3: Validate Training Data
Performs sanity checks including:
- missing values
- class distribution
- metadata columns
- feature count (25 features)

### Cell 4: Prepare Training Data
Separates:
- feature matrix (`X_train`)
- target labels (`y_train`)
- encodes labels for classification

### Cell 5: Define Candidate Classifiers
Defines:
- multiple classifier types (SVM, MLP, RF, etc.)
- stratified k-fold cross-validation strategy
- evaluation metrics

### Cell 6: Run Baseline Classifier Comparison
Applies cross-validation to each classifier and computes:
- accuracy
- precision
- recall
- F1-score
- ROC-AUC

### Cell 7: Compile and Rank Results
Aggregates and ranks classifier performance, prioritizing ROC-AUC.

### Cell 8: Tune Top Classifiers
Applies **controlled (small-grid) hyperparameter tuning** to top-performing classifiers.

### Cell 9: Save Results
Saves:
- baseline comparison results (CSV)
- tuned comparison results (CSV)
- **top two classifier configurations (JSON)**

### Cell 10: Summary and Recommendations
Summarizes results and recommends the **top two classifiers** for downstream training and evaluation.

---

## Notes and Design Choices

- **Cross-validation approach:**  
  Stratified k-fold cross-validation ensures stable and reliable performance estimates.

- **Multiple evaluation metrics:**  
  Models are evaluated using accuracy, precision, recall, F1-score, and ROC-AUC.

- **ROC-AUC prioritization:**  
  ROC-AUC is used as the primary ranking metric due to its robustness in binary classification.

- **Controlled tuning:**  
  Hyperparameter tuning uses small, targeted grids rather than exhaustive search.

- **Multi-model selection:**  
  The top two classifiers are selected to:
  - reduce sensitivity to small performance differences
  - enable comparison across model types
  - improve experimental robustness

---

## Files Produced

- `classifier_comparison_baseline.csv` — Cross-validation results for all classifiers  
- `classifier_comparison_tuned.csv` — Results after hyperparameter tuning  
- `best_classifier_config.json` — Configuration of the **top two classifiers**

---

## Role in the Overall Pipeline

This notebook identifies the strongest classifier candidates for the DIP feature representation and prepares them for final training.

The selected classifiers are trained and evaluated in subsequent notebooks.

---

## Next Step

➡️ [08 Train Two Classifiers](08_Train_Two_Classifiers.md)

