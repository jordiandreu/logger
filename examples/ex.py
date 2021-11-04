from logger import FactoryLogging

if __name__ == '__main__':
    # No configuration file provided (return a default stream logger)
    logger = FactoryLogging.get_logger('default')
    logger.debug('Debug stream')
    # Provide a valid configuration file (absolute path)
    logger = FactoryLogging.get_logger('abspath', '/home/jandreu/Development/logger/examples/config.ini')
    logger.debug('Debug stream')
    # If filename does not exists, search in the default configuration log path
    logger = FactoryLogging.get_logger('relpath', 'config.ini')
    logger.debug('Debug stream')
