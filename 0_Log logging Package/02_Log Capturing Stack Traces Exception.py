import logging

FULLPATH = './0_Log logging Package/02.log'

logging.basicConfig(
    filename=FULLPATH, 
    filemode='a', #append
    # filemode='w', #write
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
    )

a = 5
b = 0

logging.info('{} start'.format(__name__))

try:
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
#exc_info設定True的話就會顯示錯誤
#此參數不限於 error，其他四種也可以用

logging.info('{} end'.format(__name__))