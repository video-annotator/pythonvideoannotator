import os
from pythonvideoannotator.modules.patheditor.objects.object2d.datasets.path.path_base import PathBase
from pythonvideoannotator.modules.patheditor.objects.object2d.datasets.path.moment import Moment

class PathIO(PathBase):

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





	def import_csv(self, filename, sep=',', frameCol=0, xCol=1,	yCol=2, zCol=None):
		Moment.FRAME_COL = self._frame_col  = frameCol
		Moment.X_COL 	 = self._x_col 	 	= xCol
		Moment.Y_COL 	 = self._y_col 	 	= yCol
		Moment.Z_COL 	 = self._z_col 	 	= zCol
		self._separator  = self._separator  = sep

		with open(filename, 'rb') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=self._separator, quotechar='"')
			data = []

			for i, row in enumerate(spamreader):
				if Moment.TOTAL_COLS < len(row):
					Moment.TOTAL_COLS = len(row)

				rowdata = Moment(row)

				# If the first frame is not 0 then insert none values until the first frame with the position
				if len(data) == 0 and rowdata.frame > 0:
					data = [None for i in range(rowdata.frame)]
				# Add none values for missing frames
				if len(data) > 0 and data[-1] != None and (rowdata.frame - data[-1].frame) > 1:
					for i in range(data[-1].frame + 1, rowdata.frame):
						data.append(None)

				data.append(rowdata)
			self._path = data

	def export_csv(self, filename):
		Moment.FRAME_COL = self._frame_col
		Moment.X_COL 	 = self._x_col
		Moment.Y_COL 	 = self._y_col
		Moment.Z_COL 	 = self._z_col

		with open(filename, 'wb') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=self._separator)
			#spamwriter.writerow(['Frame','Name','pos X','pos Y','head X','head Y','tail X','tail Y'])
			for data in self._path:
				if data != None:
					spamwriter.writerow(data.row)