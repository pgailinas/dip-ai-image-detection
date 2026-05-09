---
title: Project Directory Structure
nav_order: 1
---

# Project Directory Structure

## Overview

This project uses a structured directory layout to organize datasets, metadata, feature vectors, models, and evaluation outputs. The design supports a fully reproducible pipeline using Google Colab and Google Drive.

All processing steps operate on metadata and stored artifacts rather than duplicating image data, ensuring consistency and efficiency.

---

## Repository Structure

```text
dip-ai-image-detection/
│
├── README.md
│
├── notebooks/
│   ├── 01_Build_Dataset.ipynb
│   ├── 02_Preprocess_Images.ipynb
│   ├── 03_Combine_and_Split.ipynb
│   ├── 04A_Extract_Gradient_Features.ipynb
│   ├── 04B_Extract_Spatial_Features.ipynb
│   ├── 04C_Extract_Frequency_Features.ipynb
│   ├── 05_Build_Feature_Vectors.ipynb
│   ├── 06_Normalize_and_Prepare_Inputs.ipynb
│   ├── 07_Classifier_Selection.ipynb
│   ├── 08_Train_Two_Classifiers.ipynb
│   ├── 09_Validate_and_Tune_Two_Models.ipynb
│   ├── 10_Basic_Testing.ipynb
│   ├── 11_Basic_Fine-Tuning.ipynb
│   ├── 12_Evaluate_Two_Models.ipynb
│   ├── 13_Feature_Level_Analysis.ipynb
│   └── 14_Source_Pair_Analysis.ipynb
│
├── docs/
│   ├── index.md
│   ├── 1. Dataset Tutorial.md
│   ├── 2. Model Description Tutorial.md
│   ├── 3. Model Optimization Tutorial.md
│   ├── 4. Basic Testing Tutorial.md
│   ├── 5. Basic Fine-Tuning Tutorial.md
│   ├── 6. Full Training Tutorial.md
│   ├── 01_Build_Dataset.md
│   ├── 02_Preprocess_Images.md
│   ├── 03_Combine_and_Split.md
│   ├── 04A_Extract_Gradient_Features.md
│   ├── 04B_Extract_Spatial_Features.md
│   ├── 04C_Extract_Frequency_Features.md
│   ├── 05_Build_Feature_Vectors.md
│   ├── 06_Normalize_and_Prepare_Inputs.md
│   ├── 07_Classifier_Selection.md
│   ├── 08_Train_Two_Classifiers.md
│   ├── 09_Validate_and_Tune_Two_Models.md
│   ├── 10_Basic_Testing.md
│   ├── 11_Basic_Fine-Tuning.md
│   ├── 12_Evaluate_Two_Models.md
│   ├── 13_Feature_Level_Analysis.md
│   ├── 14_Source_Pair_Analysis.md
│   ├── Project_Directory_Structure.md
│   ├── Thanks_For_Trying_This_Tutorial.md
│   └── images/
│       ├── basic-fine-tuning-tutorial-pipeline.png
│       ├── basic-testing-tutorial-pipeline.png
│       ├── classifier-comprison.png
│       ├── dataset-tutorial-pipeline.png
│       ├── feature-group-vs-full-model.png
│       ├── full-training-tutorial-pipeline.png
│       ├── model-description-tutorial-pipeline.png
│       ├── model-optimization-tutorial-pipeline.png
│       ├── overview-pipeline.png
│       ├── roc-curve-comparison.png
│       ├── single-feature-barchart.png
│       └── source-pair-roc-curves.png
│
├── src/
│   ├── project_config.py
│   └── datasets/
│       ├── coco_target.py
│       ├── diffusiondb_target.py
│       ├── imagenet_target.py
│       ├── midjourney_target.py
│       ├── openimages_target.py
│       └── sdxl_target.py
│
└── metadata/
    ├── original/
    ├── hashes/
    ├── preprocessed/
    ├── splits/
    ├── features/
    ├── vectors/
    ├── models/
    └── results/
```

---

## Key Directories

### notebooks/
Contains all Google Colab notebooks implementing each step of the pipeline, from dataset construction through final evaluation and analysis.

### docs/
Contains the tutorial documentation pages associated with each notebook, forming the structured learning guide.

### src/
Contains reusable Python modules and configuration files.

- `project_config.py` centralizes all paths and constants  
- `datasets/` contains dataset-specific handlers  

### metadata/

This is the **core working directory** of the project. It stores all intermediate and final artifacts.

- **original/** — raw dataset metadata  
- **hashes/** — dataset integrity and duplicate tracking  
- **preprocessed/** — metadata after preprocessing  
- **splits/** — train/test dataset definitions  
- **features/** — extracted DIP feature values  
- **vectors/** — assembled feature vectors (raw and normalized)  
- **models/** — trained models and scaler  
- **results/** — evaluation outputs and metrics  

---

## Google Drive Structure

All datasets are stored externally in Google Drive and accessed by the notebooks.

```text
releases/
├── raw/
│   ├── DiffusionDB.zip
│   ├── ImageNet_1K_256.zip
│   ├── Midjourney.zip
│   ├── MS_COCO_2017.zip
│   ├── OpenImages.zip (+ split archives)
│   └── SDXL_Generated_10K.zip
│
└── preprocessed/
    ├── All_Sources_preprocessed.zip
    ├── DiffusionDB_preprocessed.zip
    ├── ImageNet_1K_256_preprocessed.zip
    ├── Midjourney_preprocessed.zip
    ├── MS_COCO_2017_preprocessed.zip
    ├── OpenImages_preprocessed.zip
    └── SDXL_Generated_10K_preprocessed.zip
```

---

## Important Notes

- Image datasets are not duplicated; all processing is metadata-driven  
- Train/test splits are defined via CSV files to prevent data leakage  
- Feature extraction outputs are stored for reuse across experiments  
- Models and scalers are saved and reused for evaluation and testing  
- Results are stored separately for reproducibility and comparison  

---

## Summary

This directory structure supports a modular, reproducible workflow where each stage of the pipeline produces artifacts that are reused in subsequent steps. The separation of datasets, metadata, features, models, and results ensures clarity, scalability, and ease of experimentation.
