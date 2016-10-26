from pysettings import conf
from pythonvideoannotator.models.objects.object2d.datasets.path.moment.moment import Moment as BaseMoment


Moment = type(
	'Moment',
	tuple(conf.MODULES.find_class('objects.object2d.moment.Moment') + [BaseMoment]),
	{}
)
