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
classifiers using normalized **25-dimensional Digital Image Processing (DIP) feature vectors**.

The focus is on evaluating the retained models:

* RBF Support Vector Machine (RBF SVM)  
* Multi-Layer Perceptron (MLP)  

Both classifiers are evaluated using a consistent stratified cross-validation  
framework to compare their performance prior to final independent testing.

---

## Inputs

* Normalized training feature vectors (config-driven path):

  * `metadata/vectors/train_feature_vectors_normalized.csv`

* Project configuration file:

  * `src/project_config.py`

Classifier configurations are defined within this notebook based on  
results from Notebook 07 and the finalized two-model training design.

---

## Outputs

All validation results are saved to `metadata/results/`:

* `cross_validation_results.csv`  
  Full cross-validation performance summary.

* `classifier_comparison_tuned.csv`  
  Condensed comparison of key performance metrics.

---

## Main Tasks

* Load normalized training feature vectors  
* Validate dataset integrity  
* Separate features and labels  
* Define selected classifier configurations  
* Perform stratified k-fold cross-validation  
* Evaluate models using multiple performance metrics  
* Compare validation performance using formatted tables  
* Save validation outputs and verify results  

---

## Processing Workflow

This notebook executes a structured sequence of steps to validate and compare the selected classifiers:

1. **Startup and Environment Setup**  
   The runtime environment is initialized, the repository is verified or cloned,  
   `project_config.py` is imported, and config-controlled paths are established.

2. **Data Loading**  
   The normalized training dataset is loaded using config-defined paths.

3. **Data Validation and Preparation**  
   The dataset is verified for:

   * Correct metadata structure  
   * Expected feature dimensionality (25 features)  
   * Absence of missing values  

   Feature matrices and encoded labels are prepared for evaluation.

4. **Classifier Configuration Definition**  
   The two selected classifiers are defined using tuned hyperparameters established in prior steps.

5. **Cross-Validation Evaluation**  
   Both classifiers are evaluated using stratified k-fold cross-validation, producing metrics including:

   * Accuracy  
   * Precision  
   * Recall  
   * F1-score  
   * ROC-AUC  

6. **Performance Aggregation and Comparison**  
   Results are compiled, ranked by ROC-AUC, and presented using readable and side-by-side comparison tables.

7. **Output Generation**  
   Validation results are saved to disk using config-controlled output paths.

8. **Output Validation (Sanity Check)**  
   Saved files are reloaded and verified to ensure correctness and consistency.

---

## Notes and Design Choices

* **Two-model validation approach:**  
  Both RBF SVM and MLP are evaluated to preserve a fair comparison prior to final testing.

* **Config-driven pipeline:**  
  All paths and constants are sourced from `project_config.py` for consistency and portability.

* **VERBOSE-controlled output:**  
  A notebook-level `VERBOSE` flag controls display detail:

  * `True` → detailed diagnostics, previews, and formatted tables  
  * `False` → minimal output  

* **Cross-validation framework:**  
  Stratified k-fold cross-validation ensures consistent and unbiased evaluation.

* **Strict train/test separation:**  
  Only the training dataset is used in this notebook. The independent test set remains untouched.

---

## Role in the Overall Pipeline

This notebook represents the **validation stage** of the pipeline.

It evaluates the selected classifiers using consistent procedures and  
produces performance summaries that support interpretation of final test results.

---

## Next Step

➡️ [10 Basic Testing](10_Basic Testing.md)

