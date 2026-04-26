# DIP-Based AI Image Detection

This project presents a **feature-driven Digital Image Processing (DIP)** approach for detecting AI-generated images using engineered image statistics and classical machine learning.

Instead of end-to-end deep learning, the method uses **interpretable DIP features** derived from gradient, spatial, and frequency-domain analysis to capture statistical differences between real and synthetic images.

## 🚀 Project Summary

- Each image is represented by a **25-dimensional DIP feature vector**
- Classification is performed using:
  - **RBF Support Vector Machine (SVM)**
  - **Multi-Layer Perceptron (MLP)**
- Designed to be:
  - Generator-independent  
  - Reproducible  
  - Interpretable  

## 📘 Full Tutorial and Documentation

The complete step-by-step pipeline, including notebook walkthroughs and explanations, is available here:

👉 https://pgailinas.github.io/dip-ai-image-detection/

## 📂 Repository Structure

- `docs/` — GitHub Pages tutorial and documentation  
- `notebooks/` — Google Colab notebooks for each pipeline stage  
- `src/` — reusable Python code and configuration  
- `metadata/` — CSV-based pipeline artifacts (features, splits, models)  
- `data/` — dataset structure guidance  
- `releases/` — large downloadable assets via GitHub Releases  

## ⚙️ Execution Notes

- Designed for **Google Colab execution**
- Uses a **metadata-driven pipeline** (no need to store full datasets locally)
- Notebooks are modular and follow a structured pipeline

## 👤 Author

Phil Gailinas  
M.S. Computer Engineering (AI/ML) candidate
University of New Mexico
