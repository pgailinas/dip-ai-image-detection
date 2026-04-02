# DIP-Based AI Image Detection

This project presents a feature-driven approach for detecting AI-generated images using **Digital Image Processing (DIP)** techniques combined with a neural network classifier.

---

## 🔍 Project Overview

Modern generative models can produce highly realistic images, making it increasingly difficult to distinguish synthetic content from real-world imagery.

This project investigates whether **handcrafted statistical image features** can be used to reliably differentiate between:

* Real images (natural photographs)
* AI-generated images (diffusion-based models)

Rather than relying on generator-specific artifacts, the approach focuses on **generalizable statistical properties** extracted from images.

---

## 🧠 Core Idea

Each image is transformed into a fixed-length feature vector composed of **26 DIP features**, drawn from three domains:

* **Gradient-Based Features** → edge strength and orientation
* **Spatial Features** → entropy, texture, and intensity variation
* **Frequency-Domain Features** → spectral energy distribution

These features are then used as input to a **Multi-Layer Perceptron (MLP)** classifier.

---

## 🧱 Pipeline Overview

The full pipeline is implemented as a sequence of notebooks:

1. **01 Build Dataset**
   Collect and filter images from multiple datasets

2. **02 Preprocess Images**
   Standardize images (resize to 256×256, grayscale)

3. **03 Combine and Split**
   Create balanced train / validation / test datasets

4. **04 Extract Features**
   Compute gradient, spatial, and frequency features

5. **05 Build Feature Vectors**
   Merge feature sets into unified vectors

6. **06 Normalize and Prepare Inputs**
   Validate and normalize feature data

7. **07 Train Neural Network**
   Train baseline MLP classifiers

8. **08 Evaluation** *(planned)*
   Evaluate final model performance

---

## 📊 Dataset Summary

The dataset consists of **12,000 images**, balanced across classes and sources:

### Real Images

* ImageNet (256×256 subset)
* MS COCO 2017

### AI-Generated Images

* DiffusionDB
* SDXL Generated Dataset (10K subset)

### Data Split

* Training: 8,400 images
* Validation: 1,800 images
* Test: 1,800 images

Each subset maintains balance across both class and source dataset to prevent bias and dataset leakage.

---

## 🧭 How to Use This Documentation

Use the navigation menu on the left to explore each stage of the pipeline.

Each section provides:

* A clear explanation of the processing step
* A **cell-by-cell breakdown** of the notebook
* A direct link to the corresponding **Colab notebook**

This structure allows you to:

1. Understand the method
2. Inspect the implementation
3. Run the code interactively

---

## 🔑 Key Design Principles

### Dataset Balance

Ensures equal representation across datasets and classes to avoid biased learning.

### Leakage Prevention

Splitting is performed **per dataset source** to prevent cross-contamination between training and evaluation sets.

### Feature-Driven Approach

Uses explicit DIP features instead of end-to-end image models to improve interpretability.

### Modular Pipeline

Each stage is implemented as a separate notebook, enabling:

* Easy debugging
* Reproducibility
* Incremental development

---

## 🎯 Project Goal

The central question explored in this project is:

> **Can AI-generated images be reliably distinguished from real images using only statistical DIP features and a neural network classifier?**

---

## 🚀 Getting Started

Start with:

➡️ **01 Build Dataset**

Then follow the pipeline sequentially through each stage.

---

## 👤 Author

**Phil Gailinas**
MS Computer Engineering (Machine Learning focus) candidate
University of New Mexico

---

