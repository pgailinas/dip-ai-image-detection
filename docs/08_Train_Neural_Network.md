---
title: 08 Train Neural Network
nav_order: 8
---

# 08 Train Neural Network

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/07_Train_Neural_Network.ipynb)

---

## Overview

This notebook trains baseline Multi-Layer Perceptron (MLP) classifiers using normalized DIP feature vectors.

---

## Objectives

* Train baseline models
* Compare architectures
* Establish initial performance

---

## Workflow

1. Setup environment
2. Load datasets
3. Perform sanity checks
4. Define models
5. Train models
6. Evaluate performance
7. Save outputs

---

## Notebook Structure

### Cell 0 — Overview

Defines training objectives and pipeline role. 

### Cell 1 — Environment Setup

Mounts Drive and initializes environment. 

### Cell 2 — Data Loading

Loads normalized training and validation datasets. 

### Cell 3 — Data Preparation

Separates features and labels, removes metadata. 

### Cell 4 — Sanity Checks

Verifies shapes, normalization, and class balance. 

### Cell 5 — Model Definition

Defines MLP architectures:

* Small
* Medium
* Large 

### Cell 6 — Model Training

Trains models and computes performance metrics. 

### Cell 7 — Results Summary

Aggregates and compares model performance. 

### Cell 8 — Save Results

Stores trained models and results CSV. 

---

## Outputs

* Trained MLP models (.pkl)
* baseline_model_results.csv
* Performance comparison table

---

## Key Observations

* Strong baseline performance (~87–88%)
* Larger models overfit
* DIP features are highly effective

---

## Role in Pipeline

Establishes baseline model performance for further tuning.

---

## Next Step

➡️ **08 Evaluation**

