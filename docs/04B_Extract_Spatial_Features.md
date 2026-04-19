---
title: 04B Extract Spatial Features
parent: 2. Model Description Tutorial
nav_order: 2
---

# 04B Extract Spatial Features

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/04B_Extract_Spatial_Features.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook extracts spatial-domain features from preprocessed images. These features capture intensity distribution, local variability, and structural complexity within the image, providing complementary information to gradient-based descriptors.

Spatial features form the second group of the 26-dimensional DIP feature vector used for classification.

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

The following spatial feature datasets are generated:

* `train_spatial_features.csv`
  Spatial features for the training dataset.

* `test_spatial_features.csv`
  Spatial features for the test dataset.

Each dataset includes:

* `filename`
* `class_label`
* `source_dataset`
* `subset`
* Spatial feature columns

---

## Main Tasks

* Load training and test metadata
* Read preprocessed images
* Compute global and local intensity statistics
* Extract entropy-based and variance-based descriptors
* Construct feature tables
* Save spatial feature CSV files

---

## Processing Workflow

This notebook executes a structured sequence of steps to extract spatial-domain image features:

1. **Environment Setup and Data Loading**
   The runtime environment is initialized, required libraries are imported, and training and test metadata are loaded.

2. **Image Access and Preparation**
   Preprocessed images are accessed using metadata references to ensure consistent input data.

3. **Spatial Feature Computation**
   Image intensity data is analyzed to compute:

   * Global intensity statistics
   * Local entropy measures
   * Variance-based texture descriptors

4. **Feature Extraction**
   Statistical descriptors are derived to capture brightness, contrast, texture variability, and structural complexity.

5. **Feature Table Construction**
   Extracted features are combined with metadata to form structured datasets for both training and test subsets.

6. **Validation and Output Generation**
   Feature tables are validated for completeness and consistency, then saved for downstream processing.

---

## Spatial Feature Definitions

The following spatial-domain features are extracted:

* **Global Entropy**
  Measures the overall randomness of pixel intensities.

* **Local Entropy Mean**
  Captures average texture complexity across local regions.

* **Local Entropy Standard Deviation**
  Measures variability of local entropy across the image.

* **Intensity Mean**
  Represents average pixel brightness.

* **Intensity Standard Deviation**
  Measures contrast and intensity variation.

* **Laplacian Variance**
  Quantifies image sharpness and fine detail.

* **Patch Variance Mean**
  Captures average local intensity variation.

* **Patch Variance Standard Deviation**
  Measures variability of local texture strength.

---

## Notes and Design Choices

* **Intensity-based representation:**
  Spatial features describe the distribution of pixel intensities across the image.

* **Local vs global structure:**
  Both global statistics and localized measures are used to capture fine-grained texture differences.

* **Laplacian variance:**
  Serves as a measure of image sharpness and detail, which may differ between real and generated images.

* **Complementary feature group:**
  Spatial features are designed to complement gradient and frequency-domain descriptors in the overall feature vector.

---

## Role in the Overall Pipeline

This notebook produces the second group of features used in the DIP feature vector. These features are later combined with gradient and frequency-domain features to form the complete classifier input representation.

---

## Next Step

➡️ [04C Extract Frequency Features](04C_Extract_Frequency_Features.md)



