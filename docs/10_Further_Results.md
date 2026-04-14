---
title: 10 Further Results
nav_order: 12
---

# 10 Further Results

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/10_Further_Results.ipynb)

---

## Purpose

This notebook explores additional experiments and analyses beyond the core pipeline to better understand the behavior and effectiveness of the DIP feature-based classification approach.

These experiments investigate the contribution of individual features, compare simplified models to the full feature set, and provide further insight into model performance and generalization.

## Inputs

- Normalized feature vector CSV files:
  - `train_feature_vectors_normalized.csv`
  - `test_feature_vectors_normalized.csv`

- Trained model configurations (optional reuse)

- Project configuration file:
  - `project_config.py`

## Outputs

- Single-feature model evaluation results:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - ROC-AUC

- Comparative performance tables

- Additional plots and summaries (optional)

## Main Tasks

- Evaluate models using individual DIP features
- Compare single-feature performance against full feature set
- Analyze feature importance and discriminative power
- Explore model behavior across different datasets
- Summarize insights and observations

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a summary of exploratory analysis objectives and the types of additional results generated.

### Cell 1: Import Libraries and Configuration
Loads required libraries (e.g., scikit-learn, Pandas, NumPy, Matplotlib) and imports shared configuration settings.

### Cell 2: Load Normalized Feature Vectors
Reads training and test feature vector datasets for analysis.

### Cell 3: Prepare Data for Feature-Level Evaluation
Separates features and labels and prepares data structures for evaluating individual features.

### Cell 4: Train Single-Feature Models
Trains classifiers using one feature at a time to assess the predictive power of individual DIP features.

### Cell 5: Evaluate Single-Feature Performance
Computes evaluation metrics for each single-feature model.

### Cell 6: Compare Against Full Feature Model
Compares the performance of single-feature models with the full 26-feature model.

### Cell 7: Analyze Results
Identifies which features contribute most to classification performance and highlights trends.

### Cell 8: Summarize Findings
Presents conclusions and key insights derived from the experiments.

## Notes and Design Choices

- **Feature-level analysis:**  
  Evaluating individual features provides insight into their relative importance.

- **Comparison to full model:**  
  Demonstrates the benefit of combining multiple complementary features.

- **Exploratory focus:**  
  This notebook is intended for analysis and insight rather than pipeline execution.

- **Interpretability:**  
  Results help explain why the DIP feature-based approach is effective.

## Files Produced

- Single-feature evaluation results (optional CSV)
- Comparative performance summaries
- Optional plots for visualization

## Role in the Overall Pipeline

This notebook extends the core pipeline by providing deeper analysis and validation of the feature design. It supports the overall conclusions of the project and strengthens the justification for the chosen methodology.

## Next Step

➡️ [Thanks For Trying This Tutorial](Thanks_For_Trying_This_Tutorial.md)
