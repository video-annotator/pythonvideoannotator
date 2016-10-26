import csv, cv2, os
from pysettings import conf
from pyforms import BaseWidget
from PyQt4 import QtCore, QtGui
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlCombo
from pyforms.Controls import ControlLabel
from pythonvideoannotator.modules.patheditor.objects.object2d.object2d_io import Object2dIO
from pythonvideoannotator.modules.patheditor.objects.object2d.datasets.path import Path

class Object2dGUI(Object2dIO, BaseWidget):

	def __init__(self, name=None,parent=None):
		BaseWidget.__init__(self, '2D Object', parentWindow=parent)
		Object2dIO.__init__(self, name)
		self._parent = parent

		self.__create_tree_nodes()
	

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
		
		
		"""
		self.treenode_pos = self.tree.createChild('position', icon=conf.ANNOTATOR_ICON_PATH, parent=self.treenode )
		x_treenode = self.tree.createChild('x', icon=conf.ANNOTATOR_ICON_X, parent=self.treenode_pos )
		y_treenode = self.tree.createChild('y', icon=conf.ANNOTATOR_ICON_Y, parent=self.treenode_pos )
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_pos_x_to_timeline_evt, item=x_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_pos_y_to_timeline_evt, item=y_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		
		self.treenode_vel = self.tree.createChild('velocity', icon=conf.ANNOTATOR_ICON_VELOCITY, parent=self.treenode_pos )
		vx_treenode = self.tree.createChild('x', icon=conf.ANNOTATOR_ICON_X, parent=self.treenode_vel )
		vy_treenode = self.tree.createChild('y', icon=conf.ANNOTATOR_ICON_Y, parent=self.treenode_vel )
		absv_treenode = self.tree.createChild('absolute', icon=conf.ANNOTATOR_ICON_Y, parent=self.treenode_vel )
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_vel_x_to_timeline_evt, item=vx_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_vel_y_to_timeline_evt, item=vy_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_absvel_to_timeline_evt, item=absv_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		
		self.treenode_acc = self.tree.createChild('acceleration', icon=conf.ANNOTATOR_ICON_ACCELERATION, parent=self.treenode_pos )
		ax_treenode = self.tree.createChild('x', icon=conf.ANNOTATOR_ICON_X, parent=self.treenode_acc )
		ay_treenode = self.tree.createChild('y', icon=conf.ANNOTATOR_ICON_Y, parent=self.treenode_acc )
		absa_treenode = self.tree.createChild('absolute', icon=conf.ANNOTATOR_ICON_Y, parent=self.treenode_acc )
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_acc_x_to_timeline_evt, item=ax_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_acc_y_to_timeline_evt, item=ay_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_absacc_to_timeline_evt, item=absa_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		

		y_treenode.obj = x_treenode.obj = self.treenode_pos.obj = \
		absv_treenode.obj = vy_treenode.obj = vx_treenode.obj = self.treenode_vel.obj = \
		absa_treenode.obj = ay_treenode.obj = ax_treenode.obj = self.treenode_acc.obj = \
		self.treenode.obj = self"""

	def create_path_dataset(self): 
		path = Path(self)

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