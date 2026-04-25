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
identified in Notebook 07 using normalized **25-dimensional Digital Image Processing (DIP) feature vectors**.

Rather than selecting a single model, this notebook trains **two classifiers**  
(RBF SVM and MLP) using their optimized hyperparameters and prepares them  
for final independent evaluation.

---

## Inputs

* Normalized feature vector CSV file (config-driven path):

  * `metadata/vectors/train_feature_vectors_normalized.csv`

* Project configuration file:

  * `src/project_config.py`

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
* Perform stratified k-fold cross-validation  
* Compare model performance  
* Train both models on full training data  
* Save trained models and configuration summaries  

---

## Processing Workflow

This notebook executes a structured sequence of steps to train and prepare the selected classifiers:

1. **Startup and Environment Setup**  
   Repository access is verified, configuration is imported from `project_config.py`, and paths are validated.

2. **Data Loading**  
   The normalized training dataset is loaded using config-defined paths.

3. **Data Validation and Preparation**  
   The dataset is verified for:

   * Correct metadata structure  
   * Expected feature dimensionality (25 features)  
   * Absence of missing values  

   Feature matrices and labels are separated and encoded.

4. **Classifier Configuration Definition**  
   The selected classifiers are defined using optimized hyperparameters derived from Notebook 07.

5. **Cross-Validation Evaluation**  
   Both classifiers are evaluated using stratified k-fold cross-validation, producing metrics including:

   * Accuracy  
   * Precision  
   * Recall  
   * F1-score  
   * ROC-AUC  

6. **Performance Comparison**  
   Cross-validation results are aggregated, ranked, and compared using ROC-AUC as the primary metric.

7. **Final Model Training**  
   Each classifier is retrained on the full training dataset to maximize performance.

8. **Model and Result Persistence**  
   Trained models, configuration files, and cross-validation summaries are saved using config-controlled paths.

---

## Notes and Design Choices

* **Two-model training approach:**  
  Both RBF SVM and MLP are retained for downstream comparison.

* **Config-driven pipeline:**  
  All paths and constants are sourced from `project_config.py` to ensure consistency and portability.

* **VERBOSE-controlled output:**  
  A notebook-level `VERBOSE` flag controls display detail:

  * `True` → detailed diagnostics and previews  
  * `False` → minimal output  

* **Cross-validation validation:**  
  Both models are evaluated using stratified k-fold cross-validation prior to final training.

* **Final training on full dataset:**  
  Models are retrained on all available training data to maximize performance.

* **Model persistence:**  
  Saved models enable reproducible evaluation in later notebooks.

---

## Role in the Overall Pipeline

This notebook represents the **model training stage** of the pipeline.

It takes the selected classifiers from Notebook 07, trains them using consistent procedures, and produces final models ready for independent test evaluation.

---

## Next Step

➡️ [09 Validate and Tune Two Models](09_Validate_and_Tune_Two_Models.md)

