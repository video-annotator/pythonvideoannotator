# !/usr/bin/python2
# -*- coding: utf-8 -*-

SETTINGS_PRIORITY = 10

import logging, os

APP_LOG_FILENAME = 'pythonvideoannotator.log'
APP_LOG_HANDLER_FILE_LEVEL = logging.DEBUG
APP_LOG_HANDLER_CONSOLE_LEVEL = logging.INFO

PYFORMS_LOG_HANDLER_FILE_LEVEL = logging.DEBUG
PYFORMS_LOG_HANDLER_CONSOLE_LEVEL = logging.INFO

VIDEO_FILE_PATH = None

SAVED_GRAPH_FILE_PATH = ""
SAVED_BONSAI_FILE_PATH = ""

GENERIC_EDITOR_WINDOW_GEOMETRY = 2000, 100, 800, 600



VIDEO_FILE_PATH = '/home/ricardo/Downloads/Group1.avi'
CHART_FILE_PATH = '/home/ricardo/Desktop/01Apollo201403210900/01Apollo201403210900_out.csv', 0, 1


PYFORMS_STYLESHEET = os.path.join('pythonvideoannotator', 'resources','themes', 'default', 'stylesheet.css')
PYFORMS_STYLESHEET_LINUX = os.path.join('pythonvideoannotator', 'resources','themes', 'default', 'stylesheet_darwin.css')