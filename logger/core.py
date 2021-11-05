import logging
import os

from logging.config import fileConfig
from time import gmtime

ENVVAR = 'LOG_CONFIG_PATH'

logging.Formatter.converter = gmtime

level = {"INFO": logging.INFO,
         "DEBUG": logging.DEBUG,
         "WARNING": logging.WARNING,
         "ERROR": logging.ERROR}


class FactoryLogging:

    @staticmethod
    def _get_cfg_filepath(filename):
        """
        Searches for a valid configuration logging file. First, tries to load
        the file by interpreting the filename as an absolute path. If it is
        not the case, tries to search the configuration file in the default
        logger configuration path.

        If no configuration filename is found, a ValueError exception is
        raised.

        :param filename: configuration file name.
        :return: Absolute path to the configuration file.
        """
        # if not filename:
        #     _error = "Configuration filename has not been provided."
        #     raise ValueError(_error)
        # Check if filename is a valid filepath
        if os.path.isfile(os.path.abspath(filename)):
            return os.path.abspath(filename)
        else:
            _msg = "Searching in default configuration log path: "
            # Search the configuration file in the default configuration folder
            try:
                default_cfg_log_path = os.environ[ENVVAR]
            except KeyError:
                _msg += "{} is undefined.".format(ENVVAR)
                raise ValueError(_msg)
            filepath = os.path.join(default_cfg_log_path, filename)
            if os.path.isfile(filepath):
                return filepath
            else:
                _msg += "File {} does not exist".format(filepath)
                raise ValueError(_msg)

    @staticmethod
    def config_from_file(cfg_filename, loglevel="DEBUG"):
        """
        Logging helper based on a configuration file. This method will always
        return a valid logger object, following the next steps:

        1) If no configuration file is supplied, a basic default logger is
        provided with a StreamHandler to console.

        2) If a configuration file is supplied, the logger returned is
        created by using the fileConfig method from the standard python logging
        module.

        :param cfg_filename: The logging configuration filename.
        :param loglevel: Default loglevel
        :return: None
        """
        loglevel = loglevel.upper()
        name = FactoryLogging.__name__
        # Try to get a valid configuration filepath
        try:
            cfg_filepath = FactoryLogging._get_cfg_filepath(cfg_filename)
        except ValueError as e:
            formatter = logging.Formatter(
                "%(asctime)s [%(name)s] %(levelname)s: %(message)s",
                "%Y-%m-%d %H:%M:%S")
            formatter.converter = gmtime
            chlr = logging.StreamHandler()
            chlr.setFormatter(formatter)
            logger = logging.getLogger(name)
            logger.setLevel(level[loglevel])
            logger.addHandler(chlr)
            logger.warning(str(e))
            logger.info("Default logging CONFIGURATION (output stream)")

        else:
            fileConfig(cfg_filepath)
            logger = logging.getLogger(name)
            logger.setLevel(level[loglevel])
            logger.info("Logging CONFIGURATION from file ({})".format(cfg_filepath))


