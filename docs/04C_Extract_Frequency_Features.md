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

* Metadata from the GitHub repository:

  * `metadata/splits/train_metadata.csv`
  * `metadata/splits/test_metadata.csv`

* Preprocessed image archive from Google Drive:

  * `/content/drive/MyDrive/DIP_Project/releases/preprocessed/All_Sources_preprocessed.zip`

* Project configuration file:

  * `src/project_config.py`

---

## Outputs

The following frequency feature datasets are generated under `metadata/features/`:

* `metadata/features/train_frequency_features.csv`
* `metadata/features/test_frequency_features.csv`

Each dataset includes:

* `filename`
* `class_label`
* `source_dataset`
* `subset`
* Frequency-domain feature columns

⚠️ These files are written to the Colab runtime environment and are **not automatically persisted to Google Drive**.

---

## Main Tasks

* Select subset to process (`train` or `test`)
* Load subset metadata
* Extract preprocessed images from ZIP (if needed)
* Read images using metadata references
* Compute frequency-domain representations
* Extract spectral and radial descriptors
* Construct feature tables
* Save frequency feature CSV files

---

## Processing Workflow

This notebook executes a structured sequence of steps:

1. **Environment Setup and Input Verification**  
   The runtime environment is initialized, the repository is cloned, Google Drive is mounted, and required inputs are verified.

2. **Image Extraction (if needed)**  
   The preprocessed image archive is extracted into the local runtime. Images are stored in a **flat directory structure** with no subdirectories.

3. **Subset Selection and Metadata Loading**  
   A single subset (`train` or `test`) is selected via `SUBSET_NAME` and loaded.

4. **Image Access**  
   Image paths are constructed directly from filenames in metadata.

5. **Frequency-Domain Transformation**  
   Images are transformed into the frequency domain using the 2D Fourier Transform to obtain spectral representations.

6. **Feature Extraction**  
   Statistical descriptors are derived from the frequency spectrum to capture energy distribution, structural patterns, and spectral complexity.

7. **Feature Table Construction**  
   Extracted features are combined with metadata to form a structured dataset.

8. **Validation and Output Generation**  
   Feature tables are validated and saved for downstream processing.

---

## Frequency Feature Definitions

The following frequency-domain features are extracted:

* **Low Frequency Energy Ratio**  
  Represents the proportion of spectral energy in low-frequency components.

* **High Frequency Energy Ratio**  
  Represents the proportion of spectral energy in high-frequency components.

* **Radial Mean**  
  Computes average spectral magnitude as a function of radial distance.

* **Radial Std**  
  Measures variability of spectral magnitude across radial distances.

* **Radial Entropy**  
  Quantifies randomness in radial frequency distribution.

* **Spectral Centroid**  
  Indicates where energy is concentrated in the frequency spectrum.

* **Spectral Bandwidth**  
  Measures spread of frequency energy around the centroid.

* **Log Spectrum Std**  
  Captures variation in the log-transformed spectrum.

---

## Notes and Design Choices

* **Flat image structure:**  
  All 18,000 images are stored in a single directory and accessed by filename.

* **Metadata-driven processing:**  
  Dataset membership is determined entirely from metadata, not directory structure.

* **Subset-based execution:**  
  The notebook processes **one subset per run** using `SUBSET_NAME`.

* **Frequency-domain analysis:**  
  Fourier-based representations capture structural patterns not easily observable in the spatial domain.

* **Energy distribution:**  
  Frequency energy ratios provide insight into image smoothness and fine detail.

* **Radial statistics:**  
  Radial features summarize frequency content as a function of distance from the spectrum center.

* **Spectral descriptors:**  
  Centroid and bandwidth characterize the overall distribution of frequency energy.

* **Modular feature design:**  
  Frequency features complement gradient and spatial feature groups.

---

## Role in the Overall Pipeline

This notebook produces the **frequency-domain feature group (8 features)** used in the DIP feature vector.

These features are combined with:

* Gradient features (04A)
* Spatial features (04B)

to form the complete 26-dimensional feature representation used for classification.

---

## Next Step

Run this notebook twice:

1. Set `SUBSET_NAME = TRAIN_SUBSET`
2. Set `SUBSET_NAME = TEST_SUBSET`

Then proceed to:

➡️ [05 Build Feature Vectors](05_Build_Feature_Vectors.md)

