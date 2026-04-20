---
title: 02 Preprocess Images
parent: 1. Dataset Tutorial
nav_order: 2
---

# 02 Preprocess Images

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/dip-ai-image-detection/blob/main/notebooks/02_Preprocess_Images.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

---

## Purpose

This notebook preprocesses raw images for a **single user-selected dataset source** into a standardized format for downstream feature extraction and classification.

Preprocessing ensures all images have consistent size, format, and grayscale representation, while preserving dataset structure and filenames.

---

## Inputs

* A **user-selected dataset source** (one at a time)

* Raw dataset ZIP files stored on Google Drive:

  * `ImageNet_1K_256.zip`
  * `MS_COCO_2017.zip`
  * `DiffusionDB.zip`
  * `SDXL_Generated_10K.zip`
  * `Midjourney.zip`
  * `OpenImages.zip` (disallowed due to size)

* Project configuration file:

  * `project_config.py`

---

## Outputs

The following artifacts are generated for the selected source:

* Preprocessed images stored in:

  * `data/preprocessed/<dataset>/images/`

* Preprocessed metadata CSV:

  * `<dataset>_preprocessed_metadata.csv`

Each metadata file includes:

* `filename`
* `label`
* `dataset_code`
* `source_name`
* `original_width`
* `original_height`
* `processed_path`

---

## Key Design Behavior

### **Single-Source Processing**

Only one dataset source is processed per run, based on user selection.

---

### **ZIP-Based Input Handling**

Raw images are stored as ZIP archives on Google Drive. The notebook:

1. Copies the selected ZIP file to the local runtime
2. Extracts the ZIP locally
3. Processes images from the extracted directory

---

### **Filename Preservation**

Raw images already follow the project naming convention (e.g., `rl_imgn_000001.png`).

Preprocessing **preserves the filename**, meaning:

```
raw:         rl_imgn_000001.png
processed:   rl_imgn_000001.png
```

The difference lies in the image content, not the name.

---

### **Fresh-Run Execution Model**

Each run assumes a clean processing state:

* Output directories are cleared before processing
* Images are processed sequentially
* No indexing or resume logic is required

---

## Processing Workflow

1. **Environment Setup**
   Mount Google Drive, import libraries, and load configuration settings.

2. **User Source Selection**
   The user selects a dataset source, and ZIP file size is displayed to guide selection.

3. **ZIP Copy and Extraction**
   The selected ZIP file is copied locally and extracted in `/content`.

4. **Image Directory Detection**
   The notebook identifies the directory containing extracted images.

5. **Image Preprocessing**
   Each image is processed:

   * Resized to 256×256
   * Converted to grayscale
   * Saved using the same filename

6. **Metadata Collection**
   Metadata is recorded for each processed image.

7. **Metadata Save**
   A structured CSV file is generated for the processed dataset.

8. **Validation**
   Output counts and metadata consistency are verified.

9. **Visualization**
   Three sample image pairs are displayed:

   * Raw image (left)
   * Preprocessed image (right)

---

## Notes and Design Choices

* **Local processing for performance:**
  ZIP files are copied to the local runtime to avoid Google Drive I/O bottlenecks.

* **Deterministic filenames:**
  Filenames remain unchanged across raw and processed datasets.

* **Simplified pipeline:**
  Removing index-based naming eliminates duplication and alignment issues.

* **Robust validation:**
  The notebook verifies that processed image counts match metadata records.

---

## Role in the Overall Pipeline

This notebook standardizes image data for a single dataset source, preparing it for:

* Dataset combination
* Train/test splitting
* Feature extraction

Each dataset is processed independently and later merged.

---

## Next Step

➡️ [03 Combine and Split](03_Combine_and_Split.md)



