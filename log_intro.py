"""
author: @ibrahimaltun
module: log_intro.py

log_intro.py module provides a entry to logging library.
"""

# adding logging library into the module
import logging

# # import time
# # from logging.handlers import TimedRotatingFileHandler


def log_levels(times: int):  # default level is warning
    "logs level messages"
    for tm in range(times):
        logging.debug("%s This is a debug message", tm)
        logging.info("%s This is a info message", tm)
        logging.warning("%s This is a warning message", tm)
        logging.error("%s This is a error message", tm)
        logging.critical("%s This is a critical message", tm)


# 1- default logger as a fresh starting
# log_levels(1)

# 2- basic configurations using basicConfig() method
# set log level desired
# logging.basicConfig(level=logging.ERROR)
# log_levels(1)

# format parameter refers log message style, these elements comes from LogRecord class
LOG_FORMAT = "%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%d %m %y %H:%M:%S"
logging.basicConfig(
    filename="logger_file_1.log",
    filemode="a",
    format=LOG_FORMAT,
    datefmt=DATE_FORMAT,
    level=logging.INFO,
)
# log_levels(3)
# 3- pass parameter into log message
NAME = "Altunes"
logging.info("Your name is %s", NAME)



# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # This will create a new log file every minute, and 5 backup
# # files with a timestamp before overwriting old logs.
# handler = TimedRotatingFileHandler(
#     "timed_test.log", when="m", interval=1, backupCount=5
# )
# logger.addHandler(handler)

# for i in range(6):
#     logger.info("Hello, world!")
#     time.sleep(50)
