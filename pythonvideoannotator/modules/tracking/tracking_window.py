import pyforms, math, cv2
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlList
from pyforms.Controls import ControlCombo
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlCheckBox
from pyforms.Controls import ControlCheckBoxList
from pyforms.Controls import ControlEmptyWidget
from pyforms.Controls import ControlProgress

from mcvgui.dialogs.simple_image_filter_workflow import SimpleImageFilterWorkflow
from mcvapi.blobs.order_by_position import combinations

import json

class TrackingWindow(BaseWidget):

	def __init__(self, parent=None):
		super(TrackingWindow, self).__init__('Tracking', parentWindow=parent)
		self.mainwindow = parent

		self.layout().setMargin(5)
		self.setMinimumHeight(800)
		self.setMinimumWidth(1200)

		self._save_btn 		= ControlButton('Save')
		self._load_btn 		= ControlButton('Load')
		self._start 		= ControlText('Start on frame',"0")
		self._end 			= ControlText('End on frame', "10")
		self._objects 		= ControlCheckBoxList('Select the objects to track')
		self._filter_panel 	= ControlEmptyWidget('Filter')
		self._progress  	= ControlProgress('Progress')
		self._apply 		= ControlButton('Apply')

		self._formset = [
			('_save_btn','_load_btn'),
			('_start','_end'), 
			'_objects',
			'_filter_panel',
			'_apply',
			'_progress'
		]

		self.load_order = ['_start', '_end', '_filter_panel']


		self._filter 				= SimpleImageFilterWorkflow(video=self.mainwindow._video.value)
		self._filter_panel.value 	= self._filter
		self._apply.value			= self.__apply_evt
		self._load_btn.value 		= self.__load_btn_evt
		self._save_btn.value		= self.__save_btn_evt

		self._progress.hide()


	

	###########################################################################
	### IO FUNCTIONS ##########################################################
	###########################################################################

	
	###########################################################################
	### INTERFACE FUNCTIONS ###################################################
	###########################################################################

	def add_dataset_evt(self, dataset):
		self._objects+= [dataset, True]

	def remove_dataset_evt(self, dataset):
		self._objects -= dataset

	def __save_btn_evt(self):
		data = self.save({})
		with open('tracking.json', 'w') as outfile:
			json.dump(data, outfile)

	def __load_btn_evt(self):
		with open('tracking.json', 'r') as outfile:
			data = json.load(outfile)
			self.load(data)

	###########################################################################
	### PROPERTIES ############################################################
	###########################################################################


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

		objects = self.objects
		

		paths = None
		
		capture = self.player.value
		capture.set(cv2.CAP_PROP_POS_FRAMES, start); 
		

		
		for index in range(start, end+1):
			res, frame = capture.read()
			if not res: break

			paths = self._filter.processflow(frame)

			step = 16581375 / (len(paths)+1)
			for i, path in enumerate(paths): 


				rgb_int = step*(i+1)
				blue 	= rgb_int & 255
				green 	= (rgb_int >> 8) & 255
				red 	= (rgb_int >> 16) & 255
				c 		= (blue, green, red)
				path.draw(frame, color=c)
			
			self.player.image 	 = frame
			self._progress.value = index

		if paths is None: return

		objects = self.objects
		if len(paths)>len(objects):
			objects += [None for i in range(len(paths)-len(objects))]
		elif len(paths)<len(objects):
			paths += [None for i in range(len(objects)-len(paths))]

		classifications = []
		for comb in combinations( paths, objects):

			classification = 0
			for path, obj in comb:
				if not path or not obj: continue

				distances = []
				for i, b in enumerate(path.path):
					if b is None: continue 
					m = obj.get_moment(start + i)
					if m is None: continue 

					p0   = m.position
					p1 	 = path.centroid
					dist = math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
					
					distances.append( dist )

				classification += sum(distances)/len(distances)
			
			classifications.append( (classification, comb) )
			
		classifications = sorted(classifications, key=lambda x: x[0])
		for path, obj in classifications[0][1]:
			if obj is None: continue
			for index in range(start, end+1):
				b = path.path[index-start]
				if b:
					x,y = b
					obj.set_position(index, x, y)

		

		
	@property
	def objects(self): return self._objects.value
			
		
	


if __name__ == '__main__': 
	pyforms.startApp(TrackingWindow)
