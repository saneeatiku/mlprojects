import logging 
import os
from datetime import datetime

# Create a logs directory
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Now create the file path inside that folder
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Setup logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH, 
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s',
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")
