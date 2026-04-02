# Evaluation

This stage evaluates the selected model on independent data and measures how well the full method generalizes.

_Notebook link will be added when `08_evaluation.ipynb` is uploaded._

## Purpose

The purpose of this stage is to assess the final classifier using data that was not used for training or model tuning.

## Evaluation Metrics

The project uses the following metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC Curve
- Area Under the Curve (AUC)

## Why Multiple Metrics Are Needed

Accuracy alone may hide important behavior. Precision and recall help describe the balance between false positives and false negatives, while ROC and AUC provide a broader view of discriminative ability across thresholds.

## Typical Evaluation Tasks

- Run the selected MLP on the test set
- Compute classification metrics
- Plot ROC curve
- Compare performance across subsets if needed
- Summarize strengths and limitations

## What This Stage Shows

The evaluation stage answers the most important question of the project:

**Can AI-generated images be distinguished from real images using engineered DIP features and an MLP classifier?**

## Interpretation

Strong evaluation performance would support the usefulness of the feature-driven approach. More modest performance would still be informative by showing which statistical cues are helpful and where additional refinement is needed.

## Final Goal

The end result is a complete, reproducible pipeline that moves from image collection to preprocessing, feature extraction, classification, and performance analysis.
