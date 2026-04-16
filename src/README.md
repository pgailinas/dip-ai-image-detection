# Source Code (`src/`)

This folder contains reusable Python code that supports the DIP-based AI image detection pipeline.

Its primary purpose is to centralize shared configuration and isolate dataset-source access logic so that the notebooks remain clean, consistent, and focused on execution.

---

## Overview

The `src/` directory serves two distinct roles:

* **Shared project configuration**, used by nearly every notebook
* **Target-specific dataset access modules**, used only during dataset construction

This separation allows the majority of the pipeline to remain independent of how data is originally acquired.

---

## Structure

```text
src/
├── project_config.py
└── datasets/
    ├── __init__.py
    ├── coco_target.py
    ├── diffusiondb_target.py
    ├── imagenet_target.py
    ├── midjourney_target.py
    ├── openimages_target.py
    └── sdxl_target.py
```

---

## `project_config.py`

This file is the **central configuration module** for the project and is used by nearly every notebook in the pipeline.

It defines shared elements such as:

* project directory structure
* metadata locations
* model and output paths
* common constants and settings

Using a single configuration source ensures consistency across all stages of the pipeline and avoids duplication of path and parameter definitions.

---

## `datasets/`

The `datasets/` folder contains **target-specific Python modules** that handle access to remote image sources.

These modules are used **only in**:

* **Notebook 01 — `01_Build_Dataset.ipynb`**

Each module encapsulates source-specific details for datasets:

* COCO
* DiffusionDB
* ImageNet
* Midjourney
* OpenImages
* SDXL

These files are responsible for interacting with external data sources and are not required for later stages of the pipeline once metadata has been created.

---

## Design Philosophy

The `src/` directory follows a simple and intentional design:

* **Centralization**
  Shared configuration is defined once and reused everywhere.

* **Separation of concerns**
  Dataset acquisition logic is isolated from the rest of the pipeline.

* **Pipeline independence**
  After dataset construction, the remaining notebooks operate on metadata and derived features without needing access to original data sources.

---

## Usage

Typical usage in most notebooks:

```python
from src.project_config import *
```

Usage in Notebook 01 for dataset acquisition:

```python
from src.datasets import coco_target
from src.datasets import diffusiondb_target
```

---

## Notes

* `project_config.py` is a shared dependency across nearly all notebooks.
* Dataset target modules are specialized utilities used only during dataset construction.

---

