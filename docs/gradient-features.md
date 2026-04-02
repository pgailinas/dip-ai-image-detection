# Gradient Features

This stage extracts gradient-based features that describe edges, directional structure, and local intensity change.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/03_gradient_features.ipynb)

## Purpose

Gradient features help characterize image structure. They capture how rapidly intensities change and how edge directions are distributed across the image.

## Main Idea

The notebook computes image gradients using derivative operators such as Sobel or Scharr, then summarizes the resulting magnitude and orientation information into fixed numerical descriptors.

## Features Extracted

- Mean Gradient
- Std Gradient
- Max Gradient
- Gradient Entropy
- Edge Density
- Orientation Mean
- Orientation Std
- Orientation Entropy

## Why These Features Matter

Real and AI-generated images may differ in how edges are formed, how smooth or abrupt local transitions appear, and how directional structure is distributed. Gradient statistics provide one way to quantify those differences.

## Typical Processing Flow

1. Load a preprocessed grayscale image
2. Compute horizontal and vertical gradients
3. Derive gradient magnitude and orientation
4. Calculate summary statistics
5. Save the resulting features into a CSV

## Output

The output of this stage is a feature CSV containing metadata plus gradient-derived descriptors for each training image.

## Role in the Full Pipeline

Gradient features form the first block of the final 26-dimensional feature vector. They emphasize structural information and complement the spatial and frequency-domain features extracted in later stages.

## Next Step

The next notebook computes spatial-domain statistics such as entropy, variance, and noise-related measures.
