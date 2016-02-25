# !/usr/bin/python3
# -*- coding: utf-8 -*-

""" pyControlGUI

"""

import logging

__author__ = "Ricardo Ribeiro"
__copyright__ = "Copyright 2016 Champalimaud Foundation"
__credits__ = "Ricardo Ribeiro"
__license__ = "MIT"
__maintainer__ = ["Ricardo Ribeiro", "Carlos Mão de Ferro"]
__email__ = ["ricardojvr at gmail.com", "cajomferro at gmail.com"]
__status__ = "Development"

LOG_FILENAME = "pythonvideoannotator"

APP_NAME = "pythonvideoannotator"
APP_LOG_HANDLER_FILE_LEVEL = logging.DEBUG
APP_LOG_HANDLER_CONSOLE_LEVEL = logging.INFO

WINDOW_SIZE = [50, 50, 800, 600]
LOAD_PROJECT_ON_STARTUP = False

try:
    from myconf import *
except:
    pass
