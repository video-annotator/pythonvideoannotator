import cv2
from pysettings import conf
from PyQt4 import QtCore, QtGui
from pythonvideoannotator.modules.patheditor.object2d.object2d              import Object2d
from pythonvideoannotator.modules.patheditor.ChooseColumnsWindow            import ChooseColumnsWindow
from pythonvideoannotator.modules.patheditor.objects_window                 import ObjectsWindow

from pyforms.Controls import ControlDockWidget

class Module(object):

	def __init__(self):
		"""
		This implements the Path edition functionality
		"""
		super(Module, self).__init__()

		self._right_docker          = ControlDockWidget('Objects list',side=ControlDockWidget.SIDE_RIGHT)        
		self._right_docker.value    = self._objects_window = ObjectsWindow(parent=self)
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
		self._objects_window.draw(frame)
		return frame

