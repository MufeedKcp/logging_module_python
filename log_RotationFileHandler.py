import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    format='%(asctime)s - %(message)s -  %(name)s - %(levelname)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = RotatingFileHandler('report.log', 
                                   maxBytes=90, backupCount=10)
file_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)

logger.info('pipeline started')
logger.warning('memory is full')
logger.error('pipeline broken')