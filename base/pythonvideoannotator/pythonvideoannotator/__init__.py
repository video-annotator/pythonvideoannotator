# !/usr/bin/python3
# -*- coding: utf-8 -*-

__version__ = "3.305.524"
__author__ 		= ["Ricardo Ribeiro", "Carlos Mao de Ferro", "Hugo Cachitas"]
__credits__ 	= ["Ricardo Ribeiro", "Carlos Mao de Ferro", "Hugo Cachitas"]
__license__ 	= "Attribution-NonCommercial-ShareAlike 4.0 International"
__maintainer__ 	= ["Ricardo Ribeiro", "Carlos Mao de Ferro"]
__email__ 		= ["ricardojvr at gmail.com", "cajomferro at gmail.com"]
__status__ 		= "Development"

from confapp import conf; conf += 'pythonvideoannotator.settings'


import logging

logger = logging.getLogger(__name__)
logger.setLevel(conf.APP_LOG_HANDLER_LEVEL)

if conf.APP_LOG_HANDLER_FILE:
    logger = logging.getLogger()
    loggers_formatter = logging.Formatter(conf.PYFORMS_LOG_FORMAT)

    fh = logging.FileHandler(conf.APP_LOG_HANDLER_FILE)
    fh.setLevel(conf.APP_LOG_HANDLER_FILE_LEVEL)
    fh.setFormatter(loggers_formatter)
    logger.addHandler(fh)
