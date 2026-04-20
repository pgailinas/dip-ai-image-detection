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

* Metadata from the GitHub repository:

  * `metadata/splits/train_metadata.csv`
  * `metadata/splits/test_metadata.csv`

* Preprocessed image archive from Google Drive:

  * `/content/drive/MyDrive/DIP_Project/releases/preprocessed/All_Sources_preprocessed.zip`

* Project configuration file:

  * `src/project_config.py`

---

## Outputs

The following spatial feature datasets are generated in the **local runtime**:

* `metadata/features/train_spatial_features.csv`
* `metadata/features/test_spatial_features.csv`

Each dataset includes:

* `filename`
* `class_label`
* `source_dataset`
* `subset`
* Spatial feature columns

⚠️ These files are stored in local runtime storage only and are **not automatically saved to Google Drive**.

---

## Main Tasks

* Load subset metadata (train or test)
* Extract preprocessed images from ZIP (if needed)
* Read images using metadata references
* Compute spatial-domain statistics
* Extract entropy, variance, and intensity descriptors
* Construct feature tables
* Save spatial feature CSV files

---

## Processing Workflow

This notebook executes a structured sequence of steps:

1. **Environment Setup and Input Verification**  
   The runtime environment is initialized, the repository is cloned, Google Drive is mounted, and required inputs are verified.

2. **Image Extraction (if needed)**  
   The preprocessed image archive is extracted into the local runtime. Images are stored in a **flat directory structure** with no subdirectories.

3. **Metadata Loading**  
   A single subset (`train` or `test`) is loaded based on the `SUBSET_NAME` setting.

4. **Image Access**  
   Image paths are constructed directly from filenames in metadata.

5. **Spatial Feature Computation**  
   Image intensity data is analyzed to compute:

   * Global intensity statistics  
   * Local entropy maps  
   * Variance-based texture descriptors  
   * Noise residual characteristics  

6. **Feature Extraction**  
   Statistical descriptors are derived to capture brightness, contrast, texture variability, and structural complexity.

7. **Feature Table Construction**  
   Extracted features are combined with metadata to form a structured dataset.

8. **Validation and Output Generation**  
   Feature tables are validated and saved for downstream processing.

---

## Spatial Feature Definitions

The following spatial-domain features are extracted:

* **Global Entropy**  
  Measures the overall randomness of pixel intensities.

* **Local Entropy Mean**  
  Captures average texture complexity across local regions.

* **Local Entropy Std**  
  Measures variability of local entropy across the image.

* **Intensity Mean**  
  Represents average pixel brightness.

* **Intensity Std**  
  Measures contrast and intensity variation.

* **Laplacian Variance**  
  Quantifies image sharpness and fine detail.

* **Patch Variance Mean**  
  Captures average local intensity variation.

* **Patch Variance Std**  
  Measures variability of local texture strength.

* **Noise Residual Energy**  
  Measures high-frequency residual energy after smoothing, capturing fine-grained noise characteristics.

---

## Notes and Design Choices

* **Flat image structure:**  
  All 18,000 images are stored in a single directory and accessed by filename, simplifying data handling.

* **Metadata-driven processing:**  
  Dataset membership is determined entirely from metadata, not directory structure.

* **Intensity-based representation:**  
  Spatial features describe the distribution of pixel intensities across the image.

* **Local vs global structure:**  
  Both global statistics and localized measures are used to capture fine-grained texture differences.

* **Noise modeling:**  
  Noise residual energy provides additional discriminatory information between real and AI-generated images.

* **Modular feature design:**  
  Spatial features are computed independently from gradient and frequency features.

* **Subset-based execution:**  
  The notebook processes one subset per run (`train` or `test`) to preserve strict separation.

---

## Role in the Overall Pipeline

This notebook produces the **spatial feature group (9 features)** used in the DIP feature vector.

These features are later combined with:

* Gradient features (04A)
* Frequency-domain features (04C)

to form the complete 26-dimensional feature representation used for classification.

---

## Next Step

Run this notebook twice:

1. Set `SUBSET_NAME = TRAIN_SUBSET`
2. Set `SUBSET_NAME = TEST_SUBSET`

Then proceed to:

➡️ [04C Extract Frequency Features](04C_Extract_Frequency_Features.md)



