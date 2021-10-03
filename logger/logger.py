import logging
from logging.handlers import TimedRotatingFileHandler

from time import gmtime

logging.Formatter.converter = gmtime



from logging.config import fileConfig


class FactoryLogging:

    @staticmethod
    def get_logger(name='', filename=None, log_level=logging.DEBUG):
        from os import path
        log_file_path = path.join(path.dirname(path.abspath(__file__)), 'config.ini')

        fileConfig(log_file_path)

        logger = logging.getLogger(name)

        return logger

        formatter = logging.Formatter("%(asctime)s [%(name)s] %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S")
        formatter.converter = gmtime
        logger.setLevel(log_level)

        chlr = logging.StreamHandler()
        # chlr.setLevel(log_level)
        chlr.setFormatter(formatter)
        logger.addHandler(chlr)

        if filename:
            import os
            fhlr = TimedRotatingFileHandler(filename, when='midnight', backupCount=30)
            os.chmod(filename, 0o666)
            # fhlr.setLevel(log_level)
            fhlr.setFormatter(formatter)
            logger.addHandler(fhlr)

        return logger

