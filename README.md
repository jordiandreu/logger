# Configurable python logger module

## Description
This python module provides a single class method to configure a python logger
object from a configuration file.

## Usage
Import the `logger` module and use the class method `config_logger` form the
`FactoryLogger` class to configure the logger object from a configuration file,
according to the standard python logging library.

If there is any problem when configuring from the configuration file, a 
default logger in configure with a single StreamHandler to standard output.

The `config_logger` class method expects the filename as argument. If the
filename is not found even searching for a relative or absolute path, it tries
to search the file inside the folder defined by the LOG_CONFIG_PATH
environment variable.

As an optional argument, you can pass de default log level to be used, which
can be later changed on the configuration file.


```python
import logging
from logger import FactoryLogging
FactoryLogging.config_logger('/home/user/app/config.ini')
...
...
# Create a logger when needed
logger = logging.getLogger('MyLogger')
...
...
# Use the standard methods for each log level
logger.info('Info stream')
logger.debug('Debug stream')
logger.warning('Warning stream')
logger.error('Error stream')
```
