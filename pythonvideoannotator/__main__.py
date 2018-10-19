# !/usr/bin/python2
# -*- coding: utf-8 -*-

import logging
import loggingbootstrap

try:
	import pyforms
except ImportError as err:
	logging.getLogger().critical(str(err), exc_info=True)
	exit("Could not load pyforms! Is it installed?")

try:
	from confapp import conf
	# Initiating logging for pyforms. It has to be initiated manually here because we don't know yet
	# the logger filename as specified on settings
	loggingbootstrap.create_double_logger("pyforms", logging.DEBUG, 'pythonvideoannotator.log', logging.DEBUG)
except ImportError as err:
	logging.getLogger().critical(str(err), exc_info=True)
	exit("Could not load pyforms! Is it installed?")

from pythonvideoannotator.base_module import BaseModule

print()
print('**************************************')
print()

VideoAnnotator = type(
	'VideoAnnotator',
	tuple(conf.MODULES.find_class('module.Module') + [BaseModule]),
	{}
)

# setup different loggers but output to single file
loggingbootstrap.create_double_logger("pythonvideoannotator", conf.APP_LOG_HANDLER_CONSOLE_LEVEL, conf.APP_LOG_FILENAME,
									  conf.APP_LOG_HANDLER_FILE_LEVEL)




def start(): pyforms.start_app(VideoAnnotator, geometry=conf.MAIN_WINDOW_GEOMETRY)


if __name__ == '__main__': start()
