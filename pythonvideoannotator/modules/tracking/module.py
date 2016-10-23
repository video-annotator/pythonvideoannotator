import cv2
from pysettings import conf
from pythonvideoannotator.modules.tracking.tracking_window import TrackingWindow


class Module(object):

	def __init__(self):
		"""
		This implements the Path edition functionality
		"""
		super(Module, self).__init__()


		self._window = TrackingWindow(self)

		self.mainmenu.append(
			{'Tracking': [
					{'Open tracking': self._window.show },
			]}
		)

	def video_changed_evt(self):
		super(Module, self).video_changed_evt()
		self._window.video_filename = self._video.value
	


