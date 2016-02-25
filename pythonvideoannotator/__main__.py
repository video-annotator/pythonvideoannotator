# !/usr/bin/python3
# -*- coding: utf-8 -*-

""" pythonVideoAnnotator

"""

import logging
import os

os.environ['PYFORMS_APP_SETTINGS'] = 'pythonvideoannotator.settings'

try:
    import pyforms
except:
    print("ERROR: Could not load pyforms! Is it installed?")
    exit()


from pyforms import conf as settings

from pythonvideoannotator.VideoAnnotationEditor import VideoAnnotationEditor

# create logger
logger = logging.getLogger("pythonvideoannotator")
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('{0}.log'.format(settings.LOG_FILENAME))
fh.setLevel(settings.APP_LOG_HANDLER_FILE_LEVEL)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(settings.APP_LOG_HANDLER_CONSOLE_LEVEL)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(module)s | %(funcName)s | %(message)s', datefmt='%d/%m/%Y %I:%M:%S')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug("log pythonvideoannotator is now set up")
logger.info("Starting pythonVideoAnnotator")

pyforms.startApp(VideoAnnotationEditor, geometry=(settings.WINDOW_SIZE[0], settings.WINDOW_SIZE[1], settings.WINDOW_SIZE[2], settings.WINDOW_SIZE[3]))
