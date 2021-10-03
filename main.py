# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from logger.logger import FactoryLogging



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logger = FactoryLogging.get_logger('test', filename='/tmp/mycustomlog.txt')

    logger.info('PyCharm output')
    logger.debug('PyCharm output')
    logger.warning('Pycharm output')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
