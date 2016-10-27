from pythonvideoannotator.models.objects.object2d.datasets.path.path_gui import PathGUI
from pysettings import conf

Path = type(
	'Path',
	tuple(conf.MODULES.find_class('models.objects.object2d.datasets.path.Path') + [PathGUI]),
	{}
)
