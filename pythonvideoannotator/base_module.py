#! /usr/bin/python2
# -*- coding: utf-8 -*-
import os
from pysettings import conf
from pyforms import BaseWidget


if conf.PYFORMS_USE_QT5:
	from PyQt5 import QtGui, QtCore	
	from PyQt5.QtWidgets import QApplication, QFileDialog
else:
	from PyQt4 import QtGui, QtCore	
	from PyQt4.QtGui import QApplication, QFileDialog

from pyforms.Controls import ControlPlayer
from pyforms.Controls import ControlFile
from pyforms.Controls import ControlEventTimeline
from pyforms.Controls import ControlDockWidget

from pythonvideoannotator_models_gui.models import Project
from pythonvideoannotator_models_gui.dialogs.dialog import Dialog


def Exit(): exit()

class BaseModule(BaseWidget):
	"""Application form"""

	def __init__(self):
		global conf;
		conf += 'pythonvideoannotator.resources'  # Resources can only be loaded after pyqt is running

		super(BaseModule, self).__init__('Video annotation editor')
		
		self._project  = Project(parent=self)
		Dialog.project = self._project

		self._player 	= ControlPlayer("Player")
		self._time 		= ControlEventTimeline('Time')
		self._dock 		= ControlDockWidget("Timeline", side='bottom', order=1, margin=5)

		self.formset 	= ['_player']

		self._dock.value 					= self._time
		self._player.process_frame_event 	= self.process_frame_event
		self._player.click_event			= self.on_player_click_event
		self._time.key_release_event 		= self.__timeline_key_release_event

		self.load_order = []

		self.mainmenu.insert(0,
			{'File': [
				{'Open': self.__open_project_event, 'icon': conf.ANNOTATOR_ICON_OPEN},
				'-',
				{'Save': self.__save_project_event , 'icon': conf.ANNOTATOR_ICON_SAVE},
				{'Save as': self.__save_project_as_event, 'icon': conf.ANNOTATOR_ICON_SAVE},
				'-',
				{'Exit': QApplication.closeAllWindows, 'icon': conf.ANNOTATOR_ICON_EXIT} 
			] }			
		)
		self.mainmenu.insert(1, {'Modules': []} )
		self.mainmenu.insert(2, {'Windows': []} )



	######################################################################################
	#### FUNCTIONS #######################################################################
	######################################################################################

		
	def init_form(self):
		super(BaseModule, self).init_form()

		if conf.CHART_FILE_PATH: self._time.import_chart(*conf.CHART_FILE_PATH)
		if conf.PROJECT_PATH: 
			self.load_project(conf.PROJECT_PATH)
			


	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	def save(self, data, project_path=None): return data

	def load(self, data, project_path=None): pass

	def save_project(self, project_path=None):
		if project_path is None:
			print(project_path)
			project_path = QFileDialog.getExistingDirectory(self, "Select the project directory")

		if project_path is not None and str(project_path)!='':
			project_path = str(project_path)
			self.save({}, project_path)			

	def load_project(self, project_path=None):
		if project_path is None:
			project_path = QFileDialog.getExistingDirectory(self, "Select the project directory")
		if project_path is not None and str(project_path)!='':
			self.load({}, str(project_path) )



	######################################################################################
	#### EVENTS ##########################################################################
	######################################################################################

	def on_player_click_event(self, event, x, y):
		"""
		Code to select a blob with the mouse
		"""
		super(VideoAnnotationEditor, self).on_player_click_event(event, x, y)
		self._player.refresh()

	def process_frame_event(self, frame):
		"""
		Function called before render each frame
		"""
		return frame



	def __open_project_event(self): self.load_project()

	def __save_project_event(self): self.save_project(self._project.directory)

	def __save_project_as_event(self): self.save_project()
	
	def __timeline_key_release_event(self, event):
		"""
		Control video playback using the space bar to Play/Pause
		"""
		if event.key() == QtCore.Qt.Key_Space:
			self._player.stop() if self._player.is_playing else _player._video.play()
		




	######################################################################################
	#### PROPERTIES ######################################################################
	######################################################################################

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