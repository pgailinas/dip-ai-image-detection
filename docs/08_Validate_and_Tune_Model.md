# 08 Validate and Tune Model

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/08_Validate_and_Tune_Model.ipynb)

---

## Overview

This notebook validates baseline Multi-Layer Perceptron (MLP) models and performs limited hyperparameter tuning to identify the best-performing classifier configuration before final test evaluation.

It serves as the model selection stage of the pipeline, using the validation dataset to compare baseline and tuned models in a controlled and reproducible manner.

---

## Objectives

* Load prepared training and validation datasets
* Load baseline trained MLP models
* Evaluate baseline validation performance
* Define a limited hyperparameter tuning space
* Train and evaluate tuned models
* Compare all candidate models
* Select and save the best overall model configuration

---

## Workflow

1. Load normalized training and validation datasets
2. Perform consistency and sanity checks
3. Load baseline models from Notebook 07
4. Evaluate baseline model performance
5. Define tuning configurations
6. Train and evaluate tuned models
7. Combine and compare results
8. Select best model and save configuration

---

## Notebook Structure

### Cell 0 — Notebook Summary

Describes the purpose of validation and tuning, defines the role of the notebook in the overall pipeline, and lists the expected inputs and outputs. 

### Cell 1 — Imports

Loads required libraries, including:

* pandas
* numpy
* joblib / pickle
* sklearn metrics
* sklearn `MLPClassifier` 

### Cell 2 — Load Data

Loads the prepared training and validation datasets, separates features and labels, and confirms expected dataset shapes:

* Train: (8400, 26)
* Validation: (1800, 26) 

### Cell 3 — Sanity Checks

Verifies that:

* training and validation feature columns match
* there are no missing values
* label encoding is correct

This cell ensures both datasets are ready for fair model comparison. 

### Cell 4 — Load Baseline Models

Loads the baseline MLP models saved in Notebook 07.
These models differ primarily by architecture (for example, small, medium, and large network sizes) and are checked for successful loading. 

### Cell 5 — Evaluate Baseline Models

Runs each baseline model on the validation dataset and computes performance metrics, including:

* Accuracy
* Precision
* Recall
* F1-score
* ROC AUC (optional/when available)

Results are stored in a structured format for later comparison. 

### Cell 6 — Define Tuning Configurations

Defines the limited hyperparameter search space used for tuning.
This includes selected variations of:

* hidden layer sizes
* regularization strength (`alpha`)
* early stopping option

The search space is intentionally kept small to limit complexity and runtime. 

### Cell 7 — Train and Evaluate Tuned Models

Trains new MLP models using the tuning configurations defined in Cell 6, then evaluates each tuned model on the validation dataset.
For each model, it computes:

* Accuracy
* Precision
* Recall
* F1-score
* ROC AUC

The resulting metrics are stored in a structured DataFrame for comparison. 

### Cell 7 (continued) — Combine Results

Merges the baseline and tuned model results into a single comparison table.
This combined table is sorted by validation accuracy so that the top-performing model can be identified clearly. 

### Cell 8 — Select Best Model and Save Configuration

Selects the best-performing model from the combined results and reports its key validation metrics:

* Accuracy
* Precision
* Recall
* F1-score
* ROC AUC

This cell also extracts and saves the chosen configuration, including:

* hidden-layer architecture
* hyperparameters
* feature column order
* label class definitions

Outputs saved include:

* `best_model_config.json`
* `tuned_model_results.csv`
* selected model `.pkl` file in the models directory 

---

## Outputs

* `best_model_config.json`
* `tuned_model_results.csv`
* Selected trained model (`.pkl`)

---

## Validation Checks

This notebook verifies:

* consistent feature dimensions between train and validation datasets
* absence of missing or invalid values
* correct label encoding
* fair comparison across baseline and tuned models
* consistent metric computation across all candidates 

---

## Key Design Features

* Clear separation of baseline evaluation and tuning
* Structured comparison across multiple models
* Lightweight and efficient hyperparameter tuning
* Reproducible model selection via saved configuration
* Preservation of feature ordering for downstream test evaluation 

---

## Role in Pipeline

This notebook serves as the **model validation and selection stage** of the pipeline.

It identifies the best-performing classifier configuration based on validation performance and saves the finalized model artifacts required for independent evaluation on the test dataset.

---

## Next Step

➡️ **09 Final Test Evaluation**

