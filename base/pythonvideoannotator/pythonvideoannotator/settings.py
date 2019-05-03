# !/usr/bin/python2
# -*- coding: utf-8 -*-
SETTINGS_PRIORITY = 10

import logging, os
from pyforms_gui.utils.plugins_finder import PluginsFinder

VIDEOANNOTATOR_MODULES = PluginsFinder()

APP_LOG_FILENAME 				= 'pythonvideoannotator.log'
APP_LOG_HANDLER_FILE_LEVEL 		= logging.DEBUG
APP_LOG_HANDLER_CONSOLE_LEVEL 	= logging.INFO

PYFORMS_LOG_HANDLER_FILE_LEVEL 		= logging.DEBUG
PYFORMS_LOG_HANDLER_CONSOLE_LEVEL 	= logging.INFO

PYFORMS_SILENT_PLUGINS_FINDER = True

VIDEO_FILE_PATH = None
CHART_FILE_PATH = None
VIDEOANNOTATOR_PROJECTPATH    = None

USERSTATS_TIMEOUT_DAYS = 30
USERSTATS_APP_ID = 'TPYg57bdaMLFlC8c0XHVjKnvDqSzRJrZoQ'
USERSTATS_URL = "https://stats.cf-sw.org"
#USERSTATS_URL = "http://localhost:8000"

#VIDEOANNOTATOR_PROJECTPATH    = '/media/ricardo/PEN/project_bad_tracking'
#VIDEOANNOTATOR_PROJECTPATH    = '/home/ricardo/Downloads/cecilia_movies/movies/20170526/video37_2017-05-26T10_23_51/video-annotator-prj'
#VIDEOANNOTATOR_PROJECTPATH = '/media/ricardo/b4d07af6-a493-42cb-8f15-9a5d71a0a78a/cecilia_movies/movies/20170518/video21_2017-05-18T10_40_09/video-annotator-prj'

#VIDEOANNOTATOR_PROJECTPATH = '/home/ricardo/bitbucket/idtracker-project/session_session0'

#VIDEOANNOTATOR_PROJECTPATH = '/home/ricardo/Downloads/to-delete'

SAVED_GRAPH_FILE_PATH 	= ""
SAVED_BONSAI_FILE_PATH 	= ""

MAIN_WINDOW_GEOMETRY = 50, 200, 1000, 700
#MAIN_WINDOW_GEOMETRY = 1700, 50, 1400, 1000


#VIDEO_FILE_PATH = '/home/ricardo/Downloads/fc2_save_2013-10-29-124117-0001.avi'
#VIDEO_FILE_PATH = 'C:/Users/swp/Downloads/fc2_save_2013-10-29-124117-0001.avi'
#CHART_FILE_PATH = '/home/ricardo/Desktop/01Apollo201403210900/01Apollo201403210900_out.csv', 0, 1

PYFORMS_STYLESHEET 			= os.path.join( os.path.dirname(__file__), 'resources','themes', 'default', 'stylesheet.css')
#PYFORMS_STYLESHEET_LINUX 	= os.path.join('pythonvideoannotator', 'resources','themes', 'default', 'stylesheet_darwin.css')


#VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_eventsstats'

VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_importexport'
VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_virtualobjectgenerator'
VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_idtrackerai'
VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_findorientation'
VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_motioncounter'
VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_distances'
VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_smoothpaths'
VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_createpaths'
VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_backgroundfinder'
VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_contoursimages'
VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_regionsfilter'
VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_tracking'
VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_timeline'
VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_patheditor'
VIDEOANNOTATOR_MODULES += 'pythonvideoannotator_module_pathmap'
