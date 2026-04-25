---
title: 08 Train Two Classifiers
parent: 3. Model Optimization Tutorial
nav_order: 2
---

# 08 Train Two Classifiers

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/08_Train_Two_Classifiers.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

Train the selected classifiers using normalized DIP feature vectors and prepare final models for evaluation.

## Inputs

- `train_feature_vectors_normalized.csv` — normalized training feature vectors (N samples × 25 features)

## Outputs

- `final_rbf_svm_model.pkl`, `final_mlp_model.pkl` — trained classifier models  
- `best_rbf_svm_model_config.json`, `best_mlp_model_config.json` — model configurations  
- `cross_validation_results.csv` — cross-validation performance results  

## Processing Summary

- Load normalized training feature vectors  
- Separate feature columns and class labels  
- Initialize classifiers with selected hyperparameters  
- Evaluate models using stratified cross-validation  
- Train classifiers on full training dataset  
- Save trained models and evaluation results  

## Notes

- Two classifiers (RBF SVM and MLP) are trained for downstream comparison  
- Cross-validation is performed prior to final training  
- Models are retrained on the full training dataset after validation  
- A notebook-level `VERBOSE` flag controls optional diagnostic output  

## Next Notebook

➡️ [09 Validate and Tune Two Models](09_Validate_and_Tune_Two_Models.md)

