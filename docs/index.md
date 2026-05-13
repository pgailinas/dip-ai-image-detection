---
title: Home
nav_order: 0
---

# DIP-Based AI Image Detection

This tutorial presents a complete **Digital Image Processing (DIP) and machine learning pipeline** for detecting AI-generated images using engineered image statistics rather than end-to-end deep learning.

The project investigates whether compact, interpretable DIP features can capture meaningful differences between real and synthetic images across multiple image sources and AI generators.

## Project Overview

Each image is represented by a fixed **26-dimensional DIP feature vector** composed of:

- **Gradient-based features** — edge strength, gradient variation, and orientation structure
- **Spatial features** — intensity statistics, entropy, texture, and local variation
- **Frequency-domain features** — spectral energy distribution and radial frequency behavior

These handcrafted features are used with classical machine learning models to evaluate AI-image detection performance in a transparent and CPU-friendly workflow.

## Pipeline Structure

The tutorial follows a sequential notebook-based workflow covering:

- Dataset construction
- Image preprocessing
- DIP feature extraction
- Feature vector generation
- Model training and evaluation
- Feature analysis and source-pair robustness experiments

The complete workflow is illustrated below.

<p align="center">
  <img src="images/overview-pipeline.png" alt="Pipeline Overview" width="850"/>
</p>

---

**IMPORTANT NOTE:**  
The tutorial notebooks are publicly available through GitHub and can be viewed without an account. Running them in Google Colab requires a Google account. Users may also clone or download the repository and run the notebooks locally using Jupyter.

## Tutorial Scope

In addition to the core training pipeline, the project includes extended experiments and analysis for evaluating:

- Feature-level discriminative strength
- Gradient, spatial, and frequency-domain feature groups
- Cross-source robustness
- Model generalization across multiple AI generators
- Final classifier comparison and ROC analysis

The workflow emphasizes interpretability, reproducibility, modularity, and CPU-friendly execution.

## Dataset

The project dataset contains **18,000 images**, balanced across real and AI-generated image classes.

<table>
<tr>
<td valign="top">

<strong>Real-Image Datasets</strong>
<ul>
  <li>ImageNet (imgn)</li>
  <li>MS COCO (coco)</li>
  <li>OpenImages (open)</li>
</ul>

</td>
<td style="width:80px;"></td>
<td valign="top">

<strong>AI-Generated Datasets</strong>
<ul>
  <li>DiffusionDB (diff)</li>
  <li>Midjourney (midj)</li>
  <li>SDXL (sdxl)</li>
</ul>

</td>
</tr>
</table>

The dataset is organized using metadata-driven control to preserve class balance, source identity, reproducibility, and separation between training and final evaluation data.

## Models and Experiments

The tutorial evaluates multiple classical machine learning models using the normalized 26-feature DIP representation.

The workflow includes:

- Baseline classifier comparison
- Cross-validation evaluation
- Hyperparameter tuning
- Independent test-set evaluation
- ROC and AUC analysis
- Feature-level experiments
- Source-pair robustness analysis

The final stages focus not only on overall model performance, but also on understanding how feature behavior and dataset composition influence generalization.

## Evaluation and Results

<table>
<tr>
<td valign="top">

<strong>Evaluation Metrics</strong>

<ul>
  <li>Accuracy</li>
  <li>Precision</li>
  <li>Recall</li>
  <li>F1 Score</li>
  <li>ROC Curve</li>
  <li>Area Under the Curve (AUC)</li>
  <li>Confusion Matrix</li>
</ul>

</td>

<td style="width:80px;"></td>

<td valign="top">

<strong>Final Analysis Includes</strong>

<ul>
  <li>Classifier comparison</li>
  <li>Final model performance</li>
  <li>Feature-level analysis</li>
  <li>Feature-group behavior</li>
  <li>Source-pair robustness</li>
  <li>Generalization trends</li>
  <li>Implementation observations</li>
</ul>

</td>
</tr>
</table>

## Results and Insights

The completed experiments demonstrate that engineered DIP features can effectively distinguish between real and AI-generated images using lightweight classical machine learning models.

The final analysis includes:

- Classifier comparison results
- Final model performance
- Feature-level analysis
- Feature-group behavior
- Source-pair generalization trends
- Practical implementation observations

## Project Design Philosophy

This project emphasizes:

- Interpretability through handcrafted DIP features
- Reproducibility through metadata-driven processing
- Modular notebook-based pipeline stages
- Public Colab accessibility
- CPU-friendly execution
- Cross-source generalization analysis

Rather than treating AI-image detection as a black-box deep learning problem, the tutorial explores how traditional image statistics can provide meaningful and explainable detection signals.

## Author

**Phil Gailinas**  
M.S. Computer Engineering candidate  
University of New Mexico

## License

This project is intended for academic and research use.

