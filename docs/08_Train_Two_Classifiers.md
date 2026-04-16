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

This notebook trains and compares two selected classifiers—**Radial Basis Function Support Vector Machine (RBF SVM)** and **Multi-Layer Perceptron (MLP)**—using the normalized DIP feature vectors.

Both models are evaluated using cross-validation on the training dataset. The best-performing configuration for each classifier type is then trained on the full training set and saved for final evaluation.

## Inputs

- Normalized feature vector CSV files:
  - `train_feature_vectors_normalized.csv`
  - `test_feature_vectors_normalized.csv`

- Project configuration file:
  - `project_config.py`

## Outputs

- Trained model files:
  - `best_rbf_svm_model.pkl`
  - `best_mlp_model.pkl`

- Cross-validation results:
  - `cross_validation_results.csv`

- Best model configurations:
  - `best_model_config.json`

## Main Tasks

- Load normalized feature vectors
- Separate features and labels
- Define hyperparameter grids for both classifiers
- Perform cross-validation with hyperparameter tuning
- Compare model performance
- Select best configurations
- Train final models on full training data
- Save trained models and results

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a summary of training objectives, including comparison of two classifier types and expected outputs.

### Cell 1: Import Libraries and Configuration
Loads required libraries (e.g., scikit-learn, Pandas, NumPy) and imports shared configuration settings.

### Cell 2: Load Normalized Feature Vectors
Reads the normalized training dataset and prepares feature and label arrays.

### Cell 3: Prepare Training Data
Separates input features (`X_train`) and target labels (`y_train`) for use in model training.

### Cell 4: Define Hyperparameter Grids
Specifies parameter grids for:
- RBF SVM (e.g., C, gamma)
- MLP (e.g., hidden layer sizes, regularization)

### Cell 5: Perform Cross-Validation and Hyperparameter Tuning
Uses GridSearchCV with stratified k-fold cross-validation to evaluate different parameter combinations for both classifiers.

### Cell 6: Compare Model Performance
Analyzes cross-validation results and identifies the best-performing configuration for each classifier type.

### Cell 7: Train Final Models
Retrains the best RBF SVM and MLP models using the full training dataset.

### Cell 8: Save Trained Models
Saves both trained models to disk for use in final evaluation.

### Cell 9: Save Cross-Validation Results and Best Configurations
Writes cross-validation summaries and selected hyperparameters to CSV and JSON files for documentation and reproducibility.

## Notes and Design Choices

- **Two-model comparison:**  
  Both RBF SVM and MLP are retained to compare different learning approaches.

- **Cross-validation-based tuning:**  
  Hyperparameters are selected using stratified k-fold cross-validation to ensure robust model selection.

- **Final training on full dataset:**  
  After tuning, models are retrained on all available training data to maximize performance.

- **Model persistence:**  
  Saving trained models allows consistent evaluation and reuse without retraining.

## Files Produced

- `best_rbf_svm_model.pkl` — Trained RBF SVM model
- `best_mlp_model.pkl` — Trained MLP model
- `cross_validation_results.csv` — Summary of CV performance
- `best_model_config.json` — Selected hyperparameters and metadata

## Role in the Overall Pipeline

This notebook produces the final trained models used for independent evaluation. It represents the transition from model selection to finalized classifier implementations.

## Next Step

➡️ [09 Validate and Tune Two Models](09_Validate_and_Tune_Two_Models.md)

