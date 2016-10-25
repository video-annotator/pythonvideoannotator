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


from pythonvideoannotator.modules.patheditor.object2d.object2d import Object2d

class ObjectsWindow(BaseWidget):
	"""Application form"""

	def __init__(self, parent=None):
		super(ObjectsWindow, self).__init__('Objects window', parentWindow=parent)
		self._parent = parent

		self._objects 		= ControlTree('')
		self._addobj 		= ControlButton('Add object')
		self._removeobj 	= ControlButton('Remove object')
		self._details 		= ControlEmptyWidget('Details')
		self._formset 		= [
			'_objects', 
			('_addobj', '_removeobj'),
			'_details'
		]


		self._objects.showHeader = False
		self._csvparser_win = CsvParserDialog(self)
		self._csvparser_win.zField.hide()
		self._csvparser_win.loadFileEvent 	= self.__import_file_evt

		self._objects.itemSelectionChanged 	= self.__object_itemSelectionChanged
		self._addobj.value = self.__add_object
		self._removeobj.value = self.__remove_object

		self._objects.addPopupMenuOption('Import', self._csvparser_win.show)
		self._objects.addPopupMenuOption('-')
		self._objects.addPopupMenuOption('Save', self.__save_tracking_file)
		self._objects.addPopupMenuOption('Save as', self.__export_tracking_file)

		self._objs = []
		
	def initForm(self):
		super(ObjectsWindow, self).initForm()
		self._objects.iconsize = 36,36
		


	def __export_tracking_file(self):
		if self._objects.mouseSelectedRowIndex is not None:
			obj = self._objs[ self._objects.mouseSelectedRowIndex ]

			csvfilename = QtGui.QFileDialog.getSaveFileName(parent=self,
															caption="Save file",
															directory="",
															filter="*.csv",
															options=QtGui.QFileDialog.DontUseNativeDialog)

			if csvfilename != None and obj != None:
				obj.export_csv(csvfilename)

	def __save_tracking_file(self):
		if self._objects.mouseSelectedRowIndex is not None:
			obj = self._objs[ self._objects.mouseSelectedRowIndex ]

			csvfilename = obj.filename
			if csvfilename != '' and csvfilename != None and obj != None:

				reply = QtGui.QMessageBox.question(self, 'Please confirm',
												   "Are you sure you want to replace the file {0}?".format(csvfilename),
												   QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

				if reply == QtGui.QMessageBox.Yes:
					obj.export_csv(csvfilename)

			else:
				QtGui.QMessageBox.about(self, "No file imported", "No file imported yet.")


	def __import_file_evt(self):
		if self._csvparser_win.filename != None:

			separator 	= self._csvparser_win.separator
			frame 		= self._csvparser_win.frameColumn
			x 			= self._csvparser_win.xColumn
			y 			= self._csvparser_win.yColumn
			z 			= self._csvparser_win.zColumn

			name = os.path.basename( self._csvparser_win.filename )
			obj = Object2d(name, self, self._csvparser_win.filename, separator, frame, x, y, z)
			self._csvparser_win.close()
			self._objects += [ name ]
			self._objs.append( obj )


	def __object_itemSelectionChanged(self):
		if self._objects.mouseSelectedRowIndex is not None:
			self._details.value = self._objects.selectedItem.obj
			self._details.value.show()

	def create_object(self, name):
		obj 	 = Object2d(name, parent=self)
		obj.item = self._objects.createChild( name, icon=conf.ANNOTATOR_ICON_OBJECT )
		item = self._objects.createChild( 'datasets', icon=conf.ANNOTATOR_ICON_DATASETS,parent=obj.item )
		obj.item.obj = obj

		self._parent.add_object_evt(obj)
		return obj
		
	def __add_object(self):
		name = 'New object {0}'.format(len(self._objects.value))
		return self.create_object(name)

	def __remove_object(self):
		if self._objects.mouseSelectedRowIndex is not None:
			self._parent.remove_object_evt(self._objects.selectedItem.obj, self._objects.mouseSelectedRowIndex )
			self._objects -= -1


	def on_click(self, event, x, y):
		if self._objects.mouseSelectedRowIndex is not None:
			obj = self._objects.selectedItem.obj
			obj.on_click(event, x, y)

	def draw(self, frame):
		if self._objects.mouseSelectedRowIndex is not None:
			obj = self._objects.selectedItem.obj
			obj.draw(frame)

	@property
	def mainwindow(self): return self._parent

	@property
	def objects(self): 
		return [item.obj for item in self._objects.value]

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