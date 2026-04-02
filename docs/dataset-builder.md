# Dataset Builder

This stage constructs the project dataset from multiple real-image and AI-generated image sources.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/01_dataset_builder.ipynb)

## Purpose

The goal of this notebook is to gather images from the selected source datasets, apply filtering rules, and produce organized metadata that supports later preprocessing and feature extraction.

## Source Datasets

### Real Image Sources
- ImageNet (256×256 subset)
- MS COCO 2017

### AI-Generated Image Sources
- DiffusionDB
- SDXL Generated Dataset (10K subset)

## Main Tasks

This notebook is responsible for:

- Downloading or accessing source datasets
- Filtering images based on minimum size requirements
- Removing duplicates when possible
- Organizing outputs into a consistent structure
- Creating metadata CSV files for downstream processing

## Output Philosophy

The dataset is intentionally balanced across:

- Real vs AI-generated classes
- Source datasets within each class

This helps reduce class bias and prevents the classifier from learning trivial shortcuts tied to one source only.

## Design Considerations

A major concern in this project is **dataset leakage**. If similar images or related prompt-derived outputs appear across different subsets, model performance can appear artificially strong. For that reason, the dataset construction process emphasizes careful organization before splitting.

## Expected Outputs

Typical outputs of this stage include:

- Raw or filtered image collections
- Source-specific metadata CSV files
- A clean starting point for preprocessing

## Why This Stage Matters

A weak dataset pipeline can invalidate later results. This stage establishes the foundation for reproducibility, balance, and fair evaluation.

## Next Step

After dataset construction, all selected images move into the preprocessing stage, where they are standardized to a common representation.
