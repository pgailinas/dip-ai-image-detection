# ============================================================
# project_config.py
# Shared project constants for DIP-Based AI Image Detection
# Revised to match GitHub + Google Drive Rev1 directory structure
# ============================================================

# ------------------------------------------------------------
# Base repository paths
# ------------------------------------------------------------

BASE_DIR = "/content/dip-ai-image-detection"

DATA_DIR = f"{BASE_DIR}/data"
RAW_DATA_DIR = f"{DATA_DIR}/raw"
PROCESSED_DATA_DIR = f"{DATA_DIR}/preprocessed"

METADATA_DIR = f"{BASE_DIR}/metadata"
ORIGINAL_METADATA_DIR = f"{METADATA_DIR}/original"
HASH_METADATA_DIR = f"{METADATA_DIR}/hashes"
PREPROCESSED_METADATA_DIR = f"{METADATA_DIR}/preprocessed"
SPLITS_METADATA_DIR = f"{METADATA_DIR}/splits"
FEATURES_METADATA_DIR = f"{METADATA_DIR}/features"
VECTORS_METADATA_DIR = f"{METADATA_DIR}/vectors"
MODELS_METADATA_DIR = f"{METADATA_DIR}/models"
RESULTS_METADATA_DIR = f"{METADATA_DIR}/results"

SRC_DIR = f"{BASE_DIR}/src"
DOCS_DIR = f"{BASE_DIR}/docs"
NOTEBOOKS_DIR = f"{BASE_DIR}/notebooks"

# Optional Colab runtime workspace
LOCAL_WORK_DIR = "/content"
LOCAL_IMAGE_DIR = f"{LOCAL_WORK_DIR}/images"

# ------------------------------------------------------------
# Google Drive release archive paths
# ------------------------------------------------------------

DRIVE_BASE_DIR = "/content/drive/MyDrive/DIP_Project"
RELEASES_DIR = f"{DRIVE_BASE_DIR}/releases"
RAW_RELEASES_DIR = f"{RELEASES_DIR}/raw"
PREPROCESSED_RELEASES_DIR = f"{RELEASES_DIR}/preprocessed"

# ------------------------------------------------------------
# Dataset composition
# ------------------------------------------------------------

NUM_SOURCES = 6
NUM_CLASSES = 2

# ------------------------------------------------------------
# Source names and dataset codes
# ------------------------------------------------------------

