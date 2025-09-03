import logging 
import sys
import os 
from logging.handlers import RotatingFileHandler

# creating logs file
if not os.path.exists("logs"):
    os.makedirs("logs")
# log format
log_format = "%(asctime)s -%(levelname)s - %(name)s -%(message)s"

logger = logging.getLogger("fastapi_app")
logger.setLevel(logging.DEBUG)

# console handler
consoler_handler = logging.StreamHandler(sys.stdout)
consoler_handler.setLevel(logging.DEBUG)
consoler_handler.setFormatter(logging.Formatter(log_format))

# file handler 
file_handler = RotatingFileHandler("logs/app.log" , maxBytes=5*1024*1024 , backupCount=3)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(log_format))

# ATTACH handlers 
if not logger.handlers:
 logger.addHandler(consoler_handler)
 logger.addHandler(file_handler) 


logger.info("Logger initialized successfully ✅")
