import sys, os, shutil, re, pyforms, numpy as np, cv2
from pyforms 			 import BaseWidget
from pyforms.Controls 	 import ControlFile
from pyforms.Controls 	 import ControlPlayer
from pyforms.Controls 	 import ControlButton
from pyforms.Controls 	 import ControlNumber
from pyforms.Controls 	 import ControlSlider
from pyforms.Controls 	 import ControlCheckBox
from pyforms.Controls 	 import ControlText
from pyforms.Controls 	 import ControlCheckBoxList
from pyforms.Controls 	 import ControlProgress
from pythonvideoannotator.modules.motioncounter.motioncounter.motion_object import MotionObject
from PyQt4 import QtGui
from pythonvideoannotator.models.objects.object2d.datasets.path import Path

class MotionCounter(BaseWidget):

	def __init__(self, parent=None):
		BaseWidget.__init__(self, 'Motion counter', parentWindow=parent)

		self.layout().setContentsMargins(10, 5, 10, 5)
		self.setMinimumHeight(300)
		self.setMinimumWidth(500)

		self._player			= ControlPlayer('Player')
		self._objects 			= ControlCheckBoxList('Objects')
		self._show_diff			= ControlCheckBox('Show diffs boxes')
		self._threshold_slider	= ControlSlider('Threshold', 5, 1, 255)
		self._radius_slider		= ControlSlider('Radius', 30, 1, 200)
		self._apply  			= ControlButton('Apply')
		self._progress  		= ControlProgress('Progress')

		
		self._formset = [
			'_objects',
			'=',
			('_threshold_slider', '_radius_slider', '_show_diff'),
			'_player',
			'_apply',
			'_progress'
		]

		self._player.processFrame 	= self.__process_frame

		self._threshold_slider.changed 	= self.__threshold_changed_event
		self._radius_slider.changed 	= self.__radius_changed_event
		self._objects.changed 			= self.__objects_changed_evt
		self._apply.value 				= self.__apply_btn_evt

		self._progress.hide()

		self._objects_list  = []
		self._selected_objs = []

	def __apply_btn_evt(self):
		self._player.video_index = 0
		cap = self._player.value

		self._progress.value = 0
		self._progress.max = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
		self._progress.show()

		for obj in self.objects: obj.create_motion_tree_nodes()
		
		while True:
			res, frame = cap.read()
			if not res: break

			index = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
			for obj in self.objects:
				motion = obj.process(index, frame)
				if motion is not None: obj.set_motion(index, motion)
			self._progress.value = index
	
		self._progress.hide()

	def __objects_changed_evt(self):
		self._selected_objs = [MotionObject(self._objects_dict[name]) for name in self._objects.value]

	@property
	def video_filename(self): return None
	@video_filename.setter
	def video_filename(self, value): self._player.value = value

	@property
	def objects(self): return self._selected_objs
	@objects.setter
	def objects(self, value):  self._objects.value = value
	

	def add_dataset_evt(self, dataset):
		if isinstance(dataset, Path):
			self._objects += [dataset, True]
			#self._objects_list.append(dataset)

	def remove_dataset_evt(self, dataset):
		if isinstance(dataset, Path):
			self._objects -= dataset

	
		

	def __process_frame(self, frame):
		index = self._player.video_index
		
		for obj in self.objects: obj.process(index, frame)
		for obj in self.objects: obj.draw(index, frame, self._show_diff.value)

		return frame

	def __threshold_changed_event(self): self.threshold = self._threshold_slider.value
	def __radius_changed_event(self): 	 self.radius = self._radius_slider.value

	@property
	def radius(self): return self._radius_slider.value
	@radius.setter
	def radius(self, value): 
		for f in self.objects: f.radius = value

	@property
	def threshold(self): return self._threshold_slider.value
	@threshold.setter
	def threshold(self, value): 
		for f in self.objects: f.threshold = value




if __name__ == "__main__": pyforms.startApp(Main)