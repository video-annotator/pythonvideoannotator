# !/usr/bin/python2
# -*- coding: utf-8 -*-
SETTINGS_PRIORITY = 10

import logging, os
from pyforms.utils.package_finder import PackageFinder

MODULES = PackageFinder()

APP_LOG_FILENAME = 'pythonvideoannotator.log'
APP_LOG_HANDLER_FILE_LEVEL = logging.DEBUG
APP_LOG_HANDLER_CONSOLE_LEVEL = logging.INFO

PYFORMS_LOG_HANDLER_FILE_LEVEL = logging.DEBUG
PYFORMS_LOG_HANDLER_CONSOLE_LEVEL = logging.INFO

VIDEO_FILE_PATH = None
CHART_FILE_PATH = None

SAVED_GRAPH_FILE_PATH = ""
SAVED_BONSAI_FILE_PATH = ""

MAIN_WINDOW_GEOMETRY = 100, 200, 800, 600



VIDEO_FILE_PATH = '/home/ricardo/Desktop/Exemplo-1.ogv'
#CHART_FILE_PATH = '/home/ricardo/Desktop/01Apollo201403210900/01Apollo201403210900_out.csv', 0, 1


PYFORMS_STYLESHEET 			= os.path.join('pythonvideoannotator', 'resources','themes', 'default', 'stylesheet.css')
PYFORMS_STYLESHEET_LINUX 	= os.path.join('pythonvideoannotator', 'resources','themes', 'default', 'stylesheet_darwin.css')

MODULES += 'pythonvideoannotator.modules.timeline'
MODULES += 'pythonvideoannotator.modules.events_statistics'
MODULES += 'pythonvideoannotator.modules.patheditor'