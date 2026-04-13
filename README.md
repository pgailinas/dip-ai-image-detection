# DIP-Based AI Image Detection

This project presents a feature-driven approach for detecting AI-generated images using Digital Image Processing (DIP) techniques combined with machine learning classifiers.

---

## 🔍 Overview

Modern generative models produce highly realistic images, making it increasingly difficult to distinguish synthetic content from real-world imagery. This project addresses that challenge by focusing on **statistical image characteristics** rather than generator-specific artifacts.

The approach extracts a fixed set of **25 Digital Image Processing (DIP) features** from each image and uses these features as input to machine learning classifiers, including a **Multi-Layer Perceptron (MLP)** and a **Radial Basis Function Support Vector Machine (RBF SVM)**.

---

## 🧠 Key Idea

Instead of detecting artifacts specific to a particular generative model, this method identifies **generalizable statistical differences** between real and AI-generated images.

These differences are captured through:

* Gradient-based structure analysis
* Spatial-domain statistics
* Frequency-domain characteristics

---

## 🧱 Pipeline Overview

The project is organized as a modular pipeline:

1. **Dataset Builder**
   * Collects and filters images from multiple datasets
   * Ensures minimum size and removes duplicates

2. **Preprocessing**
   * Resize to 256×256
   * Convert to grayscale

3. **Feature Extraction**
   * Gradient-Based Features
   * Spatial Features
   * Frequency-Domain Features

4. **Feature Vector Construction**
   * Combine all features into a 25-dimensional vector
   * Normalize using training statistics

5. **Model Selection and Training**
   * Evaluate multiple classifiers using k-fold cross-validation
   * Train selected models (MLP and RBF SVM)

6. **Evaluation**
   * Independent test set evaluation
   * Accuracy, Precision, Recall, F1 Score
   * ROC Curve and AUC

7. **Further Analysis**
   * Single-feature vs full-feature comparisons
   * Source-pair sensitivity analysis

---

## 📁 Repository Structure

dip-ai-image-detection/

├── README.md  
├── notebooks/ (01–10 pipeline)  
├── docs/ (MkDocs site)  
└── mkdocs.yml  

---

## ▶️ Run the Notebooks (Colab)

Each stage of the pipeline can be executed independently.

---

## 📊 Feature Set

A total of **25 features** are extracted per image.

---

## 🧪 Dataset

The dataset consists of **18,000 images**, balanced across real and AI-generated classes:

### Real Images (9,000)
- ImageNet  
- MS COCO  
- OpenImages  

### AI-Generated Images (9,000)
- DiffusionDB  
- SDXL  
- MidJourney  

### Data Sources
- **6 total sources**
  - 3 REAL
  - 3 AI

### Data Split

- Training + Test split only  
- k-fold cross-validation applied to training set  

The dataset maintains balance across both class and source dataset to prevent bias and dataset leakage.

---

## 🤖 Models

* **RBF SVM (Final Model)**
  * Kernel: RBF
  * C = 100
  * gamma = 0.01

* **MLP (Comparison Model)**
  * Architecture: (128, 64, 32)
  * Alpha = 0.001

---

## 📈 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC Curve
* Area Under Curve (AUC)

---

## 📌 Current Status

* [x] Dataset construction
* [x] Preprocessing
* [x] Feature extraction (all groups)
* [x] Feature vector construction
* [x] Model selection (k-fold cross-validation)
* [x] Model training (MLP and RBF SVM)
* [x] Final evaluation on independent test set
* [ ] Further analysis (Notebook 10)
* [ ] Documentation site (GitHub Pages)

---

## 📖 Documentation

A full tutorial-style documentation site is being developed using MkDocs.

---

## 👤 Author

**Phil Gailinas**  
MS Computer Engineering (AI/ML focus) candidate at University of New Mexico

---

## 📄 License

This project is for academic and research purposes.
