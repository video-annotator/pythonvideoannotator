import cv2
from pysettings import conf
from pythonvideoannotator.modules.motioncounter.motioncounter.motion_counter import MotionCounter


class Module(object):

	def __init__(self):
		"""
		This implements the Path edition functionality
		"""
		super(Module, self).__init__()
		self._motion_window = MotionCounter(self)

		self.mainmenu.append(
			{'Motion': [
					{'Open motion': self._motion_window.show },
			]}
		)

	def video_changed_evt(self):
		super(Module, self).video_changed_evt()
		self._motion_window.video_filename = self._video.value



	def add_dataset_evt(self, dataset):
		super(Module, self).add_dataset_evt(dataset)
		self._motion_window.add_dataset_evt(dataset)

	def remove_dataset_evt(self, dataset):
		super(Module, self).remove_dataset_evt(dataset)
		self._motion_window.remove_dataset_evt(dataset)


	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	