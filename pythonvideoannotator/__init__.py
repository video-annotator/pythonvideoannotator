# !/usr/bin/python2
# -*- coding: utf-8 -*-

__version__ = "1.4"
__author__ = ["Ricardo Ribeiro", "Carlos Mao de Ferro", "Hugo Cachitas"]
__credits__ = ["Ricardo Ribeiro", "Carlos Mao de Ferro", "Hugo Cachitas"]
__license__ = "Attribution-NonCommercial-ShareAlike 4.0 International"
__maintainer__ = ["Ricardo Ribeiro", "Carlos Mao de Ferro"]
__email__ = ["ricardojvr at gmail.com", "cajomferro at gmail.com"]
__status__ = "Development"

from pysettings import conf; conf += 'pythonvideoannotator.settings'

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

from pythonvideoannotator.base_module import BaseModule

VideoAnnotator = type(
	'VideoAnnotator',
	tuple(conf.MODULES.find_class('module.Module') + [BaseModule]),
	{}
)
