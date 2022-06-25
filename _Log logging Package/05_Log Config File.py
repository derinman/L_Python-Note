import logging
from logging import config

from module_for_05 import doSomethingFromModule

# 更多範例請參考以下網址(L_Python裡面也有存):
# https://coderzcolumn.com/tutorials/python/logging-config-simple-guide-to-configure-loggers-from-dictionary-and-config-files-in-python

log_config = {
    "version":1,
    "loggers":{
        "":{ #root logger
            "handlers" : ["console","file"],
            "level": "DEBUG",
            "propagate": True
        },
        "module_for_05":{ #logger = logging.getLogger(__name__) in module_for_05
            "handlers" : ["console","file"],
            "level": "DEBUG",
            "propagate": True
        }
    },
    "handlers":{
        "console":{
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": "WARNING"
        },
        "file":{
            "formatter":"std_out",
            "class":"logging.FileHandler",
            "level":"INFO",
            "filename":"_Log logging Package/05.log"
        }
    },
    "formatters":{
        "std_out": {
            "format": "%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(lineno)d : (Process Details : (%(process)d, %(processName)s), Thread Details : (%(thread)d, %(threadName)s))\nLog : %(message)s",
            "datefmt":"%d-%m-%Y %I:%M:%S"
        }
    },
}

config.dictConfig(log_config)

def addition(a, b):
    logging.debug("Inside Addition Function")
    if isinstance(a, str) and a.isdigit():
        logging.warning("Warning : Parameter A is passed as String. Future versions won't support it.")

    if isinstance(b, str) and b.isdigit():
        logging.warning("Warning : Parameter B is passed as String. Future versions won't support it.")

    try:
        result = float(a) + float(b)
        logging.info("Addition Function Completed Successfully")
        return result
    except Exception as e:
        logging.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
        return None


if __name__ == "__main__":
    #logging.info("Current Log Level : {}\n".format(logging.getLevel()))

    result = addition(10,20)
    logging.info("Addition of {} & {} is : {}\n".format(10,20, result))

    result = addition("20",20)
    logging.info("Addition of {} & {} is : {}\n".format("'20'",20, result))

    doSomethingFromModule()