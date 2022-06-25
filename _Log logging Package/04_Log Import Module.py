# 前面範例都還是用default logger named root
# 實際(實務)上，不建議用root logger, 因為有很多外在模組會有問題

# The most commonly used classes defined in the logging module:
# Logger: 主要Object
# LogRecord: Loggers automatically create LogRecord object
# Handler: 要output去哪，StreamHandler, FileHandler, SMTPHandler, HTTPHandler...
# Formatter: format log顯示

import logging
from module_for_04 import doSomethingFromModule

# Create a custom logger
logger = logging.getLogger(__name__)
# 建議用__name__命名，因為有外來模組的話可以知道log從那個模組來的
# 一個logger可以有多可handler，所以log可以同時輸出到email跟terminal跟file

FULLPATH = './_Log logging Package/04.log'

# Create handlers
f_handler = logging.FileHandler(FULLPATH)#to file
f_handler.setLevel(logging.WARNING)

# Create formatters and add it to handlers
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(f_handler)

#define handler ->> set handler.setLevel, handler.setFormatter ->> logger.addHandler

logger.warning('This is a warning')
logger.error('This is an error')
doSomethingFromModule()