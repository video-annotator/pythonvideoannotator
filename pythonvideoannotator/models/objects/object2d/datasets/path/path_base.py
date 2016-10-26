import cv2
from pythonvideoannotator.models.objects.object2d.utils.interpolation import interpolate_positions
from pythonvideoannotator.models.objects.object2d.datasets.path.moment import Moment

class PathBase(object):

	def __init__(self, object2d):

		self._object2d  = object2d
		self._name 		= 'Path'
		self._path 	 	= [] #path of the object
		self._tmp_path 	= [] #store a temporary path to pre-visualize de interpolation
		self._sel_pts 	= [] #store the selected points

		
	######################################################################
	### CLASS FUNCTIONS ##################################################
	######################################################################

	def __len__(self): 				return len(self._path)
	def __getitem__(self, index): 	return self._path[index] if index<len(self) else None
	def __str__(self):				return "{0} - {1}".format(self._object2d.name, self.name)

	######################################################################
	### DATA MODIFICATION AND ACCESS #####################################
	######################################################################

	def calculate_tmp_interpolation(self): 
		#store a temporary path to visualize the interpolation 
		begin 		= self._sel_pts[0].frame
		end 		= self._sel_pts[1].frame
		positions 	= []
		for i in range(begin, end + 1):
			moment = self[i]
			if moment != None and moment.position != None: positions.append([i, moment.position])
		positions = interpolate_positions(positions, begin, end, interpolation_mode=self.interpolation_mode)
		self._tmp_path = [pos for frame, pos in positions]

	def delete_range(self, begin, end):
		for index in range(begin + 1, end):
			if index <= len(self._path) and self._path[index] != None:
				self._path[index].position = None

	def interpolate_range(self, begin, end, interpolation_mode=None):
		positions = []
		for i, data in enumerate(self._path[begin:end + 1]):
			if data != None and data.position != None:
				positions.append([i + begin, data.position])

		positions = interpolate_positions(positions, begin, end, interpolation_mode)

		for frame, pos in positions:
			if self._path[frame] != None:
				self._path[frame].position = pos
			else:
				self._path[frame] = v = Moment()
				v.frame 	= frame
				v.position 	= pos
		self._tmp_path = []


	
	def set_position(self, index, x, y):
		# add positions in case they do not exists
		if index >= len(self._path):
			for i in range(len(self._path), index + 1): self._path.append(None)

		# create a new moment in case it does not exists
		if self._path[index] == None: self._path[index] = m = Moment(); m.frame = index

		# update the position
		m = self._path[index]; m.position = (x, y)

		# check if the previous moment is set and update the velocity and acceleration
		if index>0:
			pm = self._path[index-1]
			if pm is not None:
				m.velocity = pm.position[0]-m.position[0], pm.position[1]-m.position[1]
				if pm.velocity is not None:
					m.acceleration = pm.velocity[0]-m.velocity[0], pm.velocity[1]-m.velocity[1]

		# update velocity and acceleration of the next moment
		if index<(len(self._path)-1):
			nm = self._path[index+1]
			if nm is not None:
				nm.velocity = m.position[0]-nm.position[0], m.position[1]-nm.position[1]
				if m.velocity is not None:
					nm.acceleration = m.velocity[0]-nm.velocity[0], m.velocity[1]-nm.velocity[1]
			

	def find_moment(self, index, x, y):
		if index <= len(self._path) and index>=0:
			item = self._path[index]
			if item != None and item.collide(x, y):
				return item
		return None

	def get_moment(self, index):
		if index < len(self._path) and index>=0:
			return self._path[index]
		return None
	
	
	######################################################################
	### VIDEO EVENTS #####################################################
	######################################################################

	def draw(self, frame, frame_index):

		# Draw the current blobs position
		if len(self) > 0:

			v = self[frame_index]
			if v: v.draw(frame)

		# Draw the selected blobs
		for item in self._sel_pts: #store a temporary path for interpolation visualization
			item.drawCircle(frame)

		# Draw the selected path #store a temporary path for interpolation visualization
		if 1 <= len(self._sel_pts) == 2: #store a temporary path for interpolation visualization
			start = self._sel_pts[0].frame #store a temporary path for interpolation visualization
			end = frame_index if len(self._sel_pts)==1 else self._sel_pts[1].frame
			for i in range(start, end - 1):
				v1 = self[i]
				v2 = self[i + 1]
				if v1 != None and v2 != None and v2.position != None and v1.position != None:
					cv2.line(frame, v1.position, v2.position, (0, 0, 255), 1)

		# Draw a temporary path
		for i in range(len(self._tmp_path) - 1):
			p1 = self._tmp_path[i]
			p2 = self._tmp_path[i + 1]
			p1 = (int(p1[0]), int(p1[1]))
			p2 = (int(p2[0]), int(p2[1]))
			cv2.line(frame, p1, p2, (255, 0, 0), 1)


	######################################################################
	### PROPERTIES #######################################################
	######################################################################

	@property
	def interpolation_mode(self): return 'Auto'

	@property
	def name(self): return self._name
	@name.setter
	def name(self, value): self._name = value