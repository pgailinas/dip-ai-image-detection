# ECE 533 Project — AI Image Detection using DIP Features

This project implements a feature-based approach to detect AI-generated images using digital image processing (DIP) statistics and a neural network classifier.

## Overview

The goal is to distinguish between real and AI-generated images using handcrafted features rather than generator-specific artifacts.

## Pipeline

1. Build Dataset  
2. Preprocess Images  
3. Combine and Split  
4. Extract Features  
5. Build Feature Vectors  
6. Normalize Data  

## Notebooks

All steps are implemented as modular Jupyter notebooks:

- notebooks/01_Build_Dataset.ipynb  
- notebooks/02_Preprocess_Images.ipynb  
- notebooks/03_Combine_and_Split.ipynb  
- notebooks/04A_Extract_Gradient_Features.ipynb  
- notebooks/04B_Extract_Spatial_Features.ipynb  
- notebooks/04C_Extract_Frequency_Features.ipynb  
- notebooks/05_Build_Feature_Vectors.ipynb  
- notebooks/06_Normalize_and_Prepare_Inputs.ipynb  

## How to Run

Run the notebooks sequentially in Google Colab.

## Datasets

- ImageNet (subset)  
- MS COCO 2017  
- DiffusionDB  
- SDXL Generated Dataset  

## Status

Pipeline implementation complete. Model training and evaluation in progress.
