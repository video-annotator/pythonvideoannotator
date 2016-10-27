import csv, cv2, os
from pysettings import conf
from pyforms import BaseWidget
from PyQt4 import QtCore, QtGui
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlCombo
from pyforms.Controls import ControlLabel
from pyforms.Controls import ControlText
from pythonvideoannotator.models.objects.object2d.object2d_io import Object2dIO


class Object2dGUI(Object2dIO, BaseWidget):

	def __init__(self, objects_set):
		BaseWidget.__init__(self, '2D Object', parentWindow=objects_set)
		Object2dIO.__init__(self, objects_set)

		self._name = ControlText('Name')

		self._formset = ['_name']

		self._name.changed = self.__name_changed_evt

	

	######################################################################
	### EVENTS ###########################################################
	######################################################################

	def __name_changed_evt(self):
		self._name_changed_activated = True
		self.name = self._name.value
		del self._name_changed_activated

	def name_updated(self, newname): pass

	######################################################################
	### PROPERTIES #######################################################
	######################################################################

	@property
	def mainwindow(self): return self.objects_set.mainwindow

	@property
	def name(self): return self._name.value
	@name.setter
	def name(self, value):
		if not hasattr(self, '_name_changed_activated'): self._name.value = value
		if hasattr(self, 'treenode'): self.treenode.setText(0,value)
		self.name_updated(value)