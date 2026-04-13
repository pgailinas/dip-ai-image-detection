---
title: 07 Classifier Selection
nav_order: 9
---

# 07 Classifier Selection

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/07_Classifier_Selection.ipynb)

---

## Overview

This notebook evaluates multiple classifier types using normalized DIP feature vectors to identify the most effective model for distinguishing AI-generated and real images.

---

## Objectives

* Compare multiple classifier types
* Evaluate performance using consistent metrics
* Identify top-performing models
* Select candidates for final training and evaluation

---

## Workflow

1. Load normalized training and validation datasets
2. Define candidate classifiers
3. Train models using training data
4. Evaluate on validation set
5. Compute performance metrics
6. Compare model results
7. Select best-performing classifier(s)

---

## Notebook Structure

### Cell 0 - Overview

Defines purpose and evaluation strategy.

### Cell 1 - Imports

Loads required libraries.

### Cell 2 - Load Data

Loads normalized training and validation datasets.

### Cell 3 - Define Classifiers

Specifies candidate models (linear models, SVM, tree-based methods, MLP).

### Cell 4 - Training Loop

Trains each classifier on the training dataset.

### Cell 5 - Validation Evaluation

Evaluates each model using the validation dataset.

### Cell 6 - Metrics Computation

Calculates performance metrics (accuracy, precision, recall, F1 score, ROC-AUC).

### Cell 7 - Results Comparison

Aggregates and compares classifier performance.

### Cell 8 - Model Selection

Identifies top-performing classifier(s).

### Cell 9 - Optional Save

Exports results if needed.

---

## Outputs

* Classifier performance comparison table
* Selected model(s) for final training
* Evaluation metrics for each classifier

---

## Key Design Features

* Consistent evaluation across models
* Metric-driven model selection
* Modular comparison framework
* Reproducible validation process

---

## Next Step

-> 08 Train Neural Network
