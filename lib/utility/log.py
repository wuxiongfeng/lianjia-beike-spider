#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import logging
from lib.utility.path import LOG_PATH
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler(LOG_PATH + "/log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

if __name__ == '__main__':
    pass