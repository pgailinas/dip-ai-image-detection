# 10 Further Results

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/10_Further_Results.ipynb)

---

## Overview

This notebook evaluates the final trained model using the independent test dataset to measure true generalization performance.
In addition to full-model evaluation, it includes a baseline comparison using single-feature models to assess the discriminative power of individual DIP features.

---

## Objectives

* Evaluate final model on independent test dataset
* Compute comprehensive performance metrics
* Generate confusion matrix and ROC curve
* Compare full model against single-feature baselines
* Validate model generalization

---

## Workflow

1. Load trained model
2. Load test dataset
3. Generate predictions
4. Compute evaluation metrics
5. Create confusion matrix
6. Generate ROC curve and AUC
7. Evaluate single-feature models
8. Compare results

---

## Notebook Structure

### Cell 0 - Overview

Defines purpose and evaluation scope.

### Cell 1 - Imports

Loads required libraries.

### Cell 2 - Load Model

Loads the trained classifier.

### Cell 3 - Load Test Data

Loads normalized test dataset.

### Cell 4 - Generate Predictions

Applies model to test data.

### Cell 5 - Metrics Computation

Calculates accuracy, precision, recall, F1 score, and ROC-AUC.

### Cell 6 - Confusion Matrix

Generates and displays confusion matrix.

### Cell 7 - ROC Curve

Plots ROC curve and computes AUC.

### Cell 8 - Results Summary

Summarizes evaluation results.

### Cell 9 - Single-Feature Performance Comparison

Evaluates selected individual DIP features as standalone inputs using a simple classifier.
Each feature is independently scaled, trained, and tested to measure its standalone predictive capability.

### Cell 10 - Full vs Single-Feature Comparison

Compares the full 26-feature model against single-feature models using metrics such as accuracy and ROC-AUC.
Provides visual or tabular comparison of performance differences.

### Cell 11 - Optional Save

Saves metrics, plots, or outputs if needed.

---

## Outputs

* Test set performance metrics
* Confusion matrix
* ROC curve and AUC
* Single-feature comparison results
* Final evaluation summary

---

## Key Design Features

* Strict use of independent test set
* Comprehensive performance evaluation
* Baseline comparison using individual features
* Clear visualization of model effectiveness
* Reproducible evaluation process

---

## Next Step

-> Project Report / Final Analysis
