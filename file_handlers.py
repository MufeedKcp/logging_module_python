import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logger.addHandler(console_handler)
logger.info("this goes to console")

# File handler
file_handler = logging.FileHandler("report.log")
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)
logger.error("this goes to console and file")

