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

Evaluate baseline model performance using DIP feature vectors on the test dataset.

## Inputs

- `train_feature_vectors.csv`, `test_feature_vectors.csv` — feature vectors (N samples × 25 features)

## Outputs

- `basic_testing_results.csv` — baseline evaluation metrics  
- `baseline_model_config.json` — baseline model configuration  
- `scaler.pkl` — normalization model  

## Processing Summary

- Load training and test feature vectors  
- Separate feature columns and class labels  
- Normalize feature values  
- Train baseline classifier  
- Evaluate model performance on test dataset  
- Generate evaluation metrics and save results  

## Notes

- The test dataset is used only for independent evaluation  
- Normalization is fit on training data and applied to both datasets  
- A standard classifier configuration is used to establish baseline performance  
- A notebook-level `VERBOSE` flag controls optional diagnostic output  

## Next Notebook

➡️ [11 Basic Fine-Tuning](11_Basic_Fine-Tuning.md)

