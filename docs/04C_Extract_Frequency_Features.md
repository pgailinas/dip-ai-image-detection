---
title: 04C Extract Frequency Features
parent: 2. Model Description Tutorial
nav_order: 3
---

# 04C Extract Frequency Features

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/04C_Extract_Frequency_Features.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook extracts frequency-domain features from preprocessed images. These features capture spectral characteristics such as energy distribution across frequency bands and structural patterns in the frequency domain.

Frequency-domain descriptors form the third group of the 26-dimensional DIP feature vector used for classification.

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

The following frequency feature datasets are generated:

* `train_frequency_features.csv`
  Frequency-domain features for the training dataset.

* `test_frequency_features.csv`
  Frequency-domain features for the test dataset.

Each dataset includes:

* `filename`
* `class_label`
* `source_dataset`
* `subset`
* Frequency-domain feature columns

---

## Main Tasks

* Load training and test metadata
* Read preprocessed images
* Compute frequency-domain representations
* Extract spectral and radial descriptors
* Construct feature tables
* Save frequency feature CSV files

---

## Processing Workflow

This notebook executes a structured sequence of steps to extract frequency-domain image features:

1. **Environment Setup and Data Loading**
   The runtime environment is initialized, required libraries are imported, and training and test metadata are loaded.

2. **Image Access and Preparation**
   Preprocessed images are accessed using metadata references to ensure consistent input data.

3. **Frequency-Domain Transformation**
   Images are transformed into the frequency domain using techniques such as the Fourier Transform to obtain spectral representations.

4. **Feature Extraction**
   Statistical descriptors are derived from the frequency spectrum to capture energy distribution, structural patterns, and frequency complexity.

5. **Feature Table Construction**
   Extracted features are combined with metadata to form structured datasets for both training and test subsets.

6. **Validation and Output Generation**
   Feature tables are validated for completeness and consistency, then saved for downstream processing.

---

## Frequency Feature Definitions

The following frequency-domain features are extracted:

* **Low Frequency Energy Ratio**
  Represents the proportion of spectral energy in low-frequency components.

* **High Frequency Energy Ratio**
  Represents the proportion of spectral energy in high-frequency components.

* **Radial Mean**
  Computes average spectral magnitude as a function of radial distance.

* **Radial Standard Deviation**
  Measures variability of spectral magnitude across radial distances.

* **Radial Entropy**
  Quantifies randomness in radial frequency distribution.

* **Spectral Centroid**
  Indicates where energy is concentrated in the frequency spectrum.

* **Spectral Bandwidth**
  Measures spread of frequency energy around the centroid.

* **Log Spectrum Standard Deviation**
  Captures variation in the log-transformed spectrum.

---

## Notes and Design Choices

* **Frequency-domain analysis:**
  Fourier-based representations capture structural patterns not easily observable in the spatial domain.

* **Energy distribution:**
  Energy ratios across frequency bands provide insight into image smoothness and detail.

* **Radial statistics:**
  Radial features summarize frequency content as a function of distance from the spectrum center.

* **Spectral descriptors:**
  Measures such as centroid and bandwidth characterize the overall distribution of frequency energy.

* **Complementary feature group:**
  Frequency features complete the DIP feature vector by adding information not captured by gradient or spatial features.

---

## Role in the Overall Pipeline

This notebook produces the final group of features used in the DIP feature vector. These features are combined with gradient and spatial features in the next step to form the complete input representation for classifier training.

---

## Next Step

➡️ [05 Build Feature Vectors](05_Build_Feature_Vectors.md)



