from pysettings import conf
from pythonvideoannotator.modules.base_app import VideoAnnotationEditor as App

AppClass = type(
	'VideoAnnotationEditor',
	tuple(conf.MODULES.find_class('module.Module') + [App]),
	{}
)
