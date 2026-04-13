# 09 Validate Tune Two Models

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/09_Validate_Tune_Two_Models.ipynb)

---

## Overview

This notebook validates baseline Multi-Layer Perceptron (MLP) models and performs limited hyperparameter tuning to identify an optimal classifier configuration prior to final testing.

It also includes a controlled comparison between full feature models and single-feature models to evaluate the contribution of individual DIP features.

---

## Objectives

* Load prepared training and validation datasets
* Load baseline trained MLP models
* Evaluate baseline model performance
* Define a limited hyperparameter tuning space
* Train and evaluate tuned models
* Compare baseline and tuned models
* Select and save the best model configuration
* Compare full-feature models against single-feature models

---

## Workflow

1. Load normalized datasets
2. Perform sanity checks
3. Load baseline models
4. Evaluate baseline performance
5. Define tuning configurations
6. Train tuned models
7. Evaluate tuned models
8. Combine and compare results
9. Select and save best model
10. Perform single-feature comparison

---

## Notebook Structure

### Cell 0 — Notebook Summary

Defines the purpose of validation and tuning, describes inputs and outputs, and places the notebook within the overall pipeline.

---

### Cell 1 — Imports

Loads required libraries, including:

* pandas
* numpy
* joblib / pickle
* sklearn metrics
* sklearn `MLPClassifier`

---

### Cell 2 — Load Data

Loads the training and validation datasets, separates feature matrices and labels, and confirms dataset structure.

---

### Cell 3 — Sanity Checks

Verifies:

* matching feature columns between datasets
* absence of missing values
* correct label encoding

Ensures datasets are consistent and suitable for evaluation.

---

### Cell 4 — Load Baseline Models

Loads previously trained MLP models from Notebook 07 and confirms successful loading.

---

### Cell 5 — Evaluate Baseline Models

Runs baseline models on the validation dataset and computes standard classification metrics.

Stores results in a structured format for comparison.

---

### Cell 6 — Define Tuning Configurations

Defines a limited set of hyperparameter variations, including:

* hidden layer configurations
* regularization strength (`alpha`)
* early stopping settings

This forms the search space for model tuning.

---

### Cell 7 — Train and Evaluate Tuned Models

Trains new MLP models using the configurations defined in Cell 6 and evaluates them on the validation dataset.

Stores performance metrics for each model.

---

### Cell 7 (continued) — Combine Results

Merges baseline and tuned model results into a single comparison table.

Sorts models by performance metric to enable consistent selection.

---

### Cell 8 — Select Best Model and Save Configuration

Selects the best-performing model based on validation results.

Extracts and saves:

* model architecture
* hyperparameters
* feature column ordering
* label class definitions

Writes outputs such as:

* model file (`.pkl`)
* configuration JSON
* results CSV

---

### Cell 9 — Single-Feature Performance Comparison

Trains and evaluates models using individual features only.

Compares these single-feature models against the full feature model to assess the contribution of individual features.

Results are structured for comparison but not used for model selection.

---

## Outputs

* Selected trained model (`.pkl`)
* Model configuration (`.json`)
* Model comparison results (`.csv`)
* Optional single-feature comparison outputs

---

## Validation Checks

This notebook ensures:

* consistent feature structure across datasets
* no missing or invalid values
* proper label handling
* consistent evaluation metrics across all models
* fair comparison between baseline and tuned configurations

---

## Key Design Features

* Separation of baseline evaluation and tuning
* Controlled and limited hyperparameter search
* Structured comparison of multiple models
* Reproducible model selection process
* Preservation of feature ordering for downstream evaluation
* Inclusion of single-feature analysis for interpretability

---

## Role in Pipeline

This notebook performs model validation and selection, identifying a finalized classifier configuration based on validation performance.

The selected model and configuration are passed forward for independent evaluation on the test dataset.

---

## Next Step

➡️ **09 Final Test Evaluation**

