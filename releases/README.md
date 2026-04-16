# Releases (`releases/`)

This folder documents how large project assets are distributed using GitHub Releases.

---

## Purpose

The repository is designed to remain lightweight and focused on code, metadata, and documentation.

Large files such as:

* image datasets
* preprocessed image archives
* large feature sets
* trained model artifacts

may exceed practical repository limits and are therefore managed through **GitHub Releases**.

---

## Usage

GitHub Releases may be used to distribute:

* zipped datasets
* preprocessed image collections
* large intermediate outputs
* trained models (if too large for the repository)

These assets can be downloaded and used within the Colab notebooks as needed.

---

## Notes

* Not all workflows require downloading large assets; many steps operate entirely on metadata
* When possible, the repository favors reproducibility through pipeline execution rather than distributing large precomputed files
* This folder exists for documentation only and does not store release assets directly

---

