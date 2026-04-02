# Preprocessing

This stage standardizes all selected images before feature extraction.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/02_preprocessing.ipynb)

## Purpose

Images from different datasets vary in size, color format, and content structure. This notebook converts them into a consistent format suitable for statistical analysis.

## Main Preprocessing Steps

- Enforce minimum input requirements
- Resize images to **256×256**
- Convert images to **grayscale**
- Save preprocessed outputs
- Generate updated metadata CSV files

## Why Resize to 256×256

A fixed spatial resolution is necessary so that feature extraction is consistent across all images. Without standard dimensions, comparisons between gradient, spatial, and frequency statistics would be less meaningful.

## Why Convert to Grayscale

This project focuses on structural and statistical image properties rather than color semantics. Grayscale conversion simplifies the pipeline and centers the analysis on texture, edges, entropy, and spectral behavior.

## Expected Outputs

Each source dataset produces:

- A folder of preprocessed images
- A corresponding preprocessed metadata CSV

These outputs become the direct inputs to the later combine/split and feature extraction stages.

## Importance

This step reduces variation caused by formatting differences and ensures that later features reflect image content rather than inconsistent preprocessing conditions.

## Next Step

Once preprocessing is complete, features are extracted from the standardized images in three groups:

- Gradient-Based
- Spatial
- Frequency-Domain
