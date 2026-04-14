---
title: 04B Extract Spatial Features
nav_order: 5
---

# 04B Extract Spatial Features

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/04B_Extract_Spatial_Features.ipynb)

---

## Purpose

This notebook extracts spatial-domain features from preprocessed images. These features capture intensity distribution, local variability, and structural complexity within the image, providing complementary information to gradient-based descriptors.

Spatial features form the second group of the 26-dimensional DIP feature vector used for classification.

## Inputs

- Training and test metadata:
  - `train_metadata.csv`
  - `test_metadata.csv`

- Preprocessed image files referenced by metadata

- Project configuration file:
  - `project_config.py`

## Outputs

- Spatial feature CSV files:
  - `train_spatial_features.csv`
  - `test_spatial_features.csv`

Each CSV contains:
- `filename`
- `class_label`
- `source_dataset`
- `subset`
- Spatial feature columns

## Main Tasks

- Load training and test metadata
- Read preprocessed images
- Compute global and local intensity statistics
- Extract entropy-based and variance-based descriptors
- Construct feature tables
- Save spatial feature CSV files

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a summary of spatial feature extraction, including purpose, inputs, and outputs.

### Cell 1: Import Libraries and Configuration
Loads required libraries (e.g., NumPy, OpenCV, Pandas) and imports shared configuration settings.

### Cell 2: Load Train and Test Metadata
Reads the training and test metadata files generated in the previous step.

### Cell 3: Define Spatial Feature Functions
Implements functions to compute spatial-domain descriptors such as intensity statistics, entropy measures, and local variance.

### Cell 4: Extract Spatial Features
Processes each image to compute spatial-domain descriptors that capture intensity distribution, texture variation, and structural complexity.

The following nine features are extracted:

- **Global Entropy**  
  Measures the overall randomness of pixel intensities in the image. Higher entropy indicates greater complexity and variability, while lower entropy suggests more uniform or smooth regions.

- **Local Entropy Mean**  
  Computes the average entropy across local neighborhoods within the image. This captures typical texture complexity at a localized level.

- **Local Entropy Standard Deviation**  
  Measures the variability of local entropy across the image. High values indicate uneven texture distribution, with both simple and complex regions present.

- **Intensity Mean**  
  Represents the average pixel intensity of the image. This reflects overall brightness and can differ between datasets due to generation or capture processes.

- **Intensity Standard Deviation**  
  Measures the spread of pixel intensities. Higher values indicate greater contrast, while lower values suggest more uniform intensity levels.

- **Laplacian Variance**  
  Quantifies the variance of the Laplacian (second-order derivative) of the image. This serves as a measure of sharpness and fine detail, with higher values indicating more high-frequency content.

- **Patch Variance Mean**  
  Computes the average variance of small image patches. This captures typical local intensity variation and texture strength.

- **Patch Variance Standard Deviation**  
  Measures how much patch variance varies across the image. High values indicate regions with differing texture intensity.

### Cell 5: Build Feature Tables
Constructs structured DataFrames containing metadata and extracted spatial features.

### Cell 6: Validate Feature Tables
Verifies:
- Correct number of rows
- Presence of all expected feature columns
- Consistency between metadata and feature values

### Cell 7: Save Spatial Feature CSV Files
Writes training and test spatial feature tables to CSV files for downstream processing.

## Notes and Design Choices

- **Intensity-based representation:**  
  Spatial features describe the distribution of pixel intensities across the image.

- **Local vs global structure:**  
  Both global statistics and localized measures (e.g., patch variance, local entropy) are used to capture fine-grained texture differences.

- **Laplacian variance:**  
  Serves as a measure of image sharpness and detail, which may differ between real and generated images.

- **Complementary feature group:**  
  Spatial features are designed to complement gradient and frequency-domain descriptors in the overall feature vector.

## Files Produced

- `train_spatial_features.csv` — Spatial features for training set
- `test_spatial_features.csv` — Spatial features for test set

## Role in the Overall Pipeline

This notebook produces the second group of features used in the DIP feature vector. These features are later combined with gradient and frequency-domain features to form the complete classifier input representation.

## Next Step

➡️ [04C Extract Frequency Features](04C_Extract_Frequency_Features.md)


