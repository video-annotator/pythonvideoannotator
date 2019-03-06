# !/usr/bin/python2
# -*- coding: utf-8 -*-

import logging

try:
	import pyforms
except ImportError as err:
	logging.getLogger().critical(str(err), exc_info=True)
	exit("Could not load pyforms! Is it installed?")

try:
	from confapp import conf
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


def start(): pyforms.start_app(VideoAnnotator, geometry=conf.MAIN_WINDOW_GEOMETRY)


if __name__ == '__main__': start()
