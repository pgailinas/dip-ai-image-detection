# DIP-Based AI Image Detection

This project presents a feature-driven approach for detecting AI-generated images using Digital Image Processing (DIP) techniques combined with a neural network classifier.

---

## 🔍 Overview

Modern generative models produce highly realistic images, making it increasingly difficult to distinguish synthetic content from real-world imagery. This project addresses that challenge by focusing on **statistical image characteristics** rather than generator-specific artifacts.

The approach extracts a fixed set of **26 Digital Image Processing (DIP) features** from each image and uses these features as input to a **Multi-Layer Perceptron (MLP)** classifier.

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

   * Combine all features into a 26-dimensional vector
   * Normalize using training statistics

5. **Model Training (MLP)**

   * Train neural network on fixed-length feature vectors

6. **Evaluation**

   * Accuracy, Precision, Recall, F1 Score
   * ROC Curve and AUC

---

## 📁 Repository Structure

```
dip-ai-image-detection/
│
├── README.md
│
├── notebooks/
│   ├── 01_dataset_builder.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_gradient_features.ipynb
│   ├── 04_spatial_features.ipynb
│   ├── 05_frequency_features.ipynb
│   ├── 06_feature_vectors.ipynb
│   ├── 07_mlp_training.ipynb        (planned)
│   └── 08_evaluation.ipynb          (planned)
│
├── docs/                            (documentation site - in progress)
│   ├── index.md
│   ├── dataset-builder.md
│   ├── preprocessing.md
│   ├── gradient-features.md
│   ├── spatial-features.md
│   ├── frequency-features.md
│   ├── feature-vectors.md
│   ├── mlp-training.md
│   └── evaluation.md
│
└── mkdocs.yml                       (site navigation - planned)
```

---

## ▶️ Run the Notebooks (Colab)

Each stage of the pipeline can be executed independently:

| Stage              | Notebook                                                                                                                                   |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Dataset Builder    | [Open in Colab](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/01_dataset_builder.ipynb)    |
| Preprocessing      | [Open in Colab](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/02_preprocessing.ipynb)      |
| Gradient Features  | [Open in Colab](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/03_gradient_features.ipynb)  |
| Spatial Features   | [Open in Colab](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/04_spatial_features.ipynb)   |
| Frequency Features | [Open in Colab](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/05_frequency_features.ipynb) |
| Feature Vectors    | [Open in Colab](https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/06_feature_vectors.ipynb)    |

---

## 📊 Feature Set

A total of **26 features** are extracted per image:

### Gradient-Based Features

* Mean Gradient
* Std Gradient
* Max Gradient
* Gradient Entropy
* Edge Density
* Orientation Mean
* Orientation Std
* Orientation Entropy

### Spatial Features

* Global Entropy
* Local Entropy (Mean, Std)
* Intensity (Mean, Std)
* Laplacian Variance
* Patch Variance (Mean, Std)
* Noise Residual Energy

### Frequency-Domain Features

* Low / Mid / High Frequency Energy Ratios
* Radial Mean / Std / Entropy
* Spectral Centroid
* Spectral Bandwidth
* Log Spectrum Std

---

## 🧪 Dataset

The dataset consists of **12,000 images**, balanced across real and AI-generated classes:

* **Real Images (6,000)**

  * ImageNet (256×256 subset)
  * MS COCO 2017

* **AI-Generated Images (6,000)**

  * DiffusionDB
  * SDXL Generated Dataset (10K subset)

### Data Split

* Training: 8,400 images
* Validation: 1,800 images
* Test: 1,800 images

Each split maintains balance across both class and source dataset to prevent bias and dataset leakage.

---

## 🤖 Model

* **Classifier**: Multi-Layer Perceptron (MLP)
* **Input**: 26-dimensional feature vector
* **Training Strategy**:

  * Train/Validation/Test split (70/15/15)
  * Feature normalization based on training data

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
* [x] Gradient feature extraction
* [x] Spatial feature extraction
* [x] Frequency feature extraction
* [x] Feature vector construction
* [ ] Model training
* [ ] Evaluation and analysis
* [ ] Documentation site (GitHub Pages)

---

## 📖 Documentation (Planned)

A full tutorial-style documentation site will be available via GitHub Pages, including:

* Step-by-step pipeline explanation
* Feature descriptions and visualizations
* Links to executable notebooks

---

## 👤 Author

**Phil Gailinas**
MS Computer Engineering (AI/ML focus) candidate at University of New Mexico

---

## 📄 License

This project is for academic and research purposes.
