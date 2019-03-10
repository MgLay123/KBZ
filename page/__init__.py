import logging

import os
import time

from base.base_logs import Logger

name  = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))+'.txt'

logger = Logger(log_file_name=name , log_level=logging.INFO, logger_name="logging").get_log()