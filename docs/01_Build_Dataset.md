---
title: 01 Build Dataset
parent: 1. Dataset Tutorial
nav_order: 1
---

# 01 Build Dataset

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/01_Build_Dataset.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook constructs the initial dataset for the DIP-based AI image detection project. It defines and organizes metadata for all image sources while establishing a consistent structure used throughout the pipeline.

The dataset consists of six sources:

* **Real images (3 sources)**
* **AI-generated images (3 sources)**

A total of **18,000 images** are referenced and prepared through metadata, without physically moving or duplicating files.

---

## Inputs

* Raw image directories for:

  * ImageNet (subset)
  * MS COCO (subset)
  * OpenImages (subset)
  * DiffusionDB (subset)
  * SDXL-generated images (subset)
  * MidJourney images (subset)

* Project configuration file:

  * `project_config.py`

---

## Outputs

The following metadata files are generated:

* `imgn_metadata.csv`
* `coco_metadata.csv`
* `open_metadata.csv`
* `diff_metadata.csv`
* `sdxl_metadata.csv`
* `mj_metadata.csv`

Each file contains:

* `filename`
* `class_label` (real or ai)
* `source_dataset`

---

## Main Tasks

* Define dataset sources and class labels
* Enumerate image files for each dataset
* Apply consistent naming conventions
* Generate structured metadata tables
* Save metadata CSV files for downstream processing

---

## Processing Workflow

This notebook executes a structured sequence of steps to construct the dataset metadata:

1. **Environment Setup and Configuration**
   The runtime environment is initialized, required libraries are imported, and project configuration settings are loaded.

2. **Dataset Definition**
   Six dataset sources are defined and assigned to either the real or AI-generated class.

3. **Image Enumeration**
   Image files are enumerated from each dataset directory, ensuring all available images are referenced without modifying their physical locations.

4. **Metadata Construction**
   Structured metadata tables are created for each dataset, capturing filename, class label, and source information.

5. **Validation**
   Metadata is validated to ensure:

   * Correct number of images per dataset
   * Balanced class distribution
   * Proper formatting and consistency

6. **Output Generation**
   Metadata tables are saved as CSV files for use in all subsequent pipeline stages.

---

## Notes and Design Choices

* **Metadata-driven design:**
  Images are not moved or duplicated; all processing is controlled through CSV files.

* **Balanced dataset construction:**
  Equal representation is maintained between real and AI-generated images.

* **Consistent naming convention:**
  Enables traceability across preprocessing, feature extraction, and evaluation stages.

* **Separation of data and logic:**
  Dataset structure is defined via configuration, improving maintainability and reproducibility.

---

## Role in the Overall Pipeline

This notebook establishes the foundation of the entire pipeline by defining the dataset structure and generating metadata used in all subsequent steps.

All later processing stages rely exclusively on these metadata files to access and manage image data.

---

## Next Step

The dataset produced here is passed to the preprocessing stage:

➡️ [02 Preprocess Images](02_Preprocess_Images.md)


