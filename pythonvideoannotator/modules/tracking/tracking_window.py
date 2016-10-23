import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlList
from pyforms.Controls import ControlCombo
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlCheckBox
from pyforms.Controls import ControlCheckBoxList
from pyforms.Controls import ControlEmptyWidget
from pyforms.Controls import ControlToolBox
from pyforms.Controls import ControlProgress

from mcvgui.dialogs.simple_image_filter_workflow import SimpleImageFilterWorkflow

class TrackingWindow(BaseWidget):

	def __init__(self, parent=None):
		super(TrackingWindow, self).__init__('Tracking', parentWindow=parent)
		self.mainwindow = parent

		self.layout().setMargin(5)
		self.setMinimumHeight(1000)
		self.setMinimumWidth(1200)


		self._toolbox 	= ControlToolBox()
		self._start 	= ControlText('Start on frame',"0")
		self._end 		= ControlText('End on frame', "10")
		self._objects 	= ControlCheckBoxList('Select the objects to track')
		self._filter_panel 	= ControlEmptyWidget('Filter')
		self._progress  = ControlProgress('Progress')
		self._apply 	= ControlButton('Apply')

		self._formset = ['_toolbox','_apply', '_progress']


		self._toolbox.value = [ 
			('TRACKING CONFIGURATION',  [ (self._start,self._end), self._objects ] 	),
			('IMAGE FILTERING', 		[self._filter_panel]						)

		]

		self._filter = SimpleImageFilterWorkflow(video=self.mainwindow._video.value)
		self._filter_panel.value = self._filter
		self._apply.value	= self.__apply_evt
		self._progress.hide()

	@property
	def player(self):
		return self._filter._player
	
	@property
	def video_filename(self): return self._video_filename if hasattr(self,'_video_filename') else None
	@video_filename.setter
	def video_filename(self, value):  self._filter.filename = value

	

	def __apply_evt(self):
		start = eval(self._start.value)
		end   = eval(self._end.value)
		self._progress.min = start
		self._progress.max = end
		self._progress.show()

		self.player.video_index = start
		cap = self.player.value
		for index in range(start, end+1):
			res, frame = cap.read()
			if not res: break

			blobs = self._filter.process(frame)
			for blob in blobs:
				blob.draw(frame)

			self.player.image = frame
			self._progress.value = index
		
		
	def show(self):
		super(TrackingWindow, self).show()
		self._objects.clear()
		for obj in self.mainwindow.objects: self._objects += (obj.name, False)

		
		


if __name__ == '__main__': 
	pyforms.startApp(TrackingWindow)
