---
title: 01 Build Dataset
nav_order: 1
---

# 01 Build Dataset

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/01_Build_Dataset.ipynb)

---

## Overview

This notebook constructs the dataset used throughout the project by collecting images from multiple real and AI-generated sources, applying filtering rules, removing duplicates, and generating structured metadata.

The output of this stage forms the foundation for all subsequent preprocessing, feature extraction, and model training steps.

---

## Objectives

* Collect images from multiple datasets
* Enforce minimum image size requirements
* Remove duplicate images using hashing
* Organize images into a consistent directory structure
* Generate metadata CSV files for downstream processing
* Ensure balanced representation across datasets

---

## Dataset Sources

### Real Images

* ImageNet (256×256 subset)
* MS COCO 2017

### AI-Generated Images

* DiffusionDB
* SDXL Generated Dataset (10K subset)

---

## Notebook Structure

### Cell 0 — Overview

Defines the purpose, inputs, outputs, and assumptions of the dataset builder pipeline.
This cell serves as a reference for the overall workflow.

---

### Cell 1 — Configuration

Defines key parameters such as:

* Target number of images per dataset
* Minimum acceptable image size
* Output directory structure
* Dataset identifiers

---

### Cell 2 — Imports and Utilities

Loads required libraries and defines helper functions for:

* Image validation
* Size checking
* Hash computation (for duplicate detection)
* File handling

---

### Cell 3 — Dataset Initialization

Initializes structures for:

* Tracking selected images
* Managing dataset-specific counters
* Storing metadata entries

---

### Cell 4 — Load Dataset (Target-Specific)

Implements dataset-specific logic for loading images.
This stage uses a modular design so that each dataset can be handled independently.

Examples:

* Hugging Face dataset loaders
* Local dataset access
* Streaming or batch loading

---

### Cell 5 — Image Filtering

Applies filtering criteria:

* Minimum resolution requirement
* Valid image format
* Basic integrity checks

Images that fail these checks are skipped.

---

### Cell 6 — Duplicate Detection

Uses hash-based comparison to detect duplicates:

* Maintains a set of previously seen image hashes
* Skips any image with a matching hash

This ensures dataset diversity and prevents redundancy.

---

### Cell 7 — Image Selection Loop

Iterates through dataset samples:

* Applies filtering rules
* Checks for duplicates
* Collects valid images until the target count is reached

---

### Cell 8 — Save Images

Stores accepted images into a structured directory:

```
/content/images/<DATASET_NAME>/
```

Filenames follow a consistent convention:

```
[label]_[dataset]_[index].png
```

---

### Cell 9 — Metadata Generation

Creates a CSV file containing:

* Filename
* Class label (ai / real)
* Source dataset
* Image resolution

This metadata is used throughout the pipeline.

---

### Cell 10 — Progress Monitoring

Displays:

* Number of images collected
* Acceptance rate
* Dataset balance

---

### Cell 11 — Dataset Balancing

Ensures equal representation:

* Across real vs AI-generated classes
* Across individual datasets

---

### Cell 12 — Final Counts

Verifies:

* Target image counts per dataset
* Overall dataset size

---

### Cell 13 — Data Integrity Checks

Performs sanity checks:

* Confirms no missing files
* Confirms metadata alignment
* Ensures consistent labeling

---

### Cell 14 — Output Summary

Prints summary statistics:

* Total images per dataset
* Total images per class
* Final dataset size

---

### Cell 15 — Save Final Metadata

Writes dataset metadata to CSV files for downstream use.

---

### Cell 16 — Optional Debug / Sampling

Displays sample images and metadata entries for verification.

---

### Cell 17 — Completion

Marks successful completion of dataset construction.

---

## Output Artifacts

* Structured image directories per dataset
* Metadata CSV files for each dataset
* Clean, filtered, and balanced dataset

---

## Key Design Decisions

### Dataset Balance

Each dataset contributes equally to:

* Prevent bias toward a single source
* Improve generalization

---

### Duplicate Removal

Hash-based filtering ensures:

* No repeated images
* Increased dataset diversity

---

### Modular Dataset Loading

Each dataset is handled independently, making it easy to:

* Add new datasets
* Replace existing sources
* Debug dataset-specific issues

---

### Metadata-Driven Pipeline

All downstream steps rely on CSV metadata rather than directory scanning, improving:

* Reproducibility
* Traceability
* Pipeline clarity

---

## Importance of This Stage

This stage defines the **quality and integrity** of the entire project.

Errors here (such as dataset imbalance or leakage) can lead to misleading model performance and invalid conclusions.

---

## Next Step

The dataset produced here is passed to the preprocessing stage:

➡️ [02 Preprocess Images](02_Preprocess_Images.md)

