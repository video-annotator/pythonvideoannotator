#! /usr/bin/python2
# -*- coding: utf-8 -*-
import os
from pysettings import conf
from pyforms import BaseWidget
from PyQt4 import QtGui, QtCore
from pythonvideoannotator.utils.tools import list_folders_in_path
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlTree
from pyforms.Controls import ControlList
from pyforms.Controls import ControlEmptyWidget
from send2trash import send2trash
from pyforms.dialogs  import CsvParserDialog

from pythonvideoannotator.models.objects.objects_gui import ObjectsGUI
from pythonvideoannotator.models.objects.object2d import Object2d

class ObjectsIO(ObjectsGUI):

	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################
	
	def save(self, data, objects_path=None):
		for obj in self.objects: obj.save(data, objects_path)

		#remove from the setups directory the unused setup files
		paths = [os.path.join(objects_path, o.name) for o in self.objects]
		for path in list_folders_in_path(objects_path):
			if path not in paths: send2trash(path)

		return data

	def load(self, data, objects_path=None):
		for object_path in list_folders_in_path(objects_path):
			name = os.path.basename(object_path)
			obj = self.create_object(name)
			obj.load(data, object_path)