# MLP Training

This stage trains a Multi-Layer Perceptron (MLP) classifier on the engineered feature vectors.

_Notebook link will be added when `07_mlp_training.ipynb` is uploaded._

## Purpose

The goal of this stage is to learn a mapping from the 26-dimensional DIP feature vector to one of two classes:

- Real
- AI-generated

## Why an MLP

This project uses a neural network, but not an end-to-end image model. Instead, the MLP acts as a classifier on top of handcrafted image statistics. This keeps the emphasis on whether DIP features themselves provide useful discriminatory power.

## Inputs

The MLP uses:

- Normalized training feature vectors
- Validation feature vectors
- Corresponding class labels

## Training Tasks

This stage typically includes:

- Defining the model architecture
- Selecting hidden-layer size and activation functions
- Choosing regularization settings
- Training on the training set
- Monitoring performance on the validation set
- Comparing candidate model configurations

## Model Selection Perspective

Different hyperparameter settings produce different trained models. The training notebook is therefore not only fitting a network, but also selecting the most effective configuration among the tested candidates.

## Expected Outputs

- Trained MLP model
- Validation performance results
- Candidate model comparison table
- Best-model selection for final testing

## Why This Stage Matters

This notebook tests the central project claim: that a neural classifier can distinguish real and AI-generated images using only DIP-based feature vectors.

## Next Step

Once the best model is selected, it is evaluated on the independent test set.
