from pythonvideoannotator.models.objects.object2d.datasets.path import Path

class Object2dBase(object):

	def __init__(self, name=None):
		self._datasets  = []	
		self._name 		= name

	def create_path_dataset(self): 
		path = Path(self)
		self._datasets.append(path)
		return path
		
	######################################################################
	### CLASS FUNCTIONS ##################################################
	######################################################################

	def __len__(self): 				return len(self._datasets)
	def __getitem__(self, index): 	return self._datasets[index] if index<len(self) else None

	######################################################################
	### PROPERTIES #######################################################
	######################################################################

	@property
	def name(self): return self._name
	@name.setter
	def name(self, value): self._name = value