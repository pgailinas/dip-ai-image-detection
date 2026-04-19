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

* Normalized feature vector CSV file:

  * `train_feature_vectors_normalized.csv`

* Project configuration file:

  * `project_config.py`

Classifier configurations are defined within this notebook based on results
from Notebook 07.

---

## Outputs

The following trained models, configurations, and evaluation summaries are generated:

### Model Artifacts (`metadata/models/`)

* `final_rbf_svm_model.pkl`

* `final_mlp_model.pkl`

* `best_rbf_svm_model_config.json`

* `best_mlp_model_config.json`

### Training and Validation Results (`metadata/results/`)

* `cross_validation_results.csv`

---

## Main Tasks

* Load normalized training feature vectors
* Validate dataset integrity
* Separate features and labels
* Define selected classifier configurations
* Initialize classifiers with tuned hyperparameters
* Perform cross-validation on both classifiers
* Compare model performance
* Train both models on full training data
* Save trained models and configuration summaries

---

## Processing Workflow

This notebook executes a structured sequence of steps to train and prepare the selected classifiers:

1. **Environment Setup and Data Loading**
   Required libraries are imported, and the normalized training dataset is loaded.

2. **Data Validation and Preparation**
   The dataset is verified for:

   * Correct metadata structure
   * Expected feature dimensionality
   * Absence of missing values
     Feature matrices and labels are separated for model training.

3. **Classifier Configuration Definition**
   The two selected classifiers are defined using optimized hyperparameters derived from prior evaluation.

4. **Cross-Validation Evaluation**
   Both classifiers are evaluated using stratified k-fold cross-validation, producing performance metrics across multiple evaluation criteria.

5. **Performance Comparison**
   Cross-validation results are aggregated and compared, with emphasis on ROC-AUC and overall consistency.

6. **Final Model Training**
   Each classifier is retrained on the full training dataset to maximize performance.

7. **Model and Result Persistence**
   Trained models, configuration details, and cross-validation results are saved for downstream evaluation and reproducibility.

---

## Notes and Design Choices

* **Two-model training approach:**
  Both RBF SVM and MLP are retained to enable comparative evaluation.

* **In-notebook configuration:**
  Classifier parameters are defined directly in this notebook based on prior selection results.

* **Cross-validation validation:**
  Both models are evaluated using stratified k-fold cross-validation prior to final training.

* **Final training on full dataset:**
  Models are retrained on all available training data to maximize performance.

* **Model persistence:**
  Saving trained models enables reproducible evaluation in subsequent notebooks.

---

## Role in the Overall Pipeline

This notebook represents the **model training stage** of the pipeline.

It takes the selected classifiers from Notebook 07, trains them using consistent procedures, and produces final models ready for independent test evaluation.

---

## Next Step

➡️ `09_Validate_and_Tune_Two_Models.md`



