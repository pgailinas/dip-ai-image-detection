# Feature Vectors

This stage merges the three feature groups into a single fixed-length representation for each image.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/06_feature_vectors.ipynb)

## Purpose

The classifier does not operate directly on images. Instead, it takes a numerical feature vector as input. This notebook combines the previously extracted gradient, spatial, and frequency features into one unified dataset.

## Inputs

This stage uses the outputs of:

- Gradient feature extraction
- Spatial feature extraction
- Frequency feature extraction

It also uses the train, validation, and test metadata splits.

## Main Tasks

- Align feature rows with metadata rows
- Merge all feature groups
- Build the full **26-dimensional feature vector**
- Separate training, validation, and test data
- Normalize features using statistics computed on the training set only
- Save processed feature tables and scaling information

## Why Training-Only Normalization Matters

Normalization parameters must be computed from the training data alone. Applying statistics from the full dataset would leak information from the validation or test sets into the model-development process.

## Outputs

Typical outputs of this stage include:

- Normalized training feature matrix
- Normalized validation feature matrix
- Normalized test feature matrix
- Scaler parameters or equivalent saved statistics
- Final CSV files ready for MLP input

## Importance

This notebook converts three separate analytical streams into a single machine-learning-ready representation. It is the bridge between image analysis and classification.

## Next Step

The next stage trains an MLP classifier using the 26-feature vectors.
