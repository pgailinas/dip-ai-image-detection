---
title: 10 Basic Testing
parent: 4. Basic Testing Tutorial
nav_order: 1
---

# 10 Basic Testing

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/10_Basic_Testing.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook establishes the **baseline performance** of the proposed Digital Image Processing (DIP) feature-based approach for AI-generated image detection.

The goal is to evaluate how well the engineered feature vector performs using a **standard classifier configuration**, without extensive hyperparameter tuning.

This provides a reference point for later improvement and analysis.

---

## Inputs

* Training feature vectors:

  * `metadata/vectors/train_feature_vectors.csv`

* Test feature vectors:

  * `metadata/vectors/test_feature_vectors.csv`

* Project configuration file:

  * `src/project_config.py`

---

## Outputs

All evaluation results are generated within the notebook and may optionally be saved:

* Classification metrics:

  * Accuracy
  * Precision
  * Recall
  * F1-score
  * ROC AUC

* Confusion matrix

* ROC curve

Optional saved outputs:

* `metadata/results/basic_testing_results.csv`

---

## Main Tasks

* Load training and test feature vectors
* Validate dataset structure and integrity
* Separate features and labels
* Normalize feature values
* Train baseline classifier(s)
* Evaluate model performance on the test set
* Generate performance metrics and visualizations

---

## Processing Workflow

This notebook executes a structured sequence of steps:

1. **Environment Setup and Data Loading**  
   The runtime environment is initialized, required libraries are imported, and training and test feature vector datasets are loaded.

2. **Data Validation and Preparation**  
   The datasets are verified for:

   * Correct metadata structure  
   * Expected feature dimensionality  
   * Absence of missing values  

   Feature matrices (`X`) and labels (`y`) are prepared.

3. **Feature Normalization**  
   Feature values are normalized using a standard scaler to ensure consistent input for the classifier.

4. **Baseline Model Training**  
   A baseline classifier is trained using the training dataset.  
   The Multi-Layer Perceptron (MLP) is the primary model used.

5. **Model Evaluation (Test Set)**  
   The trained model is evaluated on the independent test dataset to measure generalization performance.

6. **Performance Reporting**  
   Evaluation metrics and visualizations are generated to summarize model behavior.

---

## Notes and Design Choices

* **Baseline evaluation:**
  This notebook intentionally uses a simple model configuration to establish a reference performance level.

* **Test set usage:**
  The test dataset is used strictly for final evaluation and is not involved in training.

* **Feature normalization:**
  Scaling ensures that all features contribute appropriately to model training.

* **Model simplicity:**
  The focus is on evaluating the effectiveness of the DIP feature vector rather than optimizing the classifier.

* **Reproducibility:**
  Fixed random seeds are used where applicable to ensure consistent results.

---

## Role in the Overall Pipeline

This notebook represents the **initial evaluation stage** of the pipeline.

It answers the key question:

> How effective are the engineered DIP features when used with a standard classifier?

The results serve as a baseline for comparison with later improvements.

---

## Next Step

➡️ [11 Basic Fine-Tuning](11_Basic_Fine-Tuning.md)

