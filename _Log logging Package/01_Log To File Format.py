import logging

FULLPATH = './0_Log logging Package/01.log'

logging.basicConfig(
    filename=FULLPATH, 
    filemode='a', #append
    # filemode='w', #write
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
    )

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
