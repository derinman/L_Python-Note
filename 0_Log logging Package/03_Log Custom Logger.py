# 前面範例都還是用default logger named root
# 實際(實務)上，不建議用root logger, 因為有很多外在模組會有問題

# The most commonly used classes defined in the logging module:
# Logger: 主要Object
# LogRecord: Loggers automatically create LogRecord object
# Handler: 要output去哪，StreamHandler, FileHandler, SMTPHandler, HTTPHandler...
# Formatter: format log顯示

'''
Why working with the root logger for all modules isn’t the best idea?

Imagine you have one or more modules in your project. And these modules use the basic root module. 
Then, when importing the module (‘myprojectmodule.py‘), all of that module’s code will run and logger gets configured.

Once configured, the root logger in the main file (that imported the ‘myprojectmodule‘ module) will no longer be able
to change the root logger settings. Because, the logging.basicConfig() once set cannot be changed.

That means, if you want to log the messages from myprojectmodule to one file and the logs from the main module in 
another file, root logger can’t that.

To do that you need to create a new logger.
'''

import logging

# Create a custom logger
logger = logging.getLogger(__name__)
# 建議用__name__命名，因為有外來模組的話可以知道log從那個模組來的
# 一個logger可以有多可handler，所以log可以同時輸出到email跟terminal跟file

FULLPATH = './0_Log logging Package/03.log'

# Create handlers
c_handler = logging.StreamHandler()#terminal顯示
f_handler = logging.FileHandler(FULLPATH)#to file
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

#define handler ->> set handler.setLevel, handler.setFormatter ->> logger.addHandler

logger.warning('This is a warning')
logger.error('This is an error')