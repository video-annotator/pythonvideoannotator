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

	


