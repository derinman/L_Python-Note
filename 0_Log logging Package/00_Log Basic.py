import logging

#default level is WARNING
#logging.basicConfig(level=logging.DEBUG)
#只會顯示比設定level一樣或高的log

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')