import os
from pathlib import Path

BASE_DIR  = Path(__file__).resolve().parent


DATA_DIR = BASE_DIR / 'data'
LOGS_DIR = BASE_DIR / 'logs'


DATA_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# scrape settings
BASE_URL = "https://quotes.toscrape.com"  # A safe, legal site for learning
TIMEOUT = 1

OUTPUT_FILE = DATA_DIR / "scared_data.csv"
LOG_FILE = LOGS_DIR / "scrape.log"

