import os
from pythonvideoannotator.modules.patheditor.objects.object2d.object2d_base import Object2dBase


class Object2dIO(Object2dBase):

	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	def save(self, data, project_path=None):
		object_path = os.path.join(project_path, self.name)
		if not os.path.exists(object_path): os.makedirs(object_path)
		
		dataset_file = os.path.join(object_path, 'object2d_dataset.cvs')
		with open(dataset_file, 'w') as outfile:
			outfile.write(';'.join(['frame','x','y'])+'\n' )
			for i, moment in enumerate(self._path):
				if moment is None:
					outfile.write(';'.join(map(str, [i])) )
				else:
					outfile.write(';'.join(map(str, [moment.frame, moment.position[0], moment.position[1]] )))
				outfile.write('\n')

		return data

	def load(self, data, object_path=None):
		dataset_file = os.path.join(object_path, 'object2d_dataset.cvs')
		with open(dataset_file, 'r') as infile:
			infile.readline()
			for line in infile:
				values = line.split(';')
				if len(values)>1:
					values = map(int, line.split(';'))
					self.set_position(values[0], values[1], values[2])
				else:
					self._path.append(None)