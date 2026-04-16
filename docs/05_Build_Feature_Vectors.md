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

* `metadata/vectors/train_feature_vectors.csv`
* `metadata/vectors/test_feature_vectors.csv`

Each CSV contains:

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

## Cell-by-Cell Description

### Cell 0: Notebook Overview

Provides a high-level description of feature vector construction, including purpose, inputs, and outputs.

---

### Cell 1: Imports

* Import required libraries for:

  * file handling
  * CSV loading
  * validation
  * feature-vector construction

---

### Cell 2: Define Input and Output Paths

* Define local runtime paths for:

  * input feature CSVs (`metadata/features`)
  * output feature vectors (`metadata/vectors`)
* Define expected row counts for training and test subsets

---

### Cell 3: Load Feature CSVs

* Load gradient, spatial, and frequency feature CSV files for:

  * training subset
  * test subset

---

### Cell 4: Validate Row Counts and Alignment

For each subset:

* Confirm expected row counts
* Confirm feature tables align by length

---

### Cell 5: Define Metadata and Feature Columns

* Define:

  * metadata column list
  * gradient feature columns
  * spatial feature columns
  * frequency feature columns

---

### Cell 6: Verify Required Columns Exist

* Confirm that all expected metadata and feature columns are present

---

### Cell 7: Verify Metadata Alignment Across CSVs

* Confirm metadata columns match across feature groups
* Confirm filenames align row-by-row

---

### Cell 8: Verify Subset Labels

* Confirm training rows are labeled `train`
* Confirm test rows are labeled `test`

---

### Cell 9: Build Feature Vectors

For both training and test subsets:

* Retain one copy of metadata columns
* Append:

  * gradient-based features
  * spatial features
  * frequency-domain features

---

### Cell 10: Validate Feature Vectors

* Confirm final row counts
* Confirm feature counts (25 total)
* Confirm no unexpected missing values

---

### Cell 11: Save Feature Vectors

* Save:

  * `train_feature_vectors.csv`
  * `test_feature_vectors.csv`

---

### Cell 12: Quick Sanity Check

* Reload or inspect saved outputs
* Confirm file integrity and expected shapes

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

## Files Produced

* `train_feature_vectors.csv` — Training feature vectors
* `test_feature_vectors.csv` — Test feature vectors

---

## Role in the Overall Pipeline

This notebook produces the final feature representation used as input to the classifier. It serves as the bridge between feature extraction and model preparation.

All subsequent steps operate directly on these feature vector tables.

---

## Next Step

➡️ [06 Normalize and Prepare Inputs](06_Normalize_and_Prepare_Inputs.md)

