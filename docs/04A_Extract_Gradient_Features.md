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

* Metadata from the GitHub repository:

  * `metadata/splits/train_metadata.csv`
  * `metadata/splits/test_metadata.csv`

* Preprocessed image archive from Google Drive:

  * `/content/drive/MyDrive/DIP_Project/releases/preprocessed/All_Sources_preprocessed.zip`

* Project configuration file:

  * `src/project_config.py`

---

## Outputs

The following gradient feature datasets are generated under `metadata/features/`:

* `metadata/features/train_gradient_features.csv`
* `metadata/features/test_gradient_features.csv`

Each dataset includes:

* `filename`
* `class_label`
* `source_dataset`
* `subset`
* Gradient-based feature columns

⚠️ These files are written to the Colab runtime environment and are **not automatically persisted to Google Drive**.

---

## Main Tasks

* Select subset to process (`train` or `test`)
* Load subset metadata
* Extract preprocessed images from ZIP (if needed)
* Read images using metadata references
* Compute gradient magnitude and orientation
* Extract statistical descriptors from gradient data
* Construct feature tables
* Save gradient feature CSV files

---

## Processing Workflow

This notebook executes a structured sequence of steps:

1. **Environment Setup and Input Verification**  
   The runtime environment is initialized, the repository is cloned, Google Drive is mounted, and required inputs are verified.

2. **Image Extraction (if needed)**  
   The preprocessed image archive is extracted into the local runtime. Images are stored in a **flat directory structure** with no subfolders.

3. **Subset Selection and Metadata Loading**  
   A single subset (`train` or `test`) is selected via `SUBSET_NAME` and loaded.

4. **Image Access**  
   Image paths are constructed directly from filenames in metadata.

5. **Gradient Computation**  
   Image gradients are computed using Sobel operators to obtain:

   * Gradient magnitude (edge strength)
   * Gradient orientation (edge direction)

6. **Feature Extraction**  
   Statistical descriptors are derived from gradient data to capture structural characteristics.

7. **Feature Table Construction**  
   Extracted features are combined with metadata to form a structured dataset.

8. **Validation and Output Generation**  
   Feature tables are validated and saved for downstream processing.

---

## Gradient Feature Definitions

The following eight features are extracted:

* **Mean Gradient**  
  Represents the average strength of edges in the image.

* **Std Gradient**  
  Measures variability in edge strength across the image.

* **Max Gradient**  
  Captures the strongest edge response.

* **Gradient Entropy**  
  Quantifies the complexity of gradient magnitude distribution.

* **Edge Density**  
  Represents the proportion of pixels classified as edges.

* **Orientation Mean**  
  Computes the average direction of gradients.

* **Orientation Std**  
  Measures variability in gradient directions.

* **Orientation Entropy**  
  Quantifies the randomness of gradient orientations.

---

## Notes and Design Choices

* **Flat image structure:**  
  All 18,000 images are stored in a single directory and accessed by filename.

* **Metadata-driven processing:**  
  Dataset membership is determined entirely from metadata, not directory structure.

* **Subset-based execution:**  
  The notebook processes **one subset per run** using `SUBSET_NAME`.

* **Edge-focused representation:**  
  Gradient features emphasize structural content such as edges and contours.

* **Entropy measures:**  
  Capture complexity and variability in gradient distributions.

* **Modular feature design:**  
  Gradient features are computed independently from spatial and frequency features.

---

## Role in the Overall Pipeline

This notebook produces the **gradient feature group (8 features)** used in the DIP feature vector.

These features are later combined with:

* Spatial features (04B)
* Frequency-domain features (04C)

to form the complete 26-dimensional feature vector.

---

## Next Step

Run this notebook twice:

1. Set `SUBSET_NAME = TRAIN_SUBSET`
2. Set `SUBSET_NAME = TEST_SUBSET`

Then proceed to:

➡️ [04B Extract Spatial Features](04B_Extract_Spatial_Features.md)

