#! /usr/bin/python2
# -*- coding: utf-8 -*-
import os
from pysettings import conf
from pyforms import BaseWidget
from PyQt4 import QtGui, QtCore

from pyforms.Controls import ControlButton
from pyforms.Controls import ControlList
from pyforms.Controls import ControlEmptyWidget

from pyforms.dialogs  import CsvParserDialog

from pythonvideoannotator.modules.patheditor.object2d.object2d import Object2d

class ObjectsWindow(BaseWidget):
	"""Application form"""

	def __init__(self, parent=None):
		super(ObjectsWindow, self).__init__('Objects window', parentWindow=parent)

		self._import_btn 	= ControlButton('Import file')
		self._objects 		= ControlList('Objects', plusFunction=self.__add_object, minusFunction=self.__remove_object)
		self._details 		= ControlEmptyWidget('Details')
		self._formset 		= [ '_import_btn','_objects','_details' ]


		self._csvparser_win = CsvParserDialog(self)
		self._csvparser_win.zField.hide()
		self._csvparser_win.loadFileEvent 	= self.__import_file_evt

		self._objects.itemSelectionChanged 	= self.__object_itemSelectionChanged
		self._import_btn.value 				= self._csvparser_win.show


		self._objs = []
		


	def __import_file_evt(self):
		filename = os.path.basename( self._csvparser_win.filename )

		self._objects += [filename]
		self._objs.append( Object2d(filename) )


	def __object_itemSelectionChanged(self):
		if self._objects.mouseSelectedRowIndex is not None:
			self._details.value = self._objs[ self._objects.mouseSelectedRowIndex ]
			self._details.value.show()
		
	def __add_object(self):
		self._objects += ['New object {0}'.format(len(self._objects.value))]
		obj = Object2d()
		self._objs.append( obj )
		
		return obj

	def __remove_object(self):
		self._objs.pop( self._objects.mouseSelectedRowIndex )
		self._objects -= -1

