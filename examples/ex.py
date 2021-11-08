from logger import FactoryLogging

if __name__ == '__main__':
    # Provide a valid configuration file (absolute path)
    # If filename does not exists, search in the default configuration log path
    FactoryLogging.config_from_file('/home/jandreu/Development/logger/examples/config.ini')
    import logging
    logger = logging.getLogger('test')
    logger.debug('Debug stream')
