# Configurable python logger module

## Description
This python module provides a single class method to define and retrieve a 
python logger object from a configuration file.

## Usage
Import the `logger` module and use the class method `get_logger` form the
`FactoryLogger` class to obtain the logger object from the standard python
logging library.

The `get_logger` class method expects no mandatory argument, but some optional
ones:

    name: the name for the logger.
    filename: the path to the logging configuration file (*.ini).

As an example:

```python
from logger import FactoryLogging
logger = FactoryLogging.get_logger('demo')
logger.info('Info stream')
logger.debug('Debug stream')
logger.warning('Warning stream')
logger.error('Error stream')
```
