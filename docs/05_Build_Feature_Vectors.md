---
title: 05 Build Feature Vectors
parent: "2. Model Description Tutorial"
nav_order: 4
---

# 05 Build Feature Vectors

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/05_Build_Feature_Vectors.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook builds final fixed-length feature vectors for both the **training** and **test** subsets by combining gradient-based, spatial, and frequency-domain feature CSV files into classifier-ready tables.

The result is a structured dataset containing a **25-dimensional DIP feature vector** per image, which serves as input to downstream normalization and classifier training steps.

---

## Inputs

Feature CSV files (from GitHub repository):

* `metadata/features/train_gradient_features.csv`
* `metadata/features/train_spatial_features.csv`
* `metadata/features/train_frequency_features.csv`
* `metadata/features/test_gradient_features.csv`
* `metadata/features/test_spatial_features.csv`
* `metadata/features/test_frequency_features.csv`

Shared configuration:

* `src/project_config.py`

---

## Outputs

The following feature vector files are generated:

* `metadata/vectors/train_feature_vectors.csv`
  Training feature vectors with full feature representation.

* `metadata/vectors/test_feature_vectors.csv`
  Test feature vectors reserved for final evaluation.

Each file includes:

* `filename`
* `class_label`
* `source_dataset`
* `subset`
* 25 DIP feature columns

---

## Main Tasks

* Clone the GitHub repository into the Colab runtime
* Load feature tables from all three feature groups
* Validate alignment across feature CSV files
* Merge feature groups into unified tables
* Verify feature completeness and consistency
* Save final feature vector CSV files

---

## Processing Workflow

This notebook executes a structured sequence of steps to construct the final feature vector datasets:

1. **Environment Setup and Configuration**
   The Colab runtime is prepared, required libraries are imported, and file paths for input feature tables and output vectors are defined.

2. **Feature Data Loading**
   Gradient-based, spatial, and frequency-domain feature CSV files are loaded separately for both training and test subsets.

3. **Data Validation and Alignment Checks**
   Multiple validation steps ensure:

   * Consistent row counts across feature groups
   * Proper alignment of metadata (filenames, labels, datasets)
   * Presence of all required feature columns

4. **Feature Vector Construction**
   Feature groups are combined into unified tables by:

   * Retaining a single set of metadata columns
   * Appending all feature columns in a fixed order
     This results in a consistent 25-dimensional feature vector for each image.

5. **Final Validation**
   The constructed feature vectors are verified for:

   * Correct dimensionality
   * Expected row counts
   * Absence of missing or invalid values

6. **Output Generation**
   Final feature vector tables are saved and briefly inspected to confirm file integrity and expected structure.

---

## Notes and Design Choices

* **Modular feature design:**
  Features are extracted in separate groups and combined here to maintain modularity.

* **Consistent alignment:**
  Strict alignment ensures all features correspond to the correct image samples.

* **Fixed feature dimensionality:**
  Each image is represented by a 25-dimensional feature vector.

* **Metadata preservation:**
  Identifiers such as filename, class label, and dataset source are retained.

* **GitHub-based workflow:**
  All data is sourced from the GitHub repository and processed locally in Colab.

---

## Role in the Overall Pipeline

This notebook produces the final feature representation used as input to the classifier. It serves as the bridge between feature extraction and model preparation.

All subsequent steps operate directly on these feature vector tables.

---

## Next Step

➡️ [06 Normalize and Prepare Inputs](06_Normalize_and_Prepare_Inputs.md)


