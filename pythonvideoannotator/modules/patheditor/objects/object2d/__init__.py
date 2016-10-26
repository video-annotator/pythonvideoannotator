from pysettings import conf
from pythonvideoannotator.modules.patheditor.objects.object2d.object2d_gui import Object2dGUI as BaseObject2d
from pythonvideoannotator.modules.patheditor.objects.object2d.utils.interpolation import interpolate_positions

Object2d = type(
	'Moment',
	tuple(conf.MODULES.find_class('objects.object2d.Object2d') + [BaseObject2d]),
	{}
)
