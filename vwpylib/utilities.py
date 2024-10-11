import logging
from datetime import datetime

def init_logger():
    time_format = "%Y.%m.%dD%H:%M:%S"
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt=time_format)
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

def today_str():
    return datetime.datetime.today().strftime('%Y-%m-%d')





