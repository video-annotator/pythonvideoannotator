import csv, cv2, os
from pysettings import conf
from pyforms import BaseWidget
from PyQt4 import QtCore, QtGui
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlCombo
from pyforms.Controls import ControlLabel
from pythonvideoannotator.models.objects.object2d.object2d_io import Object2dIO


class Object2dGUI(Object2dIO, BaseWidget):

	def __init__(self, name=None,parent=None):
		BaseWidget.__init__(self, '2D Object', parentWindow=parent)
		Object2dIO.__init__(self, name)
		self._parent = parent

		self.__create_tree_nodes()

	def create_path_dataset(self): 
		path = super(Object2dGUI, self).create_path_dataset()
		self.mainwindow.add_dataset_evt(path)
		return path
	

	######################################################################
	### AUX FUNCTIONS ####################################################
	######################################################################

	def __create_tree_nodes(self):
		self.treenode = self.tree.createChild(self.name, icon=conf.ANNOTATOR_ICON_OBJECT )
		self.tree.addPopupMenuOption(
			label='Create a path dataset', 
			functionAction=self.create_path_dataset, 
			item=self.treenode, icon=conf.ANNOTATOR_ICON_TIMELINE
		)
		self.treenode.win = self
		
		
		
	

	def create_motion_tree_nodes(self):
		
		self.treenode_motion = self.tree.createChild('Motion', icon=conf.ANNOTATOR_ICON_PATH, parent=self.treenode )
		variation_treenode 	 = self.tree.createChild('x', icon=conf.ANNOTATOR_ICON_X, parent=self.treenode_motion )
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_motion_to_timeline_evt, item=variation_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_motion_variation_to_timeline_evt, item=variation_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		
		self.treenode_motion.obj = variation_treenode.obj = self


	######################################################################
	### PROPERTIES #######################################################
	######################################################################

	@property
	def mainwindow(self): return self._parent.mainwindow

	@property 
	def tree(self): return self._parent._objects