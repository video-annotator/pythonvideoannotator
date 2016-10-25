import cv2
from pysettings import conf
from pythonvideoannotator.modules.motioncalc.motioncounter.motion_counter import MotionCounter


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


	def add_object_evt(self, obj):
		super(Module, self).add_object_evt(obj)
		self._motion_window.add_object_evt(obj)

	def remove_object_evt(self, obj, i):
		super(Module, self).remove_object_evt(obj, i)
		self._motion_window.remove_object_evt(obj, i)


	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	