import cv2, os
from pysettings import conf
from PyQt4 import QtCore, QtGui
from pythonvideoannotator.utils.tools import list_folders_in_path
from pythonvideoannotator.modules.patheditor.objects import Objects

from pyforms.Controls import ControlDockWidget

class Module(object):

	def __init__(self):
		"""
		This implements the Path edition functionality
		"""
		super(Module, self).__init__()

		self._right_docker          = ControlDockWidget('Objects list',side=ControlDockWidget.SIDE_RIGHT)        
		self._right_docker.value    = self._objects_window = Objects(parent=self)
		#self._right_docker.hide()

		
		self.mainmenu.append(
			{'Path': [
					{'Show objects': self._right_docker.show },
			]}
		)

	def onPlayerClick(self, event, x, y): 
		self._objects_window.on_click(event, x, y)


	def process_frame(self, frame):
		"""
		Function called before render each frame
		"""
		self._objects_window.draw(frame, self._player.video_index)
		return frame

	def add_object_evt(self, obj): pass

	def remove_object_evt(self, obj, i): pass

	def add_chart(self, name, data):  self._time.add_chart(name, data)



	@property
	def objects(self): return self._objects_window.objects

	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	
	def save(self, data, project_path=None):
		data = super(Module, self).save(data, project_path)
		
		objects_path = os.path.join(project_path, 'objects')
		if not os.path.exists(objects_path): os.makedirs(objects_path)
		
		return self._objects_window.save(data, objects_path)


	def load(self, data, project_path=None):
		data = super(Module, self).load(data, project_path)

		objects_path = os.path.join(project_path, 'objects')
		self._objects_window.load(data, objects_path)
