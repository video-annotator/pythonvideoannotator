import cv2
from confapp import conf
from pythonvideoannotator_module_deeplab.deeplab_window import DeepLabWindow


class Module(object):

	def __init__(self):
		"""
		This implements the DeepLab functionality
		"""
		super(Module, self).__init__()
		self.deeplab_window = DeepLabWindow(self)

		self.mainmenu[1]['Modules'].append(
			{'DeepLab': self.deeplab_window.show },			
		)
