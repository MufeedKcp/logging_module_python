import logging

logging.basicConfig(filename="report.log", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)
logger.error("this error is saved to file")
