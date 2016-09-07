# !/usr/bin/python2
# -*- coding: utf-8 -*-

import logging
import loggingbootstrap

try:
	from pysettings import conf

	# Initiating logging for pysettings. It has to be initiated manually here because we don't know yet
	# the logger filename as specified on settings
	loggingbootstrap.create_double_logger("pysettings", logging.INFO, 'pythonvideoannotator.log', logging.INFO)

except ImportError as err:
	logging.getLogger().critical(str(err), exc_info=True)
	exit("Could not load pysettings! Is it installed?")

try:
	import pyforms
except ImportError as err:
	logging.getLogger().critical(str(err), exc_info=True)
	exit("Could not load pyforms! Is it installed?")

from pythonvideoannotator.VideoAnnotationEditor import VideoAnnotationEditor

# setup different loggers but output to single file
loggingbootstrap.create_double_logger("pythonvideoannotator", conf.APP_LOG_HANDLER_CONSOLE_LEVEL, conf.APP_LOG_FILENAME,
                                      conf.APP_LOG_HANDLER_FILE_LEVEL)
loggingbootstrap.create_double_logger("pyforms", conf.PYFORMS_LOG_HANDLER_CONSOLE_LEVEL, conf.APP_LOG_FILENAME,
                                      conf.PYFORMS_LOG_HANDLER_FILE_LEVEL)

logger = logging.getLogger("pythonvideoannotator")
logger.debug("Debug is activated")

def start(): pyforms.startApp(VideoAnnotationEditor, conf.GENERIC_EDITOR_WINDOW_GEOMETRY)


if __name__ == '__main__': start()
