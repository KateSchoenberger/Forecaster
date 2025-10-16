import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    @staticmethod
    def log(message: str):
        logging.info(message)
