from pysettings import conf
from pythonvideoannotator.modules.base_videoannotator import BaseVideoAnnotator

VideoAnnotator = type(
	'VideoAnnotator',
	tuple(conf.MODULES.find_class('module.Module') + [BaseVideoAnnotator]),
	{}
)
