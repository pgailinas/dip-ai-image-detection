---
title: 08 Train Two Classifiers
parent: 3. Model Optimization Tutorial
nav_order: 2
---

# 08 Train Two Classifiers

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/08_Train_Two_Classifiers.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook performs **model training** for the top-performing classifiers  
identified in Notebook 07 using the normalized DIP feature vectors.

Rather than selecting a single model, this notebook trains **two classifiers**  
(e.g., RBF SVM and MLP) using their optimized hyperparameters and prepares them  
for final independent evaluation.

---

## Inputs

- Normalized feature vector CSV file:
  - `train_feature_vectors_normalized.csv`

- Project configuration file:
  - `project_config.py`

Classifier configurations are defined within this notebook based on results  
from Notebook 07.

---

## Outputs

### Model Artifacts (`metadata/models/`)

- `final_rbf_svm_model.pkl`
- `final_mlp_model.pkl`

- `best_rbf_svm_model_config.json`
- `best_mlp_model_config.json`

### Training/Validation Results (`metadata/results/`)

- `cross_validation_results.csv`

---

## Main Tasks

- Load normalized training feature vectors
- Validate dataset integrity
- Separate features and labels
- Define selected classifier configurations
- Initialize classifiers with tuned hyperparameters
- Perform cross-validation on both classifiers
- Compare model performance
- Train both models on full training data
- Save trained models and configuration summaries

---

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a summary of training objectives and workflow.

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

### Cell 4: Define Classifier Configurations
Defines the two selected classifiers and their tuned hyperparameters.

### Cell 5: Cross-Validate Classifiers
Evaluates both classifiers using stratified k-fold cross-validation and multiple performance metrics.

### Cell 6: Summarize and Rank Results
Aggregates and compares classifier performance, prioritizing ROC-AUC.

### Cell 7: Train Final Models
Trains both classifiers on the full training dataset.

### Cell 8: Save Trained Models
Saves trained models to `.pkl` files in `metadata/models/`.

### Cell 9: Save Results and Configurations
Saves cross-validation results to `metadata/results/` and per-model configuration files to `metadata/models/`.

---

## Notes and Design Choices

- **Two-model training approach:**  
  Both RBF SVM and MLP are retained to enable comparative evaluation.

- **In-notebook configuration:**  
  Classifier parameters are defined directly in this notebook based on prior selection results.

- **Cross-validation validation:**  
  Both models are evaluated using stratified k-fold cross-validation prior to final training.

- **Final training on full dataset:**  
  Models are retrained on all available training data to maximize performance.

- **Model persistence:**  
  Saving trained models enables reproducible evaluation in subsequent notebooks.

---

## Files Produced

### `metadata/models/`
- `final_rbf_svm_model.pkl` — Trained RBF SVM model  
- `final_mlp_model.pkl` — Trained MLP model  
- `best_rbf_svm_model_config.json` — RBF SVM configuration and metadata  
- `best_mlp_model_config.json` — MLP configuration and metadata  

### `metadata/results/`
- `cross_validation_results.csv` — Cross-validation performance summary  

---

## Role in the Overall Pipeline

This notebook represents the **model training stage** of the pipeline.

It takes the selected classifiers from Notebook 07, trains them using consistent procedures, and produces final models ready for independent test evaluation.

---

## Next Step

➡️ `09_Validate_and_Tune_Two_Models.md`


