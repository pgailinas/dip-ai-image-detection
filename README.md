# DIP-Based AI Image Detection

A feature-driven approach for detecting AI-generated images using **Digital Image Processing (DIP)** and machine learning.

---

## 🔍 Overview

Modern generative models produce highly realistic images, making detection increasingly difficult.  
This project addresses that challenge by focusing on **statistical image characteristics** rather than generator-specific artifacts.

Each image is represented using a **25-dimensional DIP feature vector**, capturing:

- Gradient structure  
- Spatial statistics  
- Frequency-domain behavior  

These features are used to train classifiers that generalize across multiple datasets.

---

## 🧠 Key Idea

Instead of identifying artifacts from specific generative models, this method detects:

> **generalizable statistical differences between real and AI-generated images**

---

## 🧱 Pipeline

The project is implemented as a modular notebook-based pipeline:

| Stage | Notebook |
|------|--------|
| Dataset Construction | `01_Build_Dataset.ipynb` |
| Preprocessing | `02_Preprocess_Images.ipynb` |
| Combine & Split | `03_Combine_and_Split.ipynb` |
| Feature Extraction | `04–06_*_Features.ipynb` |
| Classifier Selection | `07_Classifier_Selection.ipynb` |
| Model Training | `08_Train_Two_Classifiers.ipynb` |
| Final Evaluation | `09_Evaluate_Top_Two_Classifiers.ipynb` |
| Further Analysis | `10_Further_Results.ipynb` |

---

## 📊 Feature Representation

Each image is mapped to a **25-feature vector**.

---

## 🧪 Dataset

Total: **12,000 images (balanced)**

---

## 🔄 Data Strategy

- Train/Test split only  
- k-fold cross-validation on training set  

---

## 🤖 Models

### ✅ Final Model: RBF SVM
- C = 100  
- γ = 0.01  

### Comparison Model: MLP
- (128, 64, 32), α = 0.001  

---

## 📈 Final Results (Test Set)

RBF SVM outperforms MLP across most metrics and is selected as the final model.

---

## 👤 Author

Phil Gailinas  
MS Computer Engineering (AI/ML focus)  
University of New Mexico  

---

## 📄 License

Academic and research use.
