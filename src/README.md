# Source Code (`src/`)

This folder contains reusable Python code used throughout the DIP-based AI image detection pipeline.
The goal of this directory is to centralize configuration and dataset-specific logic so that notebooks remain clean, readable, and focused on execution.

---

## Overview

The `src/` directory provides:

* **Project configuration**
* **Dataset-specific definitions**
* A foundation for future reusable utilities

Notebooks in the `notebooks/` folder import from `src/` to ensure consistent behavior across all stages of the pipeline.

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

This file serves as the **central configuration module** for the project.

It defines:

* Base directory paths used during execution
* Standardized locations for metadata, models, and outputs
* Common constants used across notebooks

Using a shared configuration file ensures that all notebooks operate with consistent assumptions about file locations and project structure.

---

## `datasets/`

The `datasets/` folder contains **dataset-specific modules**, one per data source.

Each file (e.g., `coco_target.py`, `diffusiondb_target.py`) encapsulates:

* Dataset name
* Class label (`real` or `ai`)
* Metadata file names
* Any dataset-specific handling logic

This design allows the pipeline to treat all datasets in a uniform way while still preserving dataset-specific details where needed.

---

## Design Philosophy

The `src/` directory follows these principles:

* **Separation of concerns**
  Notebooks focus on processing and experimentation, while `src/` holds reusable logic.

* **Consistency**
  All paths, dataset definitions, and shared parameters are defined in one place.

* **Extensibility**
  New datasets or utilities can be added without modifying existing notebooks.

---

## Usage

Typical usage within notebooks:

```python
from src.project_config import *
```

and when needed:

```python
from src.datasets import coco_target
```

This keeps notebook code clean and avoids duplication of configuration logic.

---

## Notes

* This directory is intentionally lightweight and focused.
* Most of the project logic resides in the notebooks, with `src/` providing support and structure.
* Additional modules may be added here as the project evolves.

---

