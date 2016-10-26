from pysettings import conf
from pyforms import BaseWidget
from PyQt4 import QtCore, QtGui
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlCombo
from pyforms.Controls import ControlLabel
from pythonvideoannotator.models.objects.object2d.datasets.path.path_io import PathIO


class PathGUI(PathIO, BaseWidget):

	def __init__(self, object2d=None):
		BaseWidget.__init__(self, '2D Object', parentWindow=object2d)
		PathIO.__init__(self, object2d)

		self.__create_tree_nodes()

		self._mark_pto_btn 	  	  = ControlButton('Mark point', checkable=True)
		self._del_path_btn 	  	  = ControlButton('Delete path')
		self._interpolation_title = ControlLabel('Interpolation')
		self._interpolation_mode  = ControlCombo('Mode')
		self._interpolate_btn 	  = ControlButton('Apply')

		self._formset = [ 
			'_mark_pto_btn',
			'_del_path_btn',
			'_interpolation_title',
			('_interpolation_mode','_interpolate_btn')			
		]


		#### set controls ##############################################
		self._interpolation_title.value = 'INTERPOLATION'
		self._interpolation_mode.addItem("Auto")
		self._interpolation_mode.addItem("Linear", 'slinear')
		self._interpolation_mode.addItem("Quadratic", 'quadratic')
		self._interpolation_mode.addItem("Cubic", 'cubic')

		self._del_path_btn.hide()
		self._interpolate_btn.hide()
		self._interpolation_mode.hide()
		self._interpolation_title.hide()

		#### set events #################################################
		self._del_path_btn.value 		 = self.__del_path_btn_evt
		self._interpolation_mode.changed = self.__interpolation_mode_changed_evt
		self._interpolate_btn.value 	 = self.__interpolate_btn_evt



	######################################################################
	### AUX FUNCTIONS ####################################################
	######################################################################



	def __create_tree_nodes(self):

		self.treenode = self.tree.createChild(self.name, icon=conf.ANNOTATOR_ICON_PATH, parent=self.parent_treenode )
		self.tree.addPopupMenuOption(
			label='Remove', 
			functionAction=self.__remove_path_dataset, 
			item=self.treenode, icon=conf.ANNOTATOR_ICON_DELETE
		)
		

		self.treenode_pos = self.tree.createChild('position', icon=conf.ANNOTATOR_ICON_POSITION, parent=self.treenode )
		x_treenode = self.tree.createChild('x', icon=conf.ANNOTATOR_ICON_X, parent=self.treenode_pos )
		y_treenode = self.tree.createChild('y', icon=conf.ANNOTATOR_ICON_Y, parent=self.treenode_pos )
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_pos_x_to_timeline_evt, item=x_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_pos_y_to_timeline_evt, item=y_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		
		self.treenode_vel = self.tree.createChild('velocity', icon=conf.ANNOTATOR_ICON_VELOCITY, parent=self.treenode )
		vx_treenode = self.tree.createChild('x', icon=conf.ANNOTATOR_ICON_X, parent=self.treenode_vel )
		vy_treenode = self.tree.createChild('y', icon=conf.ANNOTATOR_ICON_Y, parent=self.treenode_vel )
		absv_treenode = self.tree.createChild('absolute', icon=conf.ANNOTATOR_ICON_Y, parent=self.treenode_vel )
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_vel_x_to_timeline_evt, item=vx_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_vel_y_to_timeline_evt, item=vy_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_absvel_to_timeline_evt, item=absv_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		
		self.treenode_acc = self.tree.createChild('acceleration', icon=conf.ANNOTATOR_ICON_ACCELERATION, parent=self.treenode )
		ax_treenode = self.tree.createChild('x', icon=conf.ANNOTATOR_ICON_X, parent=self.treenode_acc )
		ay_treenode = self.tree.createChild('y', icon=conf.ANNOTATOR_ICON_Y, parent=self.treenode_acc )
		absa_treenode = self.tree.createChild('absolute', icon=conf.ANNOTATOR_ICON_Y, parent=self.treenode_acc )
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_acc_x_to_timeline_evt, item=ax_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_acc_y_to_timeline_evt, item=ay_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_absacc_to_timeline_evt, item=absa_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		

		y_treenode.win = x_treenode.win = self.treenode_pos.win = \
		absv_treenode.win = vy_treenode.win = vx_treenode.win = self.treenode_vel.win = \
		absa_treenode.win = ay_treenode.win = ax_treenode.win = self.treenode_acc.win = \
		self.treenode.win = self
		

	def create_motion_tree_nodes(self):
		
		self.treenode_motion = self.tree.createChild('Motion', icon=conf.ANNOTATOR_ICON_PATH, parent=self.treenode )
		variation_treenode 	 = self.tree.createChild('x', icon=conf.ANNOTATOR_ICON_X, parent=self.treenode_motion )
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_motion_to_timeline_evt, item=variation_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		self.tree.addPopupMenuOption(label='View on the timeline', functionAction=self.__send_motion_variation_to_timeline_evt, item=variation_treenode, icon=conf.ANNOTATOR_ICON_TIMELINE)
		
		self.treenode_motion.win = variation_treenode.win = self


	######################################################################
	### GUI EVENTS #######################################################
	######################################################################

	def __remove_path_dataset(self):
		item = self.tree.selectedItem
		if item is not None: 
			self.mainwindow.remove_dataset_evt(item.win)
			self.parent_treenode.removeChild(item)

	def __send_motion_to_timeline_evt(self):
		pass

	def __send_motion_variation_to_timeline_evt(self):
		pass

	def __send_pos_x_to_timeline_evt(self):
		data = [(i,m.position[0]) for i, m in enumerate(self._path) if m is not None]
		self.mainwindow.add_chart('{0} x position'.format(self.name), data)

	def __send_pos_y_to_timeline_evt(self):
		data = [(i,m.position[1]) for i, m in enumerate(self._path) if m is not None]
		self.mainwindow.add_chart('{0} y position'.format(self.name), data)

	####################################################################

	def __send_vel_x_to_timeline_evt(self):
		data = [(i,m.velocity[0]) for i, m in enumerate(self._path) if m is not None and m.velocity is not None]
		self.mainwindow.add_chart('{0} x position'.format(self.name), data)

	def __send_vel_y_to_timeline_evt(self):
		data = [(i,m.velocity[1]) for i, m in enumerate(self._path) if m is not None and m.velocity is not None]
		self.mainwindow.add_chart('{0} y position'.format(self.name), data)

	def __send_absvel_to_timeline_evt(self):
		data = [(i,(m.velocity[1]**2+m.velocity[0]**2)**0.5) for i, m in enumerate(self._path) if m is not None and m.velocity is not None]
		self.mainwindow.add_chart('{0} absolute velocity'.format(self.name), data)


	####################################################################

	def __send_acc_x_to_timeline_evt(self):
		data = [(i,m.acceleration[0]) for i, m in enumerate(self._path) if m is not None and m.acceleration is not None]
		self.mainwindow.add_chart('{0} x position'.format(self.name), data)

	def __send_acc_y_to_timeline_evt(self):
		data = [(i,m.acceleration[1]) for i, m in enumerate(self._path) if m is not None and m.acceleration is not None]
		self.mainwindow.add_chart('{0} y position'.format(self.name), data)

	def __send_absacc_to_timeline_evt(self):
		data = [(i,(m.acceleration[1]**2+m.acceleration[0]**2)**0.5) for i, m in enumerate(self._path) if m is not None and m.acceleration is not None]
		self.mainwindow.add_chart('{0} absolute acceleration'.format(self.name), data)


	####################################################################

	def __interpolate_btn_evt(self): 
		#store a temporary path for interpolation visualization
		if len(self._sel_pts) == 2:
			mode = None if self._interpolation_mode.value=='Auto' else self._interpolation_mode.value		 #store a temporary path for interpolation visualization
			self.interpolate_range( self._sel_pts[0].frame, self._sel_pts[1].frame, interpolation_mode=mode)
			self.mainwindow._player.refresh()
		else:
			QtGui.QMessageBox.about(self, "Error", "You need to select 2 frames.")

	def __interpolation_mode_changed_evt(self): 
		#store a temporary path for interpolation visualization
		if len(self._sel_pts) == 2:

			self.calculate_tmp_interpolation()
			self.mainwindow._player.refresh()

	def __del_path_btn_evt(self): #store a temporary path for interpolation visualization
		if len(self._sel_pts) == 2:
			reply = QtGui.QMessageBox.question(self, 'Confirmation',
											   "Are you sure you want to delete this path?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
			if reply == QtGui.QMessageBox.Yes: #store a temporary path for interpolation visualization
				start, end = self._sel_pts[0].frame, self._sel_pts[1].frame
				self.delete_range(start + 1, end)
				self.mainwindow._player.refresh()
		else:
			QtGui.QMessageBox.about(self, "Error", "You need to select 2 frames.")



	
	
	######################################################################
	### VIDEO EVENTS #####################################################
	######################################################################

	def on_click(self, event, x, y):

		if event.button() == 1:
			frame_index = self.mainwindow._player.video_index


			if self._mark_pto_btn.checked:
				self.set_position(frame_index if frame_index>=0 else 0, x, y)
				self._mark_pto_btn.checked = False
			else:
				selected = self.select_moment(frame_index, x, y)
				if selected != None:
					modifier = int(event.modifiers())
					# If the control button is pressed will add the blob to the previous selections
					if modifier == QtCore.Qt.ControlModifier:
						if selected not in self._sel_pts: #store a temporary path for interpolation visualization
							self._sel_pts.append(selected)
						else:
							# Remove the blob in case it was selected before #store a temporary path for interpolation visualization
							self._sel_pts.remove(selected)
					else:
						# The control key was not pressed so will select only one #store a temporary path for interpolation visualization
						self._sel_pts =[selected]
				else: #store a temporary path for interpolation visualization
					self._sel_pts =[]  # No object selected: remove previous selections #store a temporary path for interpolation visualization
				self._sel_pts =sorted(self._sel_pts, key=lambda x: x.frame)

 			#store a temporary path for interpolation visualization
			if len(self._sel_pts) == 2: 
				#########################################################
				#In case 2 frames are selected, draw the temporary path##
				#########################################################
				self.calculate_tmp_interpolation()
				self._interpolate_btn.show()
				self._interpolation_mode.show()
				self._interpolation_title.show()
				self._del_path_btn.show()
				#########################################################
			else:
				self._interpolate_btn.hide()
				self._interpolation_mode.hide()
				self._interpolation_title.hide()
				self._del_path_btn.hide()
				
			
			self.mainwindow._player.refresh()





	######################################################################
	### PROPERTIES #######################################################
	######################################################################

	@property
	def mainwindow(self): return self._object2d.mainwindow

	@property 
	def tree(self):  return self._object2d.tree

	@property 
	def parent_treenode(self):  return self._object2d.treenode