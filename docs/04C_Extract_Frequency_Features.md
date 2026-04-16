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

## Inputs

- Training and test metadata:
  - `train_metadata.csv`
  - `test_metadata.csv`

- Preprocessed image files referenced by metadata

- Project configuration file:
  - `project_config.py`

## Outputs

- Frequency feature CSV files:
  - `train_frequency_features.csv`
  - `test_frequency_features.csv`

Each CSV contains:
- `filename`
- `class_label`
- `source_dataset`
- `subset`
- Frequency-domain feature columns

## Main Tasks

- Load training and test metadata
- Read preprocessed images
- Compute frequency-domain representations
- Extract spectral and radial descriptors
- Construct feature tables
- Save frequency feature CSV files

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a summary of frequency feature extraction, including purpose, inputs, and outputs.

### Cell 1: Import Libraries and Configuration
Loads required libraries (e.g., NumPy, OpenCV, SciPy, Pandas) and imports shared configuration settings.

### Cell 2: Load Train and Test Metadata
Reads the training and test metadata files generated in the previous step.

### Cell 3: Define Frequency Feature Functions
Implements functions to compute frequency-domain representations using transforms such as the Fourier Transform and to derive spectral descriptors.

### Cell 4: Extract Frequency Features
Processes each image to compute frequency-domain descriptors that capture spectral energy distribution, structural patterns, and frequency complexity.

The following eight frequency-domain features are extracted:

- **Low Frequency Energy Ratio**  
  Represents the proportion of spectral energy in low-frequency components, corresponding to smooth regions and gradual intensity changes.

- **High Frequency Energy Ratio**  
  Represents the proportion of spectral energy in high-frequency components, corresponding to edges, fine details, and noise-like structures.

- **Radial Mean**  
  Computes the average spectral magnitude as a function of distance from the center of the frequency spectrum.

- **Radial Standard Deviation**  
  Measures the variability of spectral magnitude across radial distances.

- **Radial Entropy**  
  Quantifies the randomness of the radial frequency distribution.

- **Spectral Centroid**  
  Represents the center of mass of the frequency spectrum, indicating whether energy is concentrated in lower or higher frequencies.

- **Spectral Bandwidth**  
  Measures the spread of frequency energy around the centroid.

- **Log Spectrum Standard Deviation**  
  Captures variation in the log-transformed spectrum, emphasizing relative differences in spectral magnitude.

### Cell 5: Build Feature Tables
Constructs structured DataFrames containing metadata and extracted frequency features.

### Cell 6: Validate Feature Tables
Verifies:
- Correct number of rows
- Presence of all expected feature columns
- Consistency between metadata and feature values

### Cell 7: Save Frequency Feature CSV Files
Writes training and test frequency feature tables to CSV files for downstream processing.

## Notes and Design Choices

- **Frequency-domain analysis:**  
  Fourier-based representations capture structural patterns not easily observable in the spatial domain.

- **Energy distribution:**  
  Energy ratios across frequency bands provide insight into image smoothness and detail.

- **Radial statistics:**  
  Radial features summarize frequency content as a function of distance from the spectrum center.

- **Spectral descriptors:**  
  Measures such as centroid and bandwidth characterize the overall distribution of frequency energy.

- **Complementary feature group:**  
  Frequency features complete the DIP feature vector by adding information not captured by gradient or spatial features.

## Files Produced

- `train_frequency_features.csv` — Frequency features for training set
- `test_frequency_features.csv` — Frequency features for test set

## Role in the Overall Pipeline

This notebook produces the final group of features used in the DIP feature vector. These features are combined with gradient and spatial features in the next step to form the complete input representation for classifier training.

## Next Step

➡️ [05 Build Feature Vectors](05_Build_Feature_Vectors.md)


