import csv, cv2
from pyforms import BaseWidget
from PyQt4 import QtCore, QtGui
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlCombo
from pyforms.Controls import ControlLabel
from pythonvideoannotator.modules.patheditor.object2d.moment import Moment
from pythonvideoannotator.modules.patheditor.object2d.interpolation import interpolate_positions


class Object2d(BaseWidget):

	def __init__(self, 
		parent=None, 	filename=None, 	sep=',', 
		frameCol=0, 	xCol=1, 		yCol=2, 	zCol=None
	):
		
		super(Object2d, self).__init__('2D Object')
		self._parent 	= parent
		self._path 	 	= [] #path of the object
		self._tmp_path 	= [] #store a temporary path to pre-visualize de interpolation
		self._sel_pts 	= [] #store the selected points

		Moment.FRAME_COL = frameCol
		Moment.X_COL 	 = xCol
		Moment.Y_COL 	 = yCol
		Moment.Z_COL 	 = zCol
		self._separator  = sep
		if filename != None and filename != '': self.import_csv(filename)


		self._mark_pto_btn 	  	  = ControlButton('Mark point', checkable=True)
		self._del_path_btn 	  	  = ControlButton('Delete path')
		self._interpolation_title = ControlLabel('Interpolation')
		self._interpolation_mode  = ControlCombo('Mode')
		self._interpolate_btn 	  = ControlButton('Apply')

		self._formset = [ 
			'_mark_pto_btn',
			'_del_path_btn',
			'_interpolation_title',
			('_interpolation_mode','_interpolate_btn')			
		]


		self._interpolation_title.value = 'INTERPOLATION'
		
		self._interpolation_mode.addItem("Auto")
		self._interpolation_mode.addItem("Linear", 'slinear')
		self._interpolation_mode.addItem("Quadratic", 'quadratic')
		self._interpolation_mode.addItem("Cubic", 'cubic')

		#### EVENTS ####
		self._del_path_btn.value 		 = self.__del_path_btn_evt
		self._interpolation_mode.changed = self.__interpolation_mode_changed_evt
		self._interpolate_btn.value 	 = self.__interpolate_btn_evt
		################

		self._del_path_btn.hide()
		self._interpolate_btn.hide()
		self._interpolation_mode.hide()
		self._interpolation_title.hide()

	######################################################################
	### GUI EVENTS #######################################################
	######################################################################

	def __interpolate_btn_evt(self): 
		#store a temporary path for interpolation visualization
		if len(self._sel_pts) == 2:
			mode = None if self._interpolation_mode.value=='Auto' else self._interpolation_mode.value		 #store a temporary path for interpolation visualization
			self.interpolate_range(
				self._sel_pts[0].frame, self._sel_pts[1].frame, interpolation_mode=mode)
			self.mainwindow._player.refresh()
		else:
			QtGui.QMessageBox.about(self, "Error", "You need to select 2 frames.")

	def __interpolation_mode_changed_evt(self): 
		#store a temporary path for interpolation visualization
		if len(self._sel_pts) == 2:

			self.__calculate_tmp_interpolation()
			self.mainwindow._player.refresh()

	def __calculate_tmp_interpolation(self): 
		#store a temporary path for interpolation visualization
		begin 	= self._sel_pts[0].frame #store a temporary path for interpolation visualization
		end 	= self._sel_pts[1].frame
		positions = []
		for i in range(begin, end + 1):
			data = self._path[i]
			if data != None and data.position != None:
				positions.append([i, data.position])

		mode = None if self._interpolation_mode.value=='Auto' else self._interpolation_mode.value
		positions = interpolate_positions(positions, begin, end, interpolation_mode=mode)
		self._tmp_path = [pos for frame, pos in positions]

	def __del_path_btn_evt(self): #store a temporary path for interpolation visualization
		if len(self._sel_pts) == 2:
			reply = QtGui.QMessageBox.question(self, 'Confirmation',
											   "Are you sure you want to delete this path?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
			if reply == QtGui.QMessageBox.Yes: #store a temporary path for interpolation visualization
				start, end = self._sel_pts[0].frame, self._sel_pts[1].frame
				self.delete_range(start + 1, end)
				self.mainwindow._player.refresh()
		else:
			QtGui.QMessageBox.about(self, "Error", "You need to select 2 frames.")



	######################################################################
	### CLASS FUNCTIONS ##################################################
	######################################################################

	def __len__(self): return len(self._path)

	def __getitem__(self, index): return self._path[index] if index<len(self) else None
			
	######################################################################
	### IO FUNCTIONS #####################################################
	######################################################################

	def import_csv(self, filename):
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
		with open(filename, 'wb') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=self._separator)
			#spamwriter.writerow(['Frame','Name','pos X','pos Y','head X','head Y','tail X','tail Y'])
			for data in self._path:
				if data != None:
					spamwriter.writerow(data.row)


	######################################################################
	### DATA MODIFICATION AND ACCESS #####################################
	######################################################################

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
				v = Moment()
				v.frame = frame
				v.position = pos
				self._path[frame] = v

		self._tmp_path = []

	
	def set_position(self, index, x, y):
		# add positions in case they do not exists
		if index >= len(self._path):
			for i in range(len(self._path), index + 1):
				self._path.append(None)

		if self._path[index] == None:
			v = Moment()
			v.frame = index
			v.position = (x, y)
			self._path[index] = v
		else:
			v = self._path[index]
			v.position = (x, y)

	def select(self, index, x, y):
		if index <= len(self._path) and index>=0:
			item = self._path[index]
			if item != None and item.collide(x, y):
				return item
		return None

	

	
	######################################################################
	### VIDEO EVENTS #####################################################
	######################################################################

	def on_click(self, event, x, y):

		if event.button() == 1:
			frame_index = self.mainwindow._player.video_index

			if self._mark_pto_btn.checked:
				self.set_position(frame_index, x, y)
				self._mark_pto_btn.checked = False

			else:
				selected = self.select(frame_index, x, y)
				if selected != None:
					modifier = int(event.modifiers())
					# If the control button is pressed will add the blob to the previous selections
					if modifier == QtCore.Qt.ControlModifier:
						if selected not in self._sel_pts: #store a temporary path for interpolation visualization
							self._sel_pts.append(selected)
						else:
							# Remove the blob in case it was selected before #store a temporary path for interpolation visualization
							self._sel_pts.remove(selected)
					else:
						# The control key was not pressed so will select only one #store a temporary path for interpolation visualization
						self._sel_pts =[selected]
				else: #store a temporary path for interpolation visualization
					self._sel_pts =[]  # No object selected: remove previous selections #store a temporary path for interpolation visualization
				self._sel_pts =sorted(self._sel_pts, key=lambda x: x.frame)

 			#store a temporary path for interpolation visualization
			if len(self._sel_pts) == 2: 
				#########################################################
				#In case 2 frames are selected, draw the temporary path##
				#########################################################
				self.__calculate_tmp_interpolation()
				self._interpolate_btn.show()
				self._interpolation_mode.show()
				self._interpolation_title.show()
				self._del_path_btn.show()
				#########################################################
			else:
				self._interpolate_btn.hide()
				self._interpolation_mode.hide()
				self._interpolation_title.hide()
				self._del_path_btn.hide()
				
			
			self.mainwindow._player.refresh()



	def draw(self, frame):
		frame_index = self.mainwindow._player.video_index

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
	def mainwindow(self): return self._parent.mainwindow
	
