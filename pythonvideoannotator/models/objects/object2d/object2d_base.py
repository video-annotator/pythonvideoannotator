from pythonvideoannotator.models.objects.object2d.datasets.path import Path

class Object2dBase(object):

	def __init__(self, objects_set):
		self.datasets  	 = []	
		self.objects_set = objects_set
		self._name 		 = 'Undefined'
	######################################################################
	### OBJECT FUNCTIONS #################################################
	######################################################################

	def create_path_dataset(self): 
		p = Path(self)
		p.name = 'Path'
		self.datasets.append(p)
		return self.datasets[-1]

	def draw(self, frame, frame_index):
		for dataset in self.datasets: dataset.draw(frame, frame_index)
		
	######################################################################
	### CLASS FUNCTIONS ##################################################
	######################################################################

	def __len__(self): 				return len(self.datasets)
	def __getitem__(self, index): 	return self.datasets[index] if index<len(self) else None

	######################################################################
	### PROPERTIES #######################################################
	######################################################################

	@property
	def objects_set(self): return self._objects_set
	@objects_set.setter
	def objects_set(self, value): self._objects_set = value

	@property
	def name(self): return self._name
	@name.setter
	def name(self, value): self._name = value

	@property
	def datasets(self): return self._datasets
	@datasets.setter
	def datasets(self, value): self._datasets = value