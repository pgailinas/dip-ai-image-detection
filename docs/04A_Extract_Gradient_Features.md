---
title: 04A Extract Gradient Features
parent: 2. Model Description Tutorial
nav_order: 1
---

# 04A Extract Gradient Features

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/04A_Extract_Gradient_Features.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook extracts gradient-based features from preprocessed images. These features capture edge structure, directional information, and local intensity variations, which are useful for distinguishing real images from AI-generated images.

Gradient-based descriptors form the first group of the 26-dimensional DIP feature vector used for classification.

---

## Inputs

* Training and test metadata:

  * `train_metadata.csv`
  * `test_metadata.csv`

* Preprocessed image files referenced by metadata

* Project configuration file:

  * `project_config.py`

---

## Outputs

The following gradient feature datasets are generated:

* `train_gradient_features.csv`
  Gradient features for the training dataset.

* `test_gradient_features.csv`
  Gradient features for the test dataset.

Each dataset includes:

* `filename`
* `class_label`
* `source_dataset`
* `subset`
* Gradient-based feature columns

---

## Main Tasks

* Load training and test metadata
* Read preprocessed images
* Compute gradient magnitude and orientation
* Extract statistical descriptors from gradient data
* Construct feature tables
* Save gradient feature CSV files

---

## Processing Workflow

This notebook executes a structured sequence of steps to extract gradient-based image features:

1. **Environment Setup and Data Loading**
   The runtime environment is initialized, required libraries are imported, and training and test metadata are loaded.

2. **Image Access and Preparation**
   Preprocessed images are accessed using metadata references, ensuring consistent input data across all samples.

3. **Gradient Computation**
   Image gradients are computed using spatial derivatives to obtain:

   * Gradient magnitude (edge strength)
   * Gradient orientation (edge direction)

4. **Feature Extraction**
   Statistical descriptors are derived from gradient data to capture structural characteristics of each image.

5. **Feature Table Construction**
   Extracted features are combined with metadata to form structured feature tables for both training and test datasets.

6. **Validation and Output Generation**
   Feature tables are validated for consistency and completeness, then saved for downstream processing.

---

## Gradient Feature Definitions

The following eight features are extracted:

* **Mean Gradient Magnitude**
  Represents the average strength of edges in the image.

* **Standard Deviation of Gradient Magnitude**
  Measures variability in edge strength across the image.

* **Maximum Gradient Magnitude**
  Captures the strongest edge response.

* **Gradient Entropy**
  Quantifies the randomness or complexity of gradient magnitudes.

* **Edge Density**
  Represents the proportion of pixels classified as edges.

* **Orientation Mean**
  Computes the average direction of gradients.

* **Orientation Standard Deviation**
  Measures variability in gradient directions.

* **Orientation Entropy**
  Quantifies the randomness of gradient orientations.

---

## Notes and Design Choices

* **Edge-focused representation:**
  Gradient features emphasize structural content such as edges and contours, which often differ between real and AI-generated images.

* **Orientation analysis:**
  Gradient direction statistics provide additional discriminatory information beyond magnitude alone.

* **Entropy measures:**
  Entropy captures the complexity and variability of gradient distributions.

* **Separation of feature groups:**
  Gradient features are computed independently to support modular design and easier analysis of feature contributions.

---

## Role in the Overall Pipeline

This notebook produces the first group of features used in the DIP feature vector. These features are later combined with spatial and frequency-domain features to form the complete input representation for classifier training.

---

## Next Step

➡️ [04B Extract Spatial Features](04B_Extract_Spatial_Features.md)



