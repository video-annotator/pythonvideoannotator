import cv2
from pysettings import conf
from pythonvideoannotator.modules.tracking.tracking_window import TrackingWindow


class Module(object):

	def __init__(self):
		"""
		This implements the Path edition functionality
		"""
		super(Module, self).__init__()


		self._tracking_window = TrackingWindow(self)

		self.mainmenu.append(
			{'Tracking': [
					{'Open tracking': self._tracking_window.show },
			]}
		)

	def video_changed_evt(self):
		super(Module, self).video_changed_evt()
		self._tracking_window.video_filename = self._video.value
	

	def add_dataset_evt(self, dataset):
		super(Module, self).add_dataset_evt(dataset)
		self._tracking_window.add_dataset_evt(dataset)

	def remove_dataset_evt(self, dataset):
		super(Module, self).remove_dataset_evt(dataset)
		self._tracking_window.remove_dataset_evt(dataset)


	
	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	
	def save(self, data, project_path=None):
		data = super(Module, self).save(data, project_path)
		data['tracking-settings'] = self._tracking_window.save({})
		return data

	def load(self, data, project_path=None):
		super(Module, self).load(data, project_path)
		if 'tracking-settings' in data: self._tracking_window.load(data['tracking-settings'])
