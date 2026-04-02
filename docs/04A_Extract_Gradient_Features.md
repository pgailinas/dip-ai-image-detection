# 04 Extract Features

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/04_Extract_Features.ipynb)

---

## Overview

This stage extracts handcrafted Digital Image Processing (DIP) features from training images to form the basis of the classification model.

Feature extraction is divided into three domains:

* Gradient-Based
* Spatial
* Frequency-Domain

---

## Objectives

* Load training dataset metadata
* Access preprocessed images
* Extract domain-specific features
* Store features in structured CSV files
* Validate feature outputs

---

## Workflow

1. Load training metadata
2. Access image directory
3. Perform sanity checks
4. Extract features (per domain)
5. Save feature CSVs
6. Validate outputs

---

## Notebook Structure

### Cell 0 — Overview

Defines feature extraction goals and outputs. 

### Cell 1 — Imports

Loads required libraries for image processing and analysis. 

### Cell 2 — Load Training Metadata

Loads `train_metadata.csv` and verifies dataset size (8400). 

### Cell 3 — Image Access Setup

Defines image directory (`/content/images`) and access methods. 

### Cell 4 — Sample Image Selection

Selects sample images for sanity checks and visualization. 

---

## Gradient Feature Extraction

### Cell 5 — Gradient Setup

Prepares gradient computation (Sobel/Scharr filters). 

### Cell 6 — Compute Gradient Features

Calculates:

* Mean Gradient
* Std Gradient
* Max Gradient
* Gradient Entropy
* Edge Density
* Orientation statistics 

### Cell 7 — Save Gradient Features

Writes `train_gradient_features.csv`. 

---

## Spatial Feature Extraction

### Cell 8 — Spatial Setup

Prepares entropy, variance, and Laplacian calculations. 

### Cell 9 — Compute Spatial Features

Calculates:

* Global entropy
* Local entropy (mean/std)
* Intensity statistics
* Laplacian variance
* Patch variance
* Noise residual energy 

### Cell 10 — Save Spatial Features

Writes `train_spatial_features.csv`. 

---

## Frequency Feature Extraction

### Cell 11 — Frequency Setup

Prepares FFT computation and spectrum generation. 

### Cell 12 — Compute Frequency Features

Calculates:

* Frequency energy ratios
* Radial statistics
* Spectral centroid
* Spectral bandwidth
* Log spectrum statistics 

### Cell 13 — Save Frequency Features

Writes `train_frequency_features.csv`. 

---

## Validation and Checks

### Cell 14 — Output Verification

Confirms correct row counts (8400) and CSV integrity. 

### Cell 15 — Feature Distribution Checks

Compares distributions (AI vs Real). 

### Cell 16 — Visual Sanity Check

Displays selected images and feature behavior. 

---

## Outputs

* train_gradient_features.csv
* train_spatial_features.csv
* train_frequency_features.csv

---

## Key Design Features

* Domain-specific feature extraction
* Modular pipeline (separate feature groups)
* Optimized computations
* Reusable CSV outputs

---

## Next Step

➡️ **05 Build Feature Vectors**


