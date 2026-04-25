---
title: 11 Basic Fine-Tuning
parent: 5. Basic Fine-Tuning Tutorial
nav_order: 1
---

# 11 Basic Fine-Tuning

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/11_Basic_Fine-Tuning.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

Improve baseline model performance through controlled hyperparameter tuning using DIP feature vectors.

## Inputs

- `train_feature_vectors.csv`, `test_feature_vectors.csv` — feature vectors (N samples × 25 features)

## Outputs

- `fine_tuning_results.csv` — cross-validation performance summaries  
- `best_model_config.json` — selected model configuration  
- `tuned_model_results.csv` — final evaluation metrics on test dataset  
- `scaler.pkl` — normalization model  

## Processing Summary

- Load training and test feature vectors  
- Separate feature columns and class labels  
- Normalize feature values  
- Define candidate model configurations  
- Evaluate configurations using stratified cross-validation  
- Select best-performing configuration  
- Retrain model on full training dataset  
- Evaluate tuned model on test dataset  
- Save results and model configuration  

## Notes

- Cross-validation is performed only on training data  
- The test dataset is used only for final evaluation  
- Hyperparameter tuning is limited to small, targeted variations  
- A notebook-level `VERBOSE` flag controls optional diagnostic output  

## Next Notebook

➡️ **12 Evaluate Two Models**

