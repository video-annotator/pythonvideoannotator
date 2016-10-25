import pyforms, cv2
from pyforms import BaseWidget
from pyforms.Controls import ControlCheckBoxList
from pyforms.Controls import ControlPlayer
from pyforms.Controls import ControlCheckBox
from pyforms.Controls import ControlSlider
from pyforms.Controls import ControlButton

class MotionCalcWindow(BaseWidget):

	def __init__(self, parent=None, video=None):
		BaseWidget.__init__(self, 'Calc motion', parentWindow=parent)

		self.layout().setContentsMargins(10, 5, 10, 5)
		self.setMinimumHeight(300)
		self.setMinimumWidth(500)

		self._player   		= ControlPlayer('Player')
		self._objects 		= ControlCheckBoxList('Objects')
		self._usecircle  	= ControlCheckBox('Image filters')
		self._radius 		= ControlSlider('Radius', 30, 1, 200)
		self._apply  		= ControlButton('Apply')

		self._formset = [
			'_player',
			'=',
			('_usecircle', '_radius'),
			'_objects',
			'_apply'
		]

	@property
	def video_filename(self): return None
	@video_filename.setter
	def video_filename(self, value):
		self._player.value = value

	@property
	def objects(self): return None
	@objects.setter
	def objects(self, value): 
		self._objects.value = value
	

	def add_object_evt(self, obj):
		self._objects+= [obj.name, True]

	def remove_object_evt(self, obj, i):
		self._objects -= i

	
	