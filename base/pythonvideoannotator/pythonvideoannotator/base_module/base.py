#! /usr/bin/python2
# -*- coding: utf-8 -*-

import pypi_xmlrpc
import sys, subprocess
from confapp import conf
from AnyQt.QtCore import QTimer

from ..__init__ import __version__
from pyforms.basewidget import BaseWidget

from pyforms.controls import ControlPlayer
from pyforms.controls import ControlEventTimeline
from pyforms.controls import ControlDockWidget
from pyforms.controls import ControlProgress
from pyforms.controls import ControlButton

from pythonvideoannotator_models_gui.models import Project
from pythonvideoannotator_models_gui.dialogs.dialog import Dialog
from pythonvideoannotator_models.models.video.objects.object2d.datasets.path import Path
from pythonvideoannotator_models.models.video import Video
from pythonvideoannotator_models.models.video.objects.object2d import Object2D

from ..userstats import track_user_stats


if conf.PYFORMS_MODE == 'GUI':
    from AnyQt.QtWidgets import QApplication


def Exit(): exit()


class Base(BaseWidget):
    """Application form"""

    def __init__(self):
        global conf;
        conf += 'pythonvideoannotator.resources'  # Resources can only be loaded after pyqt is running

        super().__init__('Video annotation editor')

        self._project = Project(parent=self)
        Dialog.project = self._project

        self._player = ControlPlayer("Player")
        self._time = ControlEventTimeline('Time')
        self._dock = ControlDockWidget("Timeline", side='bottom', order=1, margin=5)
        self._progress = ControlProgress('Progress', visible=False)

        # define the application toolbar
        self.toolbar = [
            ControlButton('Open', icon=conf.ANNOTATOR_ICON_OPEN, default=self.__open_project_event),
            ControlButton('Save', icon=conf.ANNOTATOR_ICON_SAVE, default=self.__save_project_event)
        ]

        self.formset = ['_player', '_progress']

        self._dock.value = self._time
        self._player.process_frame_event = self.process_frame_event
        self._player.click_event = self.on_player_click_event
        self._player.double_click_event = self.on_player_double_click_event
        self._player.drag_event = self.on_player_drag_event
        self._player.end_drag_event = self.on_player_end_drag_event
        self._time.key_release_event = lambda x: x
        self._player.key_release_event = lambda x: x

        self.load_order = []

        self.mainmenu.insert(0,
                             {'File': [
                                 {'Open': self.__open_project_event, 'icon': conf.ANNOTATOR_ICON_OPEN},
                                 '-',
                                 {'Save': self.__save_project_event, 'icon': conf.ANNOTATOR_ICON_SAVE},
                                 {'Save as': self.__save_project_as_event, 'icon': conf.ANNOTATOR_ICON_SAVE},
                                 '-',
                                 {'Exit': QApplication.closeAllWindows, 'icon': conf.ANNOTATOR_ICON_EXIT}
                             ]}
                             )
        self.mainmenu.insert(1, {'Modules': []})
        self.mainmenu.insert(2, {'Windows': []})

        track_user_stats()

        ########################################################################
        ###### CHECK NEW VERSIONS RELEASES #####################################
        ########################################################################
        try:
            versions = pypi_xmlrpc.package_releases('Python-video-annotator')

            if versions is not None:
                new_version = versions[0]
                if float(new_version) > float(__version__):
                    response = self.question(
                        "<h2>New version <b>[{0}]</b> available</h2>"
                        "<p>Do you wish to update the software?</p>"
                        "<p>The software can be updated later by running the next command in the terminal:</p>"
                        "<i>pip install python-video-annotator --force-reinstall</i>".format(new_version),
                        'New version [{0}]'.format(new_version)
                    )

                    if response == 'yes':
                        subprocess.call(
                            [sys.executable, "-m", "pip", "install", 'python-video-annotator', '--force-reinstall'])

                        self.message(
                            'The software was updated and this session will be closed. Please execute the software again.',
                            'Restart required')
                        exit()

            else:
                print('Unable to check new versions')

        except Exception as e:
            print('Unable to check new versions:')

    ######################################################################################
    #### FUNCTIONS #######################################################################
    ######################################################################################

    def init_form(self):
        super().init_form()

        if conf.CHART_FILE_PATH:
            self._time.import_chart(*conf.CHART_FILE_PATH)
        if conf.VIDEOANNOTATOR_PROJECTPATH:
            self.load_project(conf.VIDEOANNOTATOR_PROJECTPATH)

        if len(sys.argv) > 1:
            QTimer.singleShot(1000, self.__load_project_from_argv)


    ######################################################################################
    #### EVENTS ##########################################################################
    ######################################################################################

    def on_player_drag_event(self, p1, p2):
        if self._project:
            self._project.player_on_drag(p1, p2)
        self._player.refresh()

    def on_player_end_drag_event(self, p1, p2):
        if self._project:
            self._project.player_on_end_drag(p1, p2)
        self._player.refresh()

    def on_player_click_event(self, event, x, y):
        """
        Code to select a blob with the mouse
        """
        if self._project:
            self._project.player_on_click(event, x, y)
        self._player.refresh()

    def on_player_double_click_event(self, event, x, y):
        """
        Code to select a blob with the mouse
        """
        if self._project:
            self._project.player_on_double_click(event, x, y)
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

    def __open_project_event(self):
        self.load_project()

    def __save_project_event(self):
        self.save_project(self._project.directory)

    def __save_project_as_event(self):
        self.save_project()



    def __load_project_from_argv(self):
        self.load_project(sys.argv[-1])

    ######################################################################################
    #### EVENT FUNCTIONS #################################################################
    ######################################################################################

    def select_next_path(self):

        selected = self.project.tree.selected_item

        if selected is not None:

            # If it's a video, try to select its first object and the object's first child
            if isinstance(selected.win, Video):

                if selected.childCount() > 0:
                    child_object = selected.child(0)

                    if child_object.childCount() > 0:
                        self.project.tree.selected_item = child_object.child(0)

            # If it's an object, try to select it's first child
            elif isinstance(selected.win, Object2D):
                if selected.childCount() > 0:
                    self.project.tree.selected_item = selected.child(0)

            # If it's a path try to select the first child of the next object of their parent video
            elif isinstance(selected.win, Path):

                parent_object = selected.parent()
                parent_video = parent_object.parent()

                parent_object_index = parent_video.indexOfChild(parent_object)

                if parent_object_index < parent_video.childCount() - 1:
                    next_object = parent_video.child(parent_video.indexOfChild(parent_object) + 1)

                    if next_object.childCount() > 0:
                        self.project.tree.selected_item = next_object.child(0)

                # If it's the last object of the video, go back to the path of the first one
                else:
                    next_object = parent_video.child(0)

                    if next_object.childCount() > 0:
                        self.project.tree.selected_item = next_object.child(0)



    ######################################################################################
    ######################################################################################
    #### PROPERTIES ######################################################################
    ######################################################################################

    @property
    def progress_bar(self):
        return self._progress

    @property
    def timeline(self):
        return self._time

    @property
    def player(self):
        return self._player

    @property
    def video(self):
        return self._player.value

    @video.setter
    def video(self, value):
        self._player.value = value
        self._player.enabled = value is not None
        if value:
            self._time.max = self._player.max

    @property
    def project(self):
        return self._project
