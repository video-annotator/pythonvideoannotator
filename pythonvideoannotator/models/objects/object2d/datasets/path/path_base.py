import cv2, math
from pythonvideoannotator.models.objects.object2d.utils.interpolation import interpolate_positions


class PathBase(object):

	def __init__(self, object2d):
		self.object2d   = object2d
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
		begin 		= self._sel_pts[0]
		end 		= self._sel_pts[1]
		positions 	= [[i, self.get_position(i)] for i in range(begin, end + 1) if self.get_position(i) is not None]
		positions   = interpolate_positions(positions, begin, end, interpolation_mode=self.interpolation_mode)
		self._tmp_path = [pos for frame, pos in positions]

	def delete_range(self, begin, end):
		for index in range(begin + 1, end):
			if index <= len(self._path) and self._path[index] != None: self._path[index] = None

	def interpolate_range(self, begin, end, interpolation_mode=None):
		positions = [[i, self.get_position(i)] for i in range(begin, end+1) if self.get_position(i) is not None]
		positions = interpolate_positions(positions, begin, end, interpolation_mode)
		for frame, pos in positions: self.set_position(frame, pos[0], pos[1])
		self._tmp_path = []

	def get_velocity(self, index):
		p1 = self.get_position(index)
		p2 = self.get_position(index-1)
		if p1 is None or p2 is None: return None
		return p2[0]-p1[0], p2[1]-p1[1]
		

	def get_acceleration(self, index):
		v1 = self.get_velocity(index)
		v2 = self.get_velocity(index-1)
		if v1 is None or v2 is None: return None
		return v2[0]-v1[0], v2[1]-v1[1]

	def get_position(self, index):
		if index<0 or index>=len(self._path): return None
		return self._path[index] if self._path[index] is not None else None

	def set_position(self, index, x, y):
		# add positions in case they do not exists
		if index >= len(self._path):
			for i in range(len(self._path), index + 1): self._path.append(None)

		# create a new moment in case it does not exists
		self._path[index] = int(round(x)),int(round(y))
			

	def collide_with_position(self, index, x, y, radius=20):
		p1 = self.get_position(index)
		if p1 is None: return False
		return math.sqrt((p1[0] - x)**2 + (p1[1] - y)**2) < radius
	
	######################################################################
	### VIDEO EVENTS #####################################################
	######################################################################

	def draw_circle(self, frame, frame_index):
		position = self.get_position(frame_index)
		if position != None:
			cv2.circle(frame, position[:2], 20, (255, 255, 255), 4, lineType=cv2.LINE_AA)  # pylint: disable=no-member
			cv2.circle(frame, position[:2], 20, (50, 50, 255), 1, lineType=cv2.LINE_AA)  # pylint: disable=no-member

			cv2.putText(frame, str(frame_index), position[:2], cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness=2, lineType=cv2.LINE_AA)  # pylint: disable=no-member
			cv2.putText(frame, str(frame_index), position[:2], cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), thickness=1, lineType=cv2.LINE_AA)  # pylint: disable=no-member

	def draw_position(self, frame, frame_index):
		position = self.get_position(frame_index)

		if position != None:
			cv2.circle(frame, position[:2], 5, (255, 255, 255), -1, lineType=cv2.LINE_AA)  # pylint: disable=no-member
			cv2.circle(frame, position[:2], 3, (255, 0, 255), -1, lineType=cv2.LINE_AA)  # pylint: disable=no-member


	def draw(self, frame, frame_index):

		self.draw_position(frame, frame_index)

		# Draw the selected blobs
		for item in self._sel_pts: #store a temporary path for interpolation visualization
			self.draw_circle(frame, item)

		# Draw the selected path #store a temporary path for interpolation visualization
		if 1 <= len(self._sel_pts) == 2: #store a temporary path for interpolation visualization
			start = self._sel_pts[0] #store a temporary path for interpolation visualization
			end = frame_index if len(self._sel_pts)==1 else self._sel_pts[1]
			for i in range(start, end - 1):
				v1 = self[i]
				v2 = self[i + 1]
				if v1 != None and v2 != None:
					cv2.line(frame, v1, v2, (0, 0, 255), 1)

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
	def interpolation_mode(self): return None

	@property
	def object2d(self): return self._object2d
	@object2d.setter
	def object2d(self,value): self._object2d = value

	@property
	def name(self): return self._name
	@name.setter
	def name(self, value): self._name = value