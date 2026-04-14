---
title: 04A Extract Gradient Features
nav_order: 4
---

# 04A Extract Gradient Features

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/04A_Extract_Gradient_Features.ipynb)

---

## Purpose

This notebook extracts gradient-based features from preprocessed images. These features capture edge structure, directional information, and local intensity variations, which are useful for distinguishing real images from AI-generated images.

Gradient-based descriptors form the first group of the 26-dimensional DIP feature vector used for classification.

## Inputs

- Training and test metadata:
  - `train_metadata.csv`
  - `test_metadata.csv`

- Preprocessed image files referenced by metadata

- Project configuration file:
  - `project_config.py`

## Outputs

- Gradient feature CSV files:
  - `train_gradient_features.csv`
  - `test_gradient_features.csv`

Each CSV contains:
- `filename`
- `class_label`
- `source_dataset`
- `subset`
- Gradient-based feature columns

## Main Tasks

- Load training and test metadata
- Read preprocessed images
- Compute gradient magnitude and orientation
- Extract statistical descriptors from gradient data
- Construct feature tables
- Save gradient feature CSV files

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a summary of gradient feature extraction, including purpose, inputs, and outputs.

### Cell 1: Import Libraries and Configuration
Loads required libraries (e.g., NumPy, OpenCV, Pandas) and imports shared configuration settings.

### Cell 2: Load Train and Test Metadata
Reads the training and test metadata files generated in the previous step.

### Cell 3: Define Gradient Computation Functions
Implements functions to compute gradient magnitude and orientation using image derivatives.

### Cell 4: Extract Gradient Features
Processes each image to compute gradient-based descriptors that capture edge strength, structural variation, and directional patterns.

The following eight features are extracted:

- **Mean Gradient Magnitude**  
  Represents the average strength of edges in the image. Higher values indicate stronger overall edge presence and more pronounced structural detail.

- **Standard Deviation of Gradient Magnitude**  
  Measures variability in edge strength. High values suggest a mix of strong and weak edges, indicating complex textures or heterogeneous regions.

- **Maximum Gradient Magnitude**  
  Captures the strongest edge response in the image. This reflects the presence of sharp transitions or highly defined boundaries.

- **Gradient Entropy**  
  Quantifies the randomness or complexity of gradient magnitudes. Higher entropy indicates more diverse edge strengths, while lower entropy suggests more uniform structure.

- **Edge Density**  
  Represents the proportion of pixels classified as edges. This provides a measure of how densely edges are distributed across the image.

- **Orientation Mean**  
  Computes the average direction of gradients. This reflects dominant structural orientation within the image.

- **Orientation Standard Deviation**  
  Measures the spread of gradient directions. Low values indicate consistent directional structure, while high values suggest more varied or chaotic orientations.

- **Orientation Entropy**  
  Quantifies the randomness of gradient directions. Higher entropy indicates a wide variety of edge orientations, while lower entropy suggests more uniform directional patterns.

### Cell 5: Build Feature Tables
Constructs structured DataFrames containing metadata and extracted gradient features.

### Cell 6: Validate Feature Tables
Verifies:
- Correct number of rows
- Presence of all expected feature columns
- Consistency between metadata and feature values

### Cell 7: Save Gradient Feature CSV Files
Writes training and test gradient feature tables to CSV files for downstream processing.

## Notes and Design Choices

- **Edge-focused representation:**  
  Gradient features emphasize structural content such as edges and contours, which often differ between real and AI-generated images.

- **Orientation analysis:**  
  Gradient direction statistics provide additional discriminatory information beyond magnitude alone.

- **Entropy measures:**  
  Entropy captures the complexity and variability of gradient distributions.

- **Separation of feature groups:**  
  Gradient features are computed independently to support modular design and easier analysis of feature contributions.

## Files Produced

- `train_gradient_features.csv` — Gradient features for training set
- `test_gradient_features.csv` — Gradient features for test set

## Role in the Overall Pipeline

This notebook produces the first group of features used in the DIP feature vector. These features are later combined with spatial and frequency-domain features to form the complete input representation for classifier training.

## Next Step

➡️ [04B Extract Spatial Features Images](04B_Extract_Spatial_Features.md)


