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

Validate and compare the selected classifiers using normalized DIP feature vectors prior to final testing.

## Inputs

- `train_feature_vectors_normalized.csv` — normalized training feature vectors (N samples × 25 features)

## Outputs

- `cross_validation_results.csv` — full cross-validation performance summary  
- `classifier_comparison_tuned.csv` — condensed comparison of key performance metrics  

## Processing Summary

- Load normalized training feature vectors  
- Separate feature columns and class labels  
- Initialize selected classifiers with tuned hyperparameters  
- Evaluate models using stratified cross-validation  
- Compare classifier performance across evaluation metrics  
- Save validation results  

## Notes

- Only the training dataset is used; the test dataset remains untouched  
- Stratified cross-validation ensures consistent and unbiased evaluation  
- ROC-AUC is used as the primary comparison metric  
- A notebook-level `VERBOSE` flag controls optional diagnostic output  

## Next Notebook

➡️ [10 Basic Testing](10_Basic_Testing.md)

