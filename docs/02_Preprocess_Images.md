---
title: 02 Preprocess Images
parent: 1. Dataset Tutorial
nav_order: 2
---

# 02 Preprocess Images

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/02_Preprocess_Images.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook performs image preprocessing for all dataset sources defined in the previous step. It standardizes image format, size, and quality to ensure consistency across all inputs prior to feature extraction.

Preprocessing is applied uniformly to both real and AI-generated images, enabling fair and comparable feature computation in later stages.

---

## Inputs

* Metadata CSV files from dataset construction:

  * `imgn_metadata.csv`
  * `coco_metadata.csv`
  * `open_metadata.csv`
  * `diff_metadata.csv`
  * `sdxl_metadata.csv`
  * `mj_metadata.csv`

* Raw image files referenced by metadata

* Project configuration file:

  * `project_config.py`

---

## Outputs

The following preprocessed data artifacts are generated:

* Preprocessed image files stored in dataset-specific directories

* Updated metadata CSV files:

  * `imgn_preprocessed_metadata.csv`
  * `coco_preprocessed_metadata.csv`
  * `open_preprocessed_metadata.csv`
  * `diff_preprocessed_metadata.csv`
  * `sdxl_preprocessed_metadata.csv`
  * `mj_preprocessed_metadata.csv`

Each updated metadata file maintains:

* `filename`
* `class_label`
* `source_dataset`

---

## Main Tasks

* Load metadata for each dataset
* Read and validate input images
* Convert images to a consistent format
* Resize images to a standard resolution
* Handle corrupted or unreadable files
* Save preprocessed images
* Update and save metadata tables

---

## Processing Workflow

This notebook executes a structured sequence of steps to standardize all input images:

1. **Environment Setup and Data Loading**
   The runtime environment is initialized, required libraries are imported, and metadata for all datasets is loaded.

2. **Image Access and Validation**
   Raw images are accessed using metadata references, and basic validation checks are performed to ensure files can be read.

3. **Image Preprocessing**
   Each image is processed to enforce consistency, including:

   * Format conversion
   * Resizing to a standard resolution
   * Basic quality normalization

4. **Error Handling and Logging**
   Corrupted or unreadable images are identified, skipped, and logged to maintain pipeline robustness.

5. **Metadata Update**
   Metadata tables are updated to reflect successfully processed images and remove invalid entries when necessary.

6. **Output Generation and Validation**
   Preprocessed images and updated metadata files are saved, and validation checks confirm dataset consistency and completeness.

---

## Notes and Design Choices

* **Uniform preprocessing:**
  All images are resized and formatted consistently to eliminate variability unrelated to image content.

* **Error handling for robustness:**
  Corrupted or unreadable images are safely skipped to prevent pipeline failure.

* **Metadata-driven workflow:**
  Processing is guided entirely by metadata, preserving separation between data and logic.

* **Reentrancy support:**
  The design allows preprocessing to resume without restarting from scratch in case of interruptions.

---

## Role in the Overall Pipeline

This notebook standardizes all input images, ensuring that subsequent feature extraction operates on consistent and comparable data.

It serves as a critical preparation step before combining datasets and generating feature vectors.

---

## Next Step

➡️ [03 Combine and Split](03_Combine_and_Split.md)


