import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlList
from pyforms.Controls import ControlCombo
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlCheckBox
from pyforms.Controls import ControlCheckBoxList
from pyforms.Controls import ControlEmptyWidget

from mcvgui.dialogs.simple_image_filter_workflow import SimpleImageFilterWorkflow

class TrackingWindow(BaseWidget):

	def __init__(self, parent=None):
		super(TrackingWindow, self).__init__('Tracking', parentWindow=parent)
		self.mainwindow = parent

		self.layout().setMargin(5)

		self._start = ControlText('Start on frame')
		self._end 	= ControlText('End on frame')

		self._objects 	 = ControlCheckBoxList('Select the objects to track')
		
		self._formset = [
			{ 
				'Basic configuration': [
					('_start', '_end'),	
					'_objects',
				],
				'Image filter': ['_filter']
			}
		]

		self._filter = ControlEmptyWidget('Filter')

		self._filter.value = SimpleImageFilterWorkflow()

		
	def show(self):
		super(TrackingWindow, self).show()

		self._objects.clear()
		for obj in self.mainwindow.objects:
			self._objects += (obj.name, False)

		
		


if __name__ == '__main__': 
	pyforms.startApp(TrackingWindow)
