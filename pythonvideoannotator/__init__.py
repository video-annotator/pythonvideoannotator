# !/usr/bin/python3
# -*- coding: utf-8 -*-

__version__ 	= "2.1.1"
__author__ 		= ["Ricardo Ribeiro", "Carlos Mao de Ferro", "Hugo Cachitas"]
__credits__ 	= ["Ricardo Ribeiro", "Carlos Mao de Ferro", "Hugo Cachitas"]
__license__ 	= "Attribution-NonCommercial-ShareAlike 4.0 International"
__maintainer__ 	= ["Ricardo Ribeiro", "Carlos Mao de Ferro"]
__email__ 		= ["ricardojvr at gmail.com", "cajomferro at gmail.com"]
__status__ 		= "Development"

import pyforms #make sure pyforms settings are imported before, because of the PYFORMS_USE_QT5 variable, which is used in the plugins

####################################################
## Load the user settings in case the file exists ##
####################################################
try:
	import user_settings
	conf += user_settings
except:
	pass
####################################################
####################################################

from pysettings import conf; conf += 'pythonvideoannotator.settings'

import logging, loggingbootstrap; loggingbootstrap.create_double_logger("pyforms", logging.DEBUG, 'pythonvideoannotator.log',logging.DEBUG)


from pythonvideoannotator.base_module import BaseModule

print()
print('**************************************')
print()


VideoAnnotator = type(
	'VideoAnnotator',
	tuple(conf.MODULES.find_class('module.Module') + [BaseModule]),
	{}
)
