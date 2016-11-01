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


from pythonvideoannotator.models.objects.object2d import Object2d

class ObjectsGUI(BaseWidget):
	"""Application form"""

	def __init__(self, parent=None):
		super(ObjectsGUI, self).__init__('Objects window', parentWindow=parent)
		self._parent = parent

		self._tree 			= ControlTree('')
		self._addobj 		= ControlButton('Add object')
		self._removeobj 	= ControlButton('Remove object')
		self._formset 		= [
			'_tree', 
			('_addobj', '_removeobj'),
		]

		
		## set csv import dialog ##################################################
		self._csvparser_win = CsvParserDialog(self)
		self._csvparser_win.zField.hide()
		self._csvparser_win.loadFileEvent = self.__import_file_evt

		## set controls ##########################################################
		self._tree.showHeader 			= False
		self._tree.itemSelectionChanged 	= self.__object_itemSelectionChanged
		self._addobj.value 					= self.__add_object
		self._removeobj.value 				= self.__remove_object

		self._addobj.icon = conf.ANNOTATOR_ICON_ADD
		self._removeobj.icon = conf.ANNOTATOR_ICON_REMOVE

		self._tree.addPopupMenuOption('Import', self._csvparser_win.show)
		self._tree.addPopupMenuOption('-')
		self._tree.addPopupMenuOption('Save', self.__save_tracking_file)
		self._tree.addPopupMenuOption('Save as', self.__export_tracking_file)


	######################################################################################
	#### AUX FUNCTIONS ###################################################################
	######################################################################################

	def create_object(self, name):
		obj2d = Object2d(self)
		obj2d.name = name
		self.mainwindow.add_object_evt(obj2d)

		return obj2d
		


	######################################################################################
	#### GUI EVENTS ######################################################################
	######################################################################################


	def __export_tracking_file(self):
		if self._tree.mouseSelectedRowIndex is not None:
			obj = self._objs[ self._tree.mouseSelectedRowIndex ]

			csvfilename = QtGui.QFileDialog.getSaveFileName(parent=self,
															caption="Save file",
															directory="",
															filter="*.csv",
															options=QtGui.QFileDialog.DontUseNativeDialog)

			if csvfilename != None and obj != None:
				obj.export_csv(csvfilename)

	def __save_tracking_file(self):
		if self._tree.mouseSelectedRowIndex is not None:
			obj = self._objs[ self._tree.mouseSelectedRowIndex ]

			csvfilename = obj.filename
			if csvfilename != '' and csvfilename != None and obj != None:

				reply = QtGui.QMessageBox.question(self, 'Please confirm',
												   "Are you sure you want to replace the file {0}?".format(csvfilename),
												   QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
				if reply == QtGui.QMessageBox.Yes: obj.export_csv(csvfilename)
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
			obj = Object2d(name, self)
			obj.import_csv(self._csvparser_win.filename, separator, frame, x, y, z)
			self._csvparser_win.close()
			self._tree += [ name ]


	def __object_itemSelectionChanged(self):
		if self._tree.mouseSelectedRowIndex is not None and hasattr(self._tree.selectedItem,'win'):
			self.mainwindow.details = self._tree.selectedItem.win
			self.mainwindow.details.show()
				
			
				

	def __add_object(self):
		name = 'New object {0}'.format(len(self._tree.value))
		obj2d = self.create_object(name)
		obj2d.create_path_dataset()
		
		return obj2d

	def __remove_object(self):
		if self._tree.mouseSelectedRowIndex is not None:

			if isinstance(self._tree.selectedItem.win, Object2d):
				self.mainwindow.remove_object_evt(self._tree.selectedItem.win)
				self._tree -= self._tree.selectedItem.win.treenode
			else:
				self.mainwindow.remove_object_evt(self._tree.selectedItem.object2d)
				self._tree -= self._tree.selectedItem.object2d.treenode
			
	
	######################################################################################
	#### PUBLIC FUNCTIONS ################################################################
	######################################################################################

	def player_on_click(self, event, x, y):
		if self._tree.mouseSelectedRowIndex is not None:
			obj = self._tree.selectedItem.win
			obj.on_click(event, x, y)

	def draw(self, frame, frame_index):
		if self._tree.mouseSelectedRowIndex is not None:
			obj = self._tree.selectedItem.win
			obj.draw(frame, frame_index)

	######################################################################################
	#### PROPERTIES ######################################################################
	######################################################################################

	@property
	def mainwindow(self): 	return self._parent

	@property
	def tree(self): 	return self._tree

	@property
	def objects(self):  	return [item.win for item in self._tree.value]
