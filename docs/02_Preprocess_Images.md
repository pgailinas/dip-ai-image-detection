---
title: 02 Preprocess Images
parent: 1. Dataset Tutorial
nav_order: 2
---

# 02 Preprocess Images

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/02_Preprocess_Images.ipynb)

---

## Purpose

This notebook performs image preprocessing for all dataset sources defined in the previous step. It standardizes image format, size, and quality to ensure consistency across all inputs prior to feature extraction.

Preprocessing is applied uniformly to both real and AI-generated images, enabling fair and comparable feature computation in later stages.

## Inputs

- Metadata CSV files from dataset construction:
  - `imgn_metadata.csv`
  - `coco_metadata.csv`
  - `open_metadata.csv`
  - `diff_metadata.csv`
  - `sdxl_metadata.csv`
  - `mj_metadata.csv`

- Raw image files referenced by metadata

- Project configuration file:
  - `project_config.py`

## Outputs

- Preprocessed image files stored in dataset-specific directories

- Updated metadata CSV files:
  - `imgn_preprocessed_metadata.csv`
  - `coco_preprocessed_metadata.csv`
  - `open_preprocessed_metadata.csv`
  - `diff_preprocessed_metadata.csv`
  - `sdxl_preprocessed_metadata.csv`
  - `mj_preprocessed_metadata.csv`

Each updated CSV maintains:
- `filename`
- `class_label`
- `source_dataset`

## Main Tasks

- Load metadata for each dataset
- Read and validate input images
- Convert images to a consistent format
- Resize images to a standard resolution
- Handle corrupted or unreadable files
- Save preprocessed images
- Update and save metadata tables

## Cell-by-Cell Description

### Cell 0: Notebook Overview
Provides a summary of preprocessing objectives, assumptions, and expected outputs.

### Cell 1: Import Libraries and Configuration
Loads required libraries (e.g., PIL, NumPy, Pandas) and imports shared configuration settings for directory paths and parameters.

### Cell 2: Load Metadata Files
Reads metadata CSV files generated in the dataset construction step and prepares them for processing.

### Cell 3: Define Preprocessing Function
Implements the image preprocessing routine, including loading, format conversion, resizing, and error handling.

### Cell 4: Process Images by Dataset
Iterates through each dataset, applies preprocessing to all referenced images, and saves outputs to the appropriate directories.

### Cell 5: Handle Errors and Logging
Captures and reports issues such as unreadable or corrupted files, ensuring robustness and traceability.

### Cell 6: Update Metadata Tables
Updates metadata entries to reflect successfully processed images and removes invalid entries if necessary.

### Cell 7: Validate Preprocessed Outputs
Verifies that:
- Output image counts match expectations
- Metadata remains consistent
- Directory structures are correct

### Cell 8: Save Preprocessed Metadata
Writes updated metadata CSV files for each dataset to the metadata directory.

## Notes and Design Choices

- **Uniform preprocessing:**  
  All images are resized and formatted consistently to eliminate variability unrelated to image content.

- **Error handling for robustness:**  
  Corrupted or unreadable images are safely skipped to prevent pipeline failure.

- **Metadata-driven workflow:**  
  Processing is guided entirely by metadata, preserving separation between data and logic.

- **Reentrancy support:**  
  The design allows preprocessing to resume without restarting from scratch in case of interruptions.

## Files Produced

- `imgn_preprocessed_metadata.csv` — ImageNet metadata (real)
- `coco_preprocessed_metadata.csv` — COCO metadata (real)
- `open_preprocessed_metadata.csv` — OpenImages metadata (real)
- `diff_preprocessed_metadata.csv` — DiffusionDB metadata (AI)
- `sdxl_preprocessed_metadata.csv` — SDXL metadata (AI)
- `mj_preprocessed_metadata.csv` — MidJourney metadata (AI)

## Role in the Overall Pipeline

This notebook standardizes all input images, ensuring that subsequent feature extraction operates on consistent and comparable data.

It serves as a critical preparation step before combining datasets and generating feature vectors.

## Next Step

➡️ [03 Combine and Split](03_Combine_and_Split.md)

