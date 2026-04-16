---
title: 01 Build Dataset
parent: 1. Dataset Tutorial
nav_order: 1
---

# 01 Build Dataset

**Open Notebook in Google Colab:**

<a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/01_Build_Dataset.ipynb" target="_blank" rel="noopener noreferrer">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/>
</a>

---

## Purpose

This notebook constructs the initial dataset for the DIP-based AI image detection project. It defines and organizes metadata for all image sources while establishing a consistent structure used throughout the pipeline.

The dataset consists of six sources:
- **Real images (3 sources)**
- **AI-generated images (3 sources)**

A total of **18,000 images** are referenced and prepared through metadata, without physically moving or duplicating files.

## Inputs

- Raw image directories for:
  - ImageNet (subset)
  - MS COCO (subset)
  - OpenImages (subset)
  - DiffusionDB (subset)
  - SDXL-generated images (subset)
  - MidJourney images (subset)

- Project configuration file:
  - `project_config.py`

## Outputs

- Individual metadata CSV files for each dataset:
  - `imgn_metadata.csv`
  - `coco_metadata.csv`
  - `open_metadata.csv`
  - `diff_metadata.csv`
  - `sdxl_metadata.csv`
  - `mj_metadata.csv`

Each CSV contains:
- `filename`
- `class_label` (real or ai)
- `source_dataset`

## Main Tasks

- Define dataset sources and class labels
- Enumerate image files for each dataset
- Assign consistent naming conventions
- Generate structured metadata tables
- Save metadata CSV files for downstream processing

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a high-level summary of the dataset construction process, including inputs, outputs, and assumptions.

### Cell 1: Import Libraries and Configuration
Imports required Python libraries and loads shared configuration values such as directory paths and dataset definitions.

### Cell 2: Define Dataset Sources
Specifies the six dataset sources and assigns each to either the **real** or **AI-generated** class.

### Cell 3: Enumerate Image Files
Scans dataset directories and collects filenames for each source. This step ensures that all images are accounted for without modifying their physical locations.

### Cell 4: Apply Naming Convention
Applies a consistent filename convention:
This ensures traceability and consistency across all datasets.

### Cell 5: Create Metadata Tables
Constructs a metadata table for each dataset containing filename, class label, and source information.

### Cell 6: Validate Metadata
Performs validation checks to confirm:
- Correct number of images per dataset
- Balanced class distribution
- Proper formatting of metadata fields

### Cell 7: Save Metadata CSV Files
Writes metadata tables to CSV files in the project metadata directory for use in subsequent pipeline steps.

## Notes and Design Choices

- **Metadata-driven design:**  
  Images are not moved or duplicated; all processing is controlled through CSV files.

- **Balanced dataset construction:**  
  Equal representation is maintained between real and AI-generated images.

- **Consistent naming convention:**  
  Enables traceability across preprocessing, feature extraction, and evaluation stages.

- **Separation of data and logic:**  
  Dataset structure is defined via configuration, improving maintainability and reproducibility.

## Files Produced

- `imgn_metadata.csv` — ImageNet metadata (real)
- `coco_metadata.csv` — COCO metadata (real)
- `open_metadata.csv` — OpenImages metadata (real)
- `diff_metadata.csv` — DiffusionDB metadata (AI)
- `sdxl_metadata.csv` — SDXL metadata (AI)
- `mj_metadata.csv` — MidJourney metadata (AI)

## Role in the Overall Pipeline

This notebook establishes the foundation of the entire pipeline by defining the dataset structure and generating metadata used in all subsequent steps.

All later processing stages rely exclusively on these metadata files to access and manage image data.

---

## Next Step

The dataset produced here is passed to the preprocessing stage:

➡️ [02 Preprocess Images](02_Preprocess_Images.md)

