import logging

# Create a custom logger
logger = logging.getLogger(__name__)
# 建議用__name__命名，因為有外來模組的話可以知道log從那個模組來的


def doSomethingFromModule():
    logger.debug('This is an debug from module')
    logger.info('This is a info from module')
    logger.warning('This is a warning from module')
    logger.error('This is an error from module')
    logger.critical('This is an error from critical')
    print('__name__:',__name__)