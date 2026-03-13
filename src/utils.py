import pandas as pd
import logging
from src.config import LOG_FILE

#add loging configuration
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    logging.info(f"Succesfully saved {len(data)} into {filename}")
    
def clean_text(text):
    return " ".join(text.split()) if text else ""