DATASET_CODES = {
    "diffusiondb": "diff",
    "sdxl": "sdxl",
    "midjourney": "midj",
    "imagenet": "imgn",
    "coco": "coco",
    "openimages": "open",
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

VALID_SOURCES = AI_SOURCES + REAL_SOURCES

SOURCE_FOLDER_NAMES = {
    "diffusiondb": "DiffusionDB",
    "sdxl": "SDXL_Generated_10K",
    "midjourney": "Midjourney",
    "imagenet": "ImageNet_1K_256",
    "coco": "MS_COCO_2017",
    "openimages": "OpenImages",
}

# ------------------------------------------------------------
# Class labels
# ------------------------------------------------------------

AI_LABEL = "ai"
REAL_LABEL = "rl"

VALID_LABELS = [AI_LABEL, REAL_LABEL]

SOURCE_LABEL_MAP = {
    "diffusiondb": AI_LABEL,
    "sdxl": AI_LABEL,
    "midjourney": AI_LABEL,
    "imagenet": REAL_LABEL,
    "coco": REAL_LABEL,
    "openimages": REAL_LABEL,
}

# ------------------------------------------------------------
# Dataset build control
# ------------------------------------------------------------

IMAGES_PER_SOURCE = 3000
TARGET_COUNT = IMAGES_PER_SOURCE
TARGET_ACCEPTED = IMAGES_PER_SOURCE              # 3000

TOTAL_IMAGES = IMAGES_PER_SOURCE * NUM_SOURCES   # 18000
IMAGES_PER_CLASS = TOTAL_IMAGES // NUM_CLASSES   # 9000

DEFAULT_SOURCE = "imagenet"

BATCH_ID_START = 1
BATCH_SIZE = 200
RANDOM_SEED = 42
SLEEP_BETWEEN_BATCHES = 1.0

# Notebook 01 runtime controls
PERSISTENCE_MODE = False
BATCHING_MODE = "notebook"   # expected values: "notebook", "api"
MAX_RETRIES_PER_BATCH = 3
LOG_PROGRESS_EVERY_N = 10

# ------------------------------------------------------------
# Dataset split ratios
# ------------------------------------------------------------

TRAIN_RATIO = 0.80
TEST_RATIO = 0.20

TRAIN_PER_SOURCE = int(IMAGES_PER_SOURCE * TRAIN_RATIO)   # 2400
TEST_PER_SOURCE = IMAGES_PER_SOURCE - TRAIN_PER_SOURCE    # 600

TRAIN_IMAGES = TRAIN_PER_SOURCE * NUM_SOURCES             # 14400
TEST_IMAGES = TEST_PER_SOURCE * NUM_SOURCES               # 3600

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

NUM_FEATURES = 25

FEATURE_GROUPS = {
    "gradient": 8,
    "spatial": 9,
    "frequency": 8,
}

# ------------------------------------------------------------
# Repo-local extracted image directories
# ------------------------------------------------------------

RAW_EXTRACT_DIRS = {
    source: f"{RAW_DATA_DIR}/{folder_name}"
    for source, folder_name in SOURCE_FOLDER_NAMES.items()
}

PREPROCESSED_DIRS = {
    source: f"{PROCESSED_DATA_DIR}/{folder_name}"
    for source, folder_name in SOURCE_FOLDER_NAMES.items()
}

# ------------------------------------------------------------
# Google Drive raw ZIP archive paths
# ------------------------------------------------------------

RAW_ZIP_PATHS = {
    "diffusiondb": f"{RAW_RELEASES_DIR}/DiffusionDB.zip",
    "imagenet": f"{RAW_RELEASES_DIR}/ImageNet_1K_256.zip",
    "midjourney": f"{RAW_RELEASES_DIR}/Midjourney.zip",
    "coco": f"{RAW_RELEASES_DIR}/MS_COCO_2017.zip",
    "openimages": f"{RAW_RELEASES_DIR}/OpenImages.zip",
    "sdxl": f"{RAW_RELEASES_DIR}/SDXL_Generated_10K.zip",
}

OPENIMAGES_MULTIPART_ARCHIVES = [
    f"{RAW_RELEASES_DIR}/OpenImages.zip",
    f"{RAW_RELEASES_DIR}/OpenImages.z01",
    f"{RAW_RELEASES_DIR}/OpenImages.z02",
    f"{RAW_RELEASES_DIR}/OpenImages.z03",
    f"{RAW_RELEASES_DIR}/OpenImages.z04",
    f"{RAW_RELEASES_DIR}/OpenImages.z05",
]

# ------------------------------------------------------------
# Google Drive preprocessed ZIP archive paths
# ------------------------------------------------------------

PREPROCESSED_ZIP_PATHS = {
    "all_sources": f"{PREPROCESSED_RELEASES_DIR}/All_Sources_preprocessed.zip",
    "diffusiondb": f"{PREPROCESSED_RELEASES_DIR}/DiffusionDB_preprocessed.zip",
    "imagenet": f"{PREPROCESSED_RELEASES_DIR}/ImageNet_1K_256_preprocessed.zip",
    "midjourney": f"{PREPROCESSED_RELEASES_DIR}/Midjourney_preprocessed.zip",
    "coco": f"{PREPROCESSED_RELEASES_DIR}/MS_COCO_2017_preprocessed.zip",
    "openimages": f"{PREPROCESSED_RELEASES_DIR}/OpenImages_preprocessed.zip",
    "sdxl": f"{PREPROCESSED_RELEASES_DIR}/SDXL_Generated_10K_preprocessed.zip",
}

# ------------------------------------------------------------
# Metadata file paths: original
# ------------------------------------------------------------

SOURCE_METADATA_FILES = {
    "coco": f"{ORIGINAL_METADATA_DIR}/coco_raw_metadata.csv",
    "diffusiondb": f"{ORIGINAL_METADATA_DIR}/diff_raw_metadata.csv",
    "imagenet": f"{ORIGINAL_METADATA_DIR}/imgn_raw_metadata.csv",
    "midjourney": f"{ORIGINAL_METADATA_DIR}/midj_raw_metadata.csv",
    "openimages": f"{ORIGINAL_METADATA_DIR}/open_raw_metadata.csv",
    "sdxl": f"{ORIGINAL_METADATA_DIR}/sdxl_raw_metadata.csv",
}

# ------------------------------------------------------------
# Metadata file paths: hashes
# ------------------------------------------------------------

HASH_METADATA_FILES = {
    "coco": f"{HASH_METADATA_DIR}/coco_source_hashes.json",
    "diffusiondb": f"{HASH_METADATA_DIR}/diff_source_hashes.json",
    "imagenet": f"{HASH_METADATA_DIR}/imgn_source_hashes.json",
    "midjourney": f"{HASH_METADATA_DIR}/midj_source_hashes.json",
    "openimages": f"{HASH_METADATA_DIR}/open_source_hashes.json",
    "sdxl": f"{HASH_METADATA_DIR}/sdxl_source_hashes.json",
    "global": f"{HASH_METADATA_DIR}/global_hashes.json",
}

# ------------------------------------------------------------
# Metadata file paths: preprocessed
# ------------------------------------------------------------

PREPROCESSED_METADATA_FILES = {
    "coco": f"{PREPROCESSED_METADATA_DIR}/coco_preprocessed_metadata.csv",
    "diffusiondb": f"{PREPROCESSED_METADATA_DIR}/diff_preprocessed_metadata.csv",
    "imagenet": f"{PREPROCESSED_METADATA_DIR}/imgn_preprocessed_metadata.csv",
    "midjourney": f"{PREPROCESSED_METADATA_DIR}/midj_preprocessed_metadata.csv",
    "openimages": f"{PREPROCESSED_METADATA_DIR}/open_preprocessed_metadata.csv",
    "sdxl": f"{PREPROCESSED_METADATA_DIR}/sdxl_preprocessed_metadata.csv",
}

# ------------------------------------------------------------
# Metadata file paths: splits
# ------------------------------------------------------------

COMBINED_METADATA_FILENAME = "combined_metadata.csv"
TRAIN_METADATA_FILENAME = "train_metadata.csv"
TEST_METADATA_FILENAME = "test_metadata.csv"

COMBINED_METADATA_PATH = f"{SPLITS_METADATA_DIR}/{COMBINED_METADATA_FILENAME}"
TRAIN_METADATA_PATH = f"{SPLITS_METADATA_DIR}/{TRAIN_METADATA_FILENAME}"
TEST_METADATA_PATH = f"{SPLITS_METADATA_DIR}/{TEST_METADATA_FILENAME}"

# ------------------------------------------------------------
# Metadata file paths: feature groups
# ------------------------------------------------------------

TRAIN_GRADIENT_FEATURES_FILENAME = "train_gradient_features.csv"
TEST_GRADIENT_FEATURES_FILENAME = "test_gradient_features.csv"

TRAIN_SPATIAL_FEATURES_FILENAME = "train_spatial_features.csv"
TEST_SPATIAL_FEATURES_FILENAME = "test_spatial_features.csv"

TRAIN_FREQUENCY_FEATURES_FILENAME = "train_frequency_features.csv"
TEST_FREQUENCY_FEATURES_FILENAME = "test_frequency_features.csv"

TRAIN_GRADIENT_FEATURES_PATH = f"{FEATURES_METADATA_DIR}/{TRAIN_GRADIENT_FEATURES_FILENAME}"
TEST_GRADIENT_FEATURES_PATH = f"{FEATURES_METADATA_DIR}/{TEST_GRADIENT_FEATURES_FILENAME}"

TRAIN_SPATIAL_FEATURES_PATH = f"{FEATURES_METADATA_DIR}/{TRAIN_SPATIAL_FEATURES_FILENAME}"
TEST_SPATIAL_FEATURES_PATH = f"{FEATURES_METADATA_DIR}/{TEST_SPATIAL_FEATURES_FILENAME}"

TRAIN_FREQUENCY_FEATURES_PATH = f"{FEATURES_METADATA_DIR}/{TRAIN_FREQUENCY_FEATURES_FILENAME}"
TEST_FREQUENCY_FEATURES_PATH = f"{FEATURES_METADATA_DIR}/{TEST_FREQUENCY_FEATURES_FILENAME}"

# ------------------------------------------------------------
# Metadata file paths: feature vectors
# ------------------------------------------------------------

TRAIN_FEATURE_VECTOR_FILENAME = "train_feature_vectors.csv"
TEST_FEATURE_VECTOR_FILENAME = "test_feature_vectors.csv"

TRAIN_NORMALIZED_FILENAME = "train_feature_vectors_normalized.csv"
TEST_NORMALIZED_FILENAME = "test_feature_vectors_normalized.csv"

TRAIN_FEATURE_VECTOR_PATH = f"{VECTORS_METADATA_DIR}/{TRAIN_FEATURE_VECTOR_FILENAME}"
TEST_FEATURE_VECTOR_PATH = f"{VECTORS_METADATA_DIR}/{TEST_FEATURE_VECTOR_FILENAME}"

TRAIN_NORMALIZED_PATH = f"{VECTORS_METADATA_DIR}/{TRAIN_NORMALIZED_FILENAME}"
TEST_NORMALIZED_PATH = f"{VECTORS_METADATA_DIR}/{TEST_NORMALIZED_FILENAME}"

# ------------------------------------------------------------
# Model artifact file paths
# ------------------------------------------------------------

SCALER_FILENAME = "scaler.pkl"
BEST_MLP_MODEL_CONFIG_FILENAME = "best_mlp_model_config.json"
BEST_RBF_SVM_MODEL_CONFIG_FILENAME = "best_rbf_svm_model_config.json"
FINAL_MLP_MODEL_FILENAME = "final_mlp_model.pkl"
FINAL_RBF_SVM_MODEL_FILENAME = "final_rbf_svm_model.pkl"

SCALER_PATH = f"{MODELS_METADATA_DIR}/{SCALER_FILENAME}"
BEST_MLP_MODEL_CONFIG_PATH = f"{MODELS_METADATA_DIR}/{BEST_MLP_MODEL_CONFIG_FILENAME}"
BEST_RBF_SVM_MODEL_CONFIG_PATH = f"{MODELS_METADATA_DIR}/{BEST_RBF_SVM_MODEL_CONFIG_FILENAME}"
FINAL_MLP_MODEL_PATH = f"{MODELS_METADATA_DIR}/{FINAL_MLP_MODEL_FILENAME}"
FINAL_RBF_SVM_MODEL_PATH = f"{MODELS_METADATA_DIR}/{FINAL_RBF_SVM_MODEL_FILENAME}"

# ------------------------------------------------------------
# Results file paths
# ------------------------------------------------------------

BASELINE_MODEL_CONFIG_FILENAME = "baseline_model_config.json"
BASIC_TESTING_RESULTS_FILENAME = "basic_testing_results.csv"
BEST_MODEL_CONFIG_FILENAME = "best_model_config.json"
CLASSIFIER_COMPARISON_BASELINE_FILENAME = "classifier_comparison_baseline.csv"
CLASSIFIER_COMPARISON_TUNED_FILENAME = "classifier_comparison_tuned.csv"
CROSS_VALIDATION_RESULTS_FILENAME = "cross_validation_results.csv"
FINAL_COMPARISON_SUMMARY_FILENAME = "final_comparison_summary.csv"
FINAL_CONFUSION_MATRIX_MLP_FILENAME = "final_confusion_matrix_mlp.csv"
FINAL_CONFUSION_MATRIX_RBF_SVM_FILENAME = "final_confusion_matrix_rbf_svm.csv"
FINAL_ROC_POINTS_MLP_FILENAME = "final_roc_points_mlp.csv"
FINAL_ROC_POINTS_RBF_SVM_FILENAME = "final_roc_points_rbf_svm.csv"
FINAL_TEST_RESULTS_FILENAME = "final_test_results.csv"
FINAL_TEST_RESULTS_JSON_FILENAME = "final_test_results.json"
FINE_TUNING_RESULTS_FILENAME = "fine_tuning_results.csv"
TUNED_MODEL_RESULTS_FILENAME = "tuned_model_results.csv"

BASELINE_MODEL_CONFIG_PATH = f"{RESULTS_METADATA_DIR}/{BASELINE_MODEL_CONFIG_FILENAME}"
BASIC_TESTING_RESULTS_PATH = f"{RESULTS_METADATA_DIR}/{BASIC_TESTING_RESULTS_FILENAME}"
BEST_MODEL_CONFIG_PATH = f"{RESULTS_METADATA_DIR}/{BEST_MODEL_CONFIG_FILENAME}"
CLASSIFIER_COMPARISON_BASELINE_PATH = f"{RESULTS_METADATA_DIR}/{CLASSIFIER_COMPARISON_BASELINE_FILENAME}"
CLASSIFIER_COMPARISON_TUNED_PATH = f"{RESULTS_METADATA_DIR}/{CLASSIFIER_COMPARISON_TUNED_FILENAME}"
CROSS_VALIDATION_RESULTS_PATH = f"{RESULTS_METADATA_DIR}/{CROSS_VALIDATION_RESULTS_FILENAME}"
FINAL_COMPARISON_SUMMARY_PATH = f"{RESULTS_METADATA_DIR}/{FINAL_COMPARISON_SUMMARY_FILENAME}"
FINAL_CONFUSION_MATRIX_MLP_PATH = f"{RESULTS_METADATA_DIR}/{FINAL_CONFUSION_MATRIX_MLP_FILENAME}"
FINAL_CONFUSION_MATRIX_RBF_SVM_PATH = f"{RESULTS_METADATA_DIR}/{FINAL_CONFUSION_MATRIX_RBF_SVM_FILENAME}"
FINAL_ROC_POINTS_MLP_PATH = f"{RESULTS_METADATA_DIR}/{FINAL_ROC_POINTS_MLP_FILENAME}"
FINAL_ROC_POINTS_RBF_SVM_PATH = f"{RESULTS_METADATA_DIR}/{FINAL_ROC_POINTS_RBF_SVM_FILENAME}"
FINAL_TEST_RESULTS_PATH = f"{RESULTS_METADATA_DIR}/{FINAL_TEST_RESULTS_FILENAME}"
FINAL_TEST_RESULTS_JSON_PATH = f"{RESULTS_METADATA_DIR}/{FINAL_TEST_RESULTS_JSON_FILENAME}"
FINE_TUNING_RESULTS_PATH = f"{RESULTS_METADATA_DIR}/{FINE_TUNING_RESULTS_FILENAME}"
TUNED_MODEL_RESULTS_PATH = f"{RESULTS_METADATA_DIR}/{TUNED_MODEL_RESULTS_FILENAME}"

