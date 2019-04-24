#! /usr/bin/python2
# -*- coding: utf-8 -*-
import pypi_xmlrpc
import pip, sys, subprocess

from .__init__ import __version__
from pyforms.basewidget import BaseWidget

from pyforms.controls import ControlPlayer
from pyforms.controls import ControlEventTimeline
from pyforms.controls import ControlDockWidget

from pythonvideoannotator_models_gui.models import Project
from pythonvideoannotator_models_gui.dialogs.dialog import Dialog
from pythonvideoannotator_models.models.video.objects.object2d.datasets.path import Path
from pythonvideoannotator_models.models.video import Video
from pythonvideoannotator_models.models.video.objects.object2d import  Object2D

from .userstats import track_user_stats

from confapp import conf
if conf.PYFORMS_MODE=='GUI':
    from AnyQt import QtCore
    from AnyQt.QtWidgets import QApplication, QFileDialog, QMessageBox
    


def Exit(): exit()

class BaseModule(BaseWidget):
    """Application form"""

    def __init__(self):
        global conf;
        conf += 'pythonvideoannotator.resources'  # Resources can only be loaded after pyqt is running

        super(BaseModule, self).__init__('Video annotation editor')

        self._project  = Project(parent=self)
        Dialog.project = self._project

        self._player    = ControlPlayer("Player")
        self._time      = ControlEventTimeline('Time')
        self._dock      = ControlDockWidget("Timeline", side='bottom', order=1, margin=5)

        self.formset    = ['_player']

        self._dock.value                    = self._time
        self._player.process_frame_event    = self.process_frame_event
        self._player.click_event            = self.on_player_click_event
        self._time.key_release_event        = lambda x: x
        self._player.key_release_event      = lambda x: x

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

        track_user_stats()

        ########################################################################
        ###### CHECK NEW VERSIONS RELEASES #####################################
        ########################################################################
        try:
            versions = pypi_xmlrpc.package_releases('Python-video-annotator')

            if versions is not None:
                new_version = versions[0]
                new_version_numbers = [int(x) for x in new_version.split('.')]
                version_numbers = [int(x) for x in __version__.split('.')]
                for new_n, n in zip(new_version_numbers, version_numbers):
                    if new_n > n:
                        response = self.question(
                            "<h2>New version <b>[{0}]</b> available</h2>"
                            "<p>Do you wish to update the software?</p>"
                            "<p>The software can be updated later by running the next command in the terminal:</p>"
                            "<i>pip install python-video-annotator --force-reinstall</i>".format(new_version),
                            'New version [{0}]'.format(new_version)
                        )

                        if response == 'yes':
                            subprocess.call([sys.executable, "-m", "pip", "install", 'python-video-annotator', '--force-reinstall'])

                            self.message('The software was updated and this session will be closed. Please execute the software again.', 'Restart required')
                            exit()
                        break
            else:
                print('Enabled to check new versions')

        except Exception as e:
            print('Enabled to check new versions:')

    ######################################################################################
    #### FUNCTIONS #######################################################################
    ######################################################################################
        
    def init_form(self):
        super(BaseModule, self).init_form()

        if conf.CHART_FILE_PATH: self._time.import_chart(*conf.CHART_FILE_PATH)
        if conf.PROJECT_PATH:    self.load_project(conf.PROJECT_PATH)


    ######################################################################################
    #### IO FUNCTIONS ####################################################################
    ######################################################################################

    def save(self, data, project_path=None):
        self._project.save(data, project_path)
        return data


    def load(self, data, project_path=None):
        try:
            self._project.load(data, project_path)
        except FileNotFoundError as e:
            QMessageBox.critical(self, "Error", str(e))

    def save_project(self, project_path=None):
        try:
            if project_path is None:
                project_path = QFileDialog.getExistingDirectory(self, "Select the project directory")

            if project_path is not None and str(project_path)!='':
                project_path = str(project_path)
                self.save({}, project_path)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

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


    def add_dataset_event(self, dataset):
        pass

    def removed_dataset_event(self, dataset):
        pass

    def removed_object_event(self, obj):
        pass


    def __open_project_event(self): self.load_project()

    def __save_project_event(self):
        print('Project saved')
        self.save_project(self._project.directory)

    def __save_project_as_event(self): self.save_project()

    def keyReleaseEvent(self, event):
        ######################################################################################
        #### SPECIFIC SHORTCUTS###############################################################
        ######################################################################################
        
        #Go to the next event and then click the mark the point button
        if event.key() == QtCore.Qt.Key_I:
            if self.timeline.timeline_widget.selected is not None and self.timeline.timeline_widget.selected != self.timeline.timeline_widget.pointer:
                self.move_to_next_event()
                self.mark_point()

        ######################################################################################
        #### DOCK SHORTCUTS ##################################################################
        ######################################################################################

        #Select the path of the next object
        if event.key() == QtCore.Qt.Key_U:
            self.select_next_path()

        #"Click" the Mark Point button in the current Path
        elif event.key() == QtCore.Qt.Key_O:
            self.mark_point()

        ######################################################################################
        #### TIMELINE SHORTCUTS ##############################################################
        ######################################################################################

        if self.timeline.timeline_widget.selected is not None:

            modifier = int(event.modifiers())

            if modifier == QtCore.Qt.ControlModifier and event.key() == QtCore.Qt.Key_Left:
                self.move_event_or_pointer_left(event)

            if modifier == QtCore.Qt.ControlModifier and event.key() == QtCore.Qt.Key_Right:
                self.move_event_or_pointer_right(event)

            if self.timeline.timeline_widget.selected != self.timeline.timeline_widget.pointer:

                # Delete the selected event
                if event.key() == QtCore.Qt.Key_Delete:
                    self.timeline.timeline_widget.remove_selected_event()

                # Lock or unlock an event
                if event.key() == QtCore.Qt.Key_L:
                    self.timeline.timeline_widget.toggle_selected_event_lock()

                if event.key() == QtCore.Qt.Key_E:
                    self.move_to_next_event()

                if event.key() == QtCore.Qt.Key_Q:
                    self.move_to_previous_event()

                if modifier == QtCore.Qt.ControlModifier and event.key() == QtCore.Qt.Key_Up:
                    self.move_event_up()

                if modifier == QtCore.Qt.ControlModifier and event.key() == QtCore.Qt.Key_Down:
                    self.move_event_down()

                if modifier == int(
                        QtCore.Qt.ShiftModifier | QtCore.Qt.ControlModifier) and event.key() == QtCore.Qt.Key_Left:
                    self.move_event_end_left()

                if modifier == int(
                        QtCore.Qt.ShiftModifier | QtCore.Qt.ControlModifier) and event.key() == QtCore.Qt.Key_Right:
                    self.move_event_end_right()

                if modifier == QtCore.Qt.ShiftModifier and event.key() == QtCore.Qt.Key_Left:
                    self.move_event_begin_left()

                if modifier == QtCore.Qt.ShiftModifier and event.key() == QtCore.Qt.Key_Right:
                    self.move_event_begin_right()

        else:
            if event.key() == QtCore.Qt.Key_S:

                self.create_event_at_current_frame()

            # walk backwards 1 step
            elif event.key() == QtCore.Qt.Key_A:
                self.timeline.timeline_widget.position = self.timeline.timeline_widget.position - 1

            # forward 1 step
            elif event.key() == QtCore.Qt.Key_D:
                self.timeline.timeline_widget.position = self.timeline.timeline_widget.position + 1

            elif event.key() == QtCore.Qt.Key_E:
                self.move_to_first_event()

            elif event.key() == QtCore.Qt.Key_Q:
                self.move_to_last_event()

        ######################################################################################
        #### PLAYER SHORTCUTS ################################################################
        ######################################################################################

        # Control video playback using the space bar to Play/Pause
        if event.key() == QtCore.Qt.Key_Space:

            if self.player.video_widget.control.is_playing:
                self.player.video_widget.control.stop()
            else:
                self.player.video_widget.control.play()

        # Jumps 1 frame backwards
        elif event.key() == QtCore.Qt.Key_A:
            self.player.video_widget.control.video_index -= 2
            self.player.video_widget.control.call_next_frame()

        # Jumps 1 frame forward
        elif event.key() == QtCore.Qt.Key_D:
            self.player.video_widget.control.call_next_frame()

        # Jumps 20 seconds backwards
        elif event.key() == QtCore.Qt.Key_Z:
            self.player.video_widget.control.jump_backward()
            self.player.video_widget.control.call_next_frame()

        # Jumps 20 seconds forward
        elif event.key() == QtCore.Qt.Key_C:
            self.player.video_widget.control.jump_forward()
            self.player.video_widget.control.call_next_frame()

        elif event.key() == QtCore.Qt.Key_M:
            self._move_img = False

        elif event.key() == QtCore.Qt.Key_1:
            self.player.video_widget.control.next_frame_step = 1
            self.player.video_widget.show_tmp_msg('Speed: 1x')

        elif event.key() == QtCore.Qt.Key_2:
            self.player.video_widget.control.next_frame_step = 2
            self.player.video_widget.show_tmp_msg('Speed: 2x')

        elif event.key() == QtCore.Qt.Key_3:
            self.player.video_widget.control.next_frame_step = 3
            self.player.video_widget.show_tmp_msg('Speed: 3x')

        elif event.key() == QtCore.Qt.Key_4:
            self.player.video_widget.control.next_frame_step = 4
            self.player.video_widget.show_tmp_msg('Speed: 4x')

        elif event.key() == QtCore.Qt.Key_5:
            self.player.video_widget.control.next_frame_step = 5
            self.player.video_widget.show_tmp_msg('Speed: 5x')

        elif event.key() == QtCore.Qt.Key_6:
            self.player.video_widget.control.next_frame_step = 6
            self.player.video_widget.show_tmp_msg('Speed: 6x')

        elif event.key() == QtCore.Qt.Key_7:
            self.player.video_widget.control.next_frame_step = 7
            self.player.video_widget.show_tmp_msg('Speed: 7x')

        elif event.key() == QtCore.Qt.Key_8:
            self.player.video_widget.control.next_frame_step = 8
            self.player.video_widget.show_tmp_msg('Speed: 8x')

        elif event.key() == QtCore.Qt.Key_9:
            self.player.video_widget.control.next_frame_step = 9
            self.player.video_widget.show_tmp_msg('Speed: 9x')

    ######################################################################################
    #### EVENT FUNCTIONS #################################################################
    ######################################################################################

    def select_next_path(self):

        selected = self.project.tree.selected_item

        if selected is not None:

            #If it's a video, try to select its first object and the object's first child 
            if isinstance(selected.win, Video):

                if selected.childCount() > 0:
                    child_object = selected.child(0)

                    if child_object.childCount() > 0:
                        self.project.tree.selected_item = child_object.child(0)

            #If it's an object, try to select it's first child
            elif isinstance(selected.win, Object2D):
                if selected.childCount() > 0:
                    self.project.tree.selected_item = selected.child(0)

            #If it's a path try to select the first child of the next object of their parent video
            elif isinstance(selected.win, Path):

                parent_object = selected.parent()
                parent_video = parent_object.parent()

                parent_object_index = parent_video.indexOfChild(parent_object)

                if parent_object_index < parent_video.childCount() -1 :
                    next_object = parent_video.child(parent_video.indexOfChild(parent_object)+1)

                    if next_object.childCount() > 0:
                        self.project.tree.selected_item = next_object.child(0)

                #If it's the last object of the video, go back to the path of the first one
                else:
                    next_object = parent_video.child(0)

                    if next_object.childCount() > 0:
                        self.project.tree.selected_item = next_object.child(0)


    def mark_point(self):
        selected = self.project.tree.selected_item

        if selected is not None and isinstance(selected.win, Path):
            path = selected.win

            path.mark_point_button.click()


    def move_to_next_event(self):
        index = self.timeline.timeline_widget.selected_row.events.index(self.timeline.timeline_widget.selected)
        if index < len(self.timeline.timeline_widget.selected_row.events)-1:
            self.timeline.timeline_widget.selected = self.timeline.timeline_widget.selected_row.events[index+1]
            self.timeline.timeline_widget.position = self.timeline.timeline_widget.selected.begin

    def move_to_previous_event(self):
        index = self.timeline.timeline_widget.selected_row.events.index(self.timeline.timeline_widget.selected)
        if index > 0:
            self.timeline.timeline_widget.selected = self.timeline.timeline_widget.selected_row.events[index - 1]
            self.timeline.timeline_widget.position = self.timeline.timeline_widget.selected.begin

    def move_to_first_event(self):
        if self.timeline.timeline_widget.selected_row is not None and len(self.timeline.timeline_widget.selected_row)>0:
            self.timeline.timeline_widget.selected = self.timeline.timeline_widget.selected_row.events[0]
            self.timeline.timeline_widget.position = self.timeline.timeline_widget.selected.begin

    def move_to_last_event(self):
        if self.timeline.timeline_widget.selected_row is not None and len(self.timeline.timeline_widget.selected_row)>0:
            self.timeline.timeline_widget.selected = self.timeline.timeline_widget.selected_row.events[len(self.timeline.timeline_widget.selected_row)-1]
            self.timeline.timeline_widget.position = self.timeline.timeline_widget.selected.begin

    def move_event_or_pointer_left(self, event):
        modifier = int(event.modifiers())

        self.timeline.timeline_widget.selected.move(-1, 0)
        event.ignore()
        self.timeline.timeline_widget.repaint()

    def move_event_or_pointer_right(self, event):
        modifier = int(event.modifiers())

        self.timeline.timeline_widget.selected.move(1, 0)
        event.ignore()
        self.timeline.timeline_widget.repaint()

    def move_event_up(self):
        self.timeline.timeline_widget.selected.move(0, self.timeline.timeline_widget.selected.top_coordinate - self.timeline.timeline_widget.TRACK_HEIGHT)
        self.timeline.timeline_widget.repaint()

    def move_event_down(self):
        self.timeline.timeline_widget.selected.move(0, self.timeline.timeline_widget.selected.top_coordinate + self.timeline.timeline_widget.TRACK_HEIGHT)
        self.timeline.timeline_widget.repaint()

    def move_event_end_left(self):
        self.timeline.timeline_widget.selected.move_end(-1)
        self.timeline.timeline_widget.repaint()

    def move_event_end_right(self):
        self.timeline.timeline_widget.selected.move_end(1)
        self.timeline.timeline_widget.repaint()

    def move_event_begin_left(self):
        self.timeline.timeline_widget.selected.move_begin(-1)
        self.timeline.timeline_widget.repaint()

    def move_event_begin_right(self):
        self.timeline.timeline_widget.selected.move_begin(1)
        self.timeline.timeline_widget.repaint()

    def create_event_at_current_frame(self):
        if not self.timeline.timeline_widget.creating_event:
            # Start
            self.timeline.timeline_widget.creating_event_start = self.timeline.timeline_widget.pointer.frame
            self.timeline.timeline_widget.creating_event = True

            # TODO Add some indicator that an event is being recorded, like
            # using the track selector circle to become red

        else:
            # End, must be followed right after Start key and have no
            # effect otherwise
            self.timeline.timeline_widget.creating_event_end = self.timeline.timeline_widget.pointer.frame

            start = self.timeline.timeline_widget.creating_event_start
            end = self.timeline.timeline_widget.creating_event_end
            comment = ""

            if end > start:
                track = self.timeline.timeline_widget.selected_row
                if track is None and len(self.timeline.timeline_widget.tracks)>0:
                    track = self.timeline.timeline_widget.tracks[0]
                if track is None:
                    track = self.timeline.timeline_widget.add_track()

                self.timeline.timeline_widget.add_event(start, end, comment, track=track )
                self.timeline.timeline_widget.repaint()
                self.timeline.timeline_widget.creating_event = False
            else:
                self.timeline.timeline_widget.creating_event = False




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
        self._player.value      = value
        self._player.enabled    = value is not None
        if value:
            self._time.max = self._player.max

    @property
    def project(self): return self._project
