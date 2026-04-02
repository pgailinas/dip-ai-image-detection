# Frequency Features

This stage extracts frequency-domain statistics that describe how image energy is distributed across spatial frequencies.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/05_frequency_features.ipynb)

## Purpose

Frequency-domain analysis helps reveal patterns that may not be obvious in the spatial domain. It provides a compact way to summarize coarse structure, fine detail, and spectral organization.

## Main Idea

Each image is transformed using the Fourier Transform. The resulting spectrum is analyzed to compute descriptors that measure how image energy is distributed across low, mid, and high frequencies.

## Features Extracted

- Low Frequency Energy Ratio
- Mid Frequency Energy Ratio
- High Frequency Energy Ratio
- Radial Mean
- Radial Std
- Radial Entropy
- Spectral Centroid
- Spectral Bandwidth
- Log Spectrum Std

## Why These Features Matter

Synthetic images may differ from real images in their spectral balance, radial energy distribution, or fine-detail content. Frequency-domain features provide a way to quantify those differences systematically.

## Typical Processing Flow

1. Load a preprocessed grayscale image
2. Compute the FFT
3. Form the magnitude or power spectrum
4. Compute radial statistics and band energy ratios
5. Derive spectral summary features
6. Save the results to a CSV

## Output

The output is a CSV containing metadata plus frequency-domain descriptors for each image.

## Role in the Full Pipeline

These features provide the third and final feature group in the overall 26-dimensional image representation.

## Next Step

After all three feature groups are extracted, they are merged into unified feature vectors for training and evaluation.
