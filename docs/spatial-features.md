# Spatial Features

This stage extracts spatial-domain statistics that summarize texture, intensity variation, entropy, and local detail.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/04_spatial_features.ipynb)

## Purpose

Spatial features describe how pixel values behave directly in the image domain. They capture image complexity, local variation, and texture-related properties.

## Features Extracted

- Global Entropy
- Local Entropy Mean
- Local Entropy Std
- Intensity Mean
- Intensity Std
- Laplacian Variance
- Patch Variance Mean
- Patch Variance Std
- Noise Residual Energy

## Why These Features Matter

AI-generated images can appear visually convincing while still differing statistically from real images. Spatial statistics help expose these differences by measuring:

- overall randomness
- local complexity
- sharpness and detail variation
- residual noise structure

## Typical Processing Flow

1. Load a preprocessed grayscale image
2. Compute global and local entropy measures
3. Compute intensity statistics
4. Measure Laplacian variance for sharpness-related behavior
5. Estimate patch-level variance and noise residual energy
6. Save results to a CSV

## Output

This notebook produces a CSV containing metadata plus spatial-domain features for each image.

## Role in the Full Pipeline

Spatial features form the second major block of the 26-feature representation. They complement gradient measures by focusing on texture and variability directly in the pixel domain.

## Next Step

The following notebook extracts frequency-domain features using FFT-based analysis.
