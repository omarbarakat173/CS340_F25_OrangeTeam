import logging
import os

log_dir = "Output"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "log.txt")

logging.basicConfig(
    filename=log_file,
    filemode="a",
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)

def log_progress(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
