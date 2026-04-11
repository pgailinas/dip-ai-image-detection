# ============================================================
# project_config.py
# Shared project constants for DIP-Based AI Image Detection
# ============================================================

# ------------------------------------------------------------
# Base paths
# ------------------------------------------------------------

BASE_DIR = "/content/drive/MyDrive/DIP_Project"

DATA_DIR = f"{BASE_DIR}/data"
RAW_DATA_DIR = f"{DATA_DIR}/raw"
PROCESSED_DATA_DIR = f"{DATA_DIR}/processed"
METADATA_DIR = f"{DATA_DIR}/metadata"
MODELS_DIR = f"{BASE_DIR}/models"
SRC_DIR = f"{BASE_DIR}/src"

# Optional working directory in Colab runtime
LOCAL_WORK_DIR = "/content"
LOCAL_IMAGE_DIR = f"{LOCAL_WORK_DIR}/images"

# ------------------------------------------------------------
# Dataset composition
# ------------------------------------------------------------

NUM_SOURCES = 6
NUM_CLASSES = 2

# ============================================================
# Dataset Build Control
# ============================================================

IMAGES_PER_SOURCE = 3000
TARGET_ACCEPTED = IMAGES_PER_SOURCE              # 3000
TOTAL_IMAGES = IMAGES_PER_SOURCE * NUM_SOURCES   # 18000
IMAGES_PER_CLASS = TOTAL_IMAGES // NUM_CLASSES   # 9000

BATCH_ID_START = 1
BATCH_SIZE = 200
RANDOM_SEED = 42
SLEEP_BETWEEN_BATCHES = 1.0

# ------------------------------------------------------------
# Source names and dataset codes
# ------------------------------------------------------------

DATASET_CODES = {
    "diffusiondb": "diff",
    "sdxl": "sdxl",
    "midjourney": "midj",
    "imagenet": "imgn",
    "coco": "coco",
    "openimages": "opim",
}

AI_SOURCES = [
    "diffusiondb",
    "sdxl",
    "midjourney",
]

REAL_SOURCES = [
    "imagenet",
    "coco",
    "openimages",
]

# ------------------------------------------------------------
# Class labels
# ------------------------------------------------------------

AI_LABEL = "ai"
REAL_LABEL = "rl"

VALID_LABELS = [AI_LABEL, REAL_LABEL]

# ------------------------------------------------------------
# Dataset split ratios
# ------------------------------------------------------------

TRAIN_RATIO = 0.80
TEST_RATIO = 0.20

# Per-source split counts
TRAIN_PER_SOURCE = int(IMAGES_PER_SOURCE * TRAIN_RATIO)   # 2400
TEST_PER_SOURCE = IMAGES_PER_SOURCE - TRAIN_PER_SOURCE    # 600

# Global split counts
TRAIN_IMAGES = TRAIN_PER_SOURCE * NUM_SOURCES             # 14400
TEST_IMAGES = TEST_PER_SOURCE * NUM_SOURCES               # 3600

# Per-class split counts
TRAIN_PER_CLASS = TRAIN_IMAGES // NUM_CLASSES             # 7200
TEST_PER_CLASS = TEST_IMAGES // NUM_CLASSES               # 1800

# ------------------------------------------------------------
# Cross-validation settings
# ------------------------------------------------------------

K_FOLDS = 5
CV_SHUFFLE = True
CV_RANDOM_STATE = RANDOM_SEED

# ------------------------------------------------------------
# Subset names
# ------------------------------------------------------------

TRAIN_SUBSET = "train"
TEST_SUBSET = "test"

VALID_SUBSETS = [TRAIN_SUBSET, TEST_SUBSET]

# ------------------------------------------------------------
# Image preprocessing
# ------------------------------------------------------------

TARGET_SIZE = (256, 256)
MIN_WIDTH = 256
MIN_HEIGHT = 256

OUTPUT_IMAGE_FORMAT = "png"
OUTPUT_COLOR_MODE = "L"   # grayscale
OUTPUT_FILE_EXTENSION = ".png"

# ------------------------------------------------------------
# Filename convention
# ------------------------------------------------------------

FILENAME_FORMAT = "{label}_{dataset}_{index:06d}.png"

# Example:
# ai_diff_000001.png
# rl_imgn_000001.png

# ------------------------------------------------------------
# Metadata column names
# ------------------------------------------------------------

METADATA_COLUMNS = [
    "filename",
    "class_label",
    "source_dataset",
    "subset",
]

SOURCE_METADATA_COLUMNS = [
    "filename",
    "label",
    "dataset_code",
    "source_name",
    "source_id",
    "source_ref",
    "original_width",
    "original_height",
]

PREPROCESSED_METADATA_COLUMNS = [
    "filename",
    "label",
    "dataset_code",
    "source_name",
    "source_id",
    "source_ref",
    "original_width",
    "original_height",
    "processed_path",
]

# ------------------------------------------------------------
# Feature extraction
# ------------------------------------------------------------

NUM_FEATURES = 26

FEATURE_GROUPS = {
    "gradient": 8,
    "spatial": 8,
    "frequency": 10,
}

# ------------------------------------------------------------
# Classifier / normalization file names
# ------------------------------------------------------------

SCALER_FILENAME = "scaler.pkl"
SCALER_DEBUG_FILENAME = "scaler_debug.csv"
BEST_MODEL_CONFIG_FILENAME = "best_model_config.json"
BASELINE_RESULTS_FILENAME = "baseline_model_results.csv"
CV_RESULTS_FILENAME = "cross_validation_results.csv"

# ------------------------------------------------------------
# Common CSV output file names
# ------------------------------------------------------------

COMBINED_METADATA_FILENAME = "combined_metadata.csv"
TRAIN_METADATA_FILENAME = "train_metadata.csv"
TEST_METADATA_FILENAME = "test_metadata.csv"

TRAIN_FEATURE_VECTOR_FILENAME = "train_feature_vectors.csv"
TEST_FEATURE_VECTOR_FILENAME = "test_feature_vectors.csv"

TRAIN_NORMALIZED_FILENAME = "train_feature_vectors_normalized.csv"
TEST_NORMALIZED_FILENAME = "test_feature_vectors_normalized.csv"
