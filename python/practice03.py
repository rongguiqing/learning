#longging模块案例3
import logging

#log有5种级别：debug,info,warnning,error,critical
#严重程度从小到大
#debug,info级别默认不输出,可以自定义输出日志格式basicConfig
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s - %(pathname)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
logging.basicConfig(filename="my.log", level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

logging.debug("This is a debug log")
logging.info("This is a info log")
logging.warning("This is a warning log")
logging.error("This is a error log")
logging.critical("This is a critical log")