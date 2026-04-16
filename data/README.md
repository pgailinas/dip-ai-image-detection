# Data (`data/`)

This folder provides guidance related to dataset usage within the project.

---

## Purpose

The `data/` directory is **not** the primary working location for the pipeline.
All structured data used during processing is stored in the `metadata/` directory.

Instead, this folder exists to:

* document how datasets are used in the project
* clarify where data should and should not be stored
* provide a reference point for dataset-related notes

---

## Usage

* Raw datasets are initially accessed during **Notebook 01 — Build Dataset**
* After acquisition, all processing is performed using metadata and derived data stored in `metadata/`
* This folder may optionally contain:

  * small reference files
  * dataset notes or documentation

---

## Notes

* Large datasets should **not** be stored directly in the repository
* External data sources or packaged datasets should be accessed as described in the tutorial notebooks
* The `metadata/` directory is the authoritative location for all pipeline data

---

