import os
from pythonvideoannotator.models.objects.object2d.datasets.path.path_base import PathBase

class PathIO(PathBase):

	def get_csvrow(self, index): 
		pos = self.get_position(index)
		if pos is None: pos = [None, None]
		return [index] + list(pos)

	def load_csvrow(self, index, csvrow): 
		if csvrow[1] is None or csvrow[2] is None or len(csvrow[1])==0 or len(csvrow[2])==0: return
		frame, x, y = int(csvrow[0]), int(csvrow[1]), int(csvrow[2])
		self.set_position(frame, x, y)

	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	def save(self, data, datasets_path=None):
		dataset_file = os.path.join(datasets_path, 'path-{0}.cvs'.format(self.name))
		with open(dataset_file, 'w') as outfile:
			outfile.write(';'.join(['frame','x','y'])+'\n' )
			for i in range(len(self._path)):
				outfile.write(';'.join(  map(str,self.get_csvrow(i))  ))
				outfile.write('\n')
		return data

	def load(self, data, dataset_file=None):
		with open(dataset_file, 'r') as infile:
			infile.readline()
			for i, line in enumerate(infile):
				csvrow = line.split(';')
				self.load_csvrow(i, csvrow)