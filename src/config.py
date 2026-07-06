"""
Project Configuration File
Stores all important project paths in one place.
"""

from pathlib import Path

# Base Project Directory
BASE_DIR = Path(__file__).resolve().parent.parent


# Data Directory
DATA_DIR = BASE_DIR / "data"


# Output Directory
OUTPUT_DIR = BASE_DIR / "outputs"

FIGURE_DIR = OUTPUT_DIR / "figures"

TABLE_DIR = OUTPUT_DIR / "tables"

REPORT_DIR = OUTPUT_DIR / "reports"


# Dataset Paths
TRADING_DATA_PATH = DATA_DIR / "historical_data.csv"

SENTIMENT_DATA_PATH = DATA_DIR / "fear_greed_index.csv"