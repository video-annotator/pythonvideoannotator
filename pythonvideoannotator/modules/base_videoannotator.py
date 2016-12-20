#! /usr/bin/python2
# -*- coding: utf-8 -*-
import os, json
from pysettings import conf
from pyforms import BaseWidget
from PyQt4 import QtGui, QtCore
from pyforms.Controls import ControlPlayer
from pyforms.Controls import ControlFile
from pyforms.Controls import ControlEventTimeline
from pyforms.Controls import ControlDockWidget


def Exit(): exit()

class BaseVideoAnnotator(BaseWidget):
	"""Application form"""

	def __init__(self):
		global conf;
		conf += 'pythonvideoannotator.resources'  # Resources can only be loaded after pyqt is running

		super(BaseVideoAnnotator, self).__init__('Video annotation editor')

		self._player 	= ControlPlayer("Player")
		self._time 		= ControlEventTimeline('Time')
		self._dock 		= ControlDockWidget("Timeline", side='bottom', order=1, margin=5)
		self.formset 	= ['_player']

		self._dock.value 				= self._time
		self._player.process_frame_event = self.process_frame
		self._player.on_click_event		= self.onPlayerClick
		self._time.key_release_event 	= self.__time_key_release_event

		self.load_order = []

		self.mainmenu.insert(0,
			{'File': [
				{'Open': self.__open_project_evt, 'icon': conf.ANNOTATOR_ICON_OPEN},
				'-',
				{'Save': self.__save_project_evt , 'icon': conf.ANNOTATOR_ICON_SAVE},
				{'Save as': self.__save_project_as_evt, 'icon': conf.ANNOTATOR_ICON_SAVE},
				'-',
				{'Exit': Exit, 'icon': conf.ANNOTATOR_ICON_EXIT} 
			] }
		)
		self.mainmenu.insert(1, {'Modules': []} )

		self._current_project_path = None

	######################################################################################
	#### FUNCTIONS #######################################################################
	######################################################################################

		
	def init_form(self):
		super(BaseVideoAnnotator, self).init_form()

		if conf.CHART_FILE_PATH: self._time.import_chart(*conf.CHART_FILE_PATH)

		if conf.PROJECT_PATH: self.load_project(conf.PROJECT_PATH)


	def video_added_event(self, video): pass

	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	def save(self, data, project_path=None):
		return data

	def load(self, data, project_path=None):
		pass

	def save_project(self, project_path=None):
		if project_path is None:
			project_path = QtGui.QFileDialog.getExistingDirectory(self, "Select the project directory")
		
		if project_path is not None:
			project_filename = os.path.join(str(project_path), 'project.json')
			data = self.save({}, str(project_path))
			with open(project_filename, 'w') as outfile:
				json.dump(data, outfile)

			self._current_project_path = str(project_path)

	def load_project(self, project_path=None):
		if project_path is None:
			project_path = QtGui.QFileDialog.getExistingDirectory(self, "Select the project directory")
		if project_path is not None:
			project_filename = os.path.join(str(project_path), 'project.json')
			with open(project_filename, 'r') as outfile:
				data = json.load(outfile)
			self.load(data, str(project_path))
			self._current_project_path = str(project_path)
			


	######################################################################################
	#### EVENTS ##########################################################################
	######################################################################################

	def __open_project_evt(self): self.load_project()

	def __save_project_evt(self): self.save_project(self._current_project_path)

	def __save_project_as_evt(self): self.save_project()

	
	def __time_key_release_event(self, event):
		"""
		Control video playback using the space bar to Play/Pause
		"""
		if event.key() == QtCore.Qt.Key_Space:
			self._player.stop() if self._player.is_playing else _player._video.play()
		

	def onPlayerClick(self, event, x, y):
		"""
		Code to select a blob with the mouse
		"""
		super(VideoAnnotationEditor, self).onPlayerClick(event, x, y)
		self._player.refresh()

	def process_frame(self, frame):
		"""
		Function called before render each frame
		"""
		return frame

	@property
	def timeline(self): return self._time

	@property
	def player(self): return self._player
	
	@property
	def video(self): return self._player.value
	@video.setter
	def video(self, value): 
		self._player.value 		= value
		self._player.enabled 	= value is not None
		if value:
			self._time.max = self._player.max

	@property
	def project(self): return self._project