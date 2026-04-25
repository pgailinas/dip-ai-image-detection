---
title: 14 Source-Pair Analysis
parent: 6. Full Training Tutorial
nav_order: 3
---

# 14 Source-Pair Analysis

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/14_Source_Pair_Analysis.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook evaluates model generalization across dataset combinations by training and testing classifiers on specific pairs of real and AI image sources.

The goal is to assess sensitivity to dataset selection and understand how performance varies across different source pairings.

---

## Inputs

* Normalized feature vector CSV files:

  * `train_feature_vectors_normalized.csv`
  * `test_feature_vectors_normalized.csv`

* Project configuration file:

  * `project_config.py`

---

## Outputs

The following generalization analysis results are generated:

* Source-pair performance metrics:

  * Accuracy
  * Precision
  * Recall
  * F1-score
  * ROC-AUC

* Comparative performance tables across all experiments

---

## Main Tasks

* Define source combinations
* Construct balanced datasets for each experiment
* Train classifiers per source pair
* Evaluate model performance
* Aggregate and compare results
* Analyze generalization behavior

---

## Processing Workflow

1. **Source Combination Definition**
   Define experiment sets:

   * 1 real vs 1 AI (9 experiments)
   * 2 real vs 2 AI (9 experiments)

2. **Dataset Construction**
   Build balanced datasets for each experiment.

3. **Model Training per Experiment**
   Train classifiers independently for each source pairing.

4. **Performance Evaluation**
   Compute standard classification metrics.

5. **Result Aggregation**
   Compile results into structured comparison tables.

6. **Analysis and Interpretation**
   Examine:

   * dataset sensitivity
   * generator detectability
   * robustness across combinations

---

## Notes and Design Choices

* **Generalization analysis:**
  Evaluates how model performance varies across dataset combinations.

* **Balanced comparisons:**
  Each experiment maintains consistent class representation.

* **Complementary to core evaluation:**
  Provides insight beyond aggregate test performance.

---

## Role in the Overall Pipeline

This notebook evaluates model robustness and generalization across different data sources, strengthening interpretation of final results.

---

## Next Step

➡️ [Thanks For Trying This Tutorial](Thanks_For_Trying_This_Tutorial.md)


