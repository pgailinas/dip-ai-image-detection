---
title: 12 Evaluate Two Models
parent: 6. Full Training Tutorial
nav_order: 1
---

# 12 Evaluate Two Models

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/12_Evaluate_Two_Models.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

Evaluate trained classifiers on the held-out test dataset using normalized DIP feature vectors.

## Inputs

- `test_feature_vectors_normalized.csv` — normalized test feature vectors (N samples × 25 features)  
- `final_rbf_svm_model.pkl`, `final_mlp_model.pkl` — trained classifier models  

## Outputs

- `final_test_results.csv`, `final_test_results.json` — evaluation metrics for both models  
- `final_confusion_matrix_mlp.csv`, `final_confusion_matrix_rbf_svm.csv` — confusion matrices  
- `final_roc_points_mlp.csv`, `final_roc_points_rbf_svm.csv` — ROC curve data  
- `final_comparison_summary.csv` — model performance comparison  

## Processing Summary

- Load normalized test dataset  
- Load trained classifier models  
- Generate predictions and class probabilities  
- Compute evaluation metrics  
- Generate confusion matrices and ROC curves  
- Compare model performance  
- Save evaluation results  

## Notes

- The test dataset is used only for independent evaluation  
- The AI-generated class is treated as the positive class  
- Both classifiers are evaluated for comparative analysis  
- A notebook-level `VERBOSE` flag controls optional diagnostic output  

## Next Notebook

➡️ [13 Feature-Level Analysis](13_Feature_Level_Analysis.md)

