import pyforms
from confapp import conf
from pyforms.basewidget import BaseWidget
from pyforms_gui.controls.control_button import ControlButton
from pyforms_gui.controls.control_dir import ControlDir
from pyforms_gui.controls.control_file import ControlFile

from os import listdir
from os.path import isfile, join, splitext, abspath, dirname

import re, yaml

class DeepLabWindow(BaseWidget):

    def __init__(self, parent=None):
        super(DeepLabWindow, self).__init__('DeepLab', parent_win=parent)
        self.mainwindow = parent


        self._file         = ControlFile('YAML  to import from:')
        self._importButton  = ControlButton('Import')

        self._formset = [
            ('_file', '_importButton'),
            ' '
        ]

        self._importButton.value = self.__importFromYAMLFile


        self.set_margin(5)
        #self.layout().setMargin(5)
        self.setMinimumHeight(400)
        self.setMinimumWidth(800)

    ###########################################################################
    ### EVENTS ################################################################
    ###########################################################################

    def __importFromYAMLFile(self):


        with open(self._file.value, 'r') as f:
            try:
                dict_yaml = yaml.load(f)
            except yaml.YAMLError as exc:
                print(exc)
                return

        videos = dict_yaml.get("video_sets").keys()
        bodyparts = dict_yaml.get("bodyparts")

        for video in videos:

            v = self.mainwindow.project.create_video()
            v.filepath = abspath(video)

            for part in bodyparts:
                obj = v.create_object()
                obj.name = part
                obj.create_path()

            track = self.mainwindow.timeline.add_track(title=v.name)

            frames_directory = join(abspath(dirname(self._file.value)), "labeled-data", v.name+ "_labeled")

            frames = self.get_frames_from_directory_with_images(frames_directory)
            for frame in frames:
                self.mainwindow.timeline.add_event(begin=frame, end=frame+1, track=track)



    ###########################################################################
    ### HELPER FUNCTIONS ######################################################
    ###########################################################################

    def get_frames_from_directory_with_images(self, directory):

        files = [f for f in listdir(directory) if isfile(join(directory, f))]

        frames = []

        for filename in files:

            filename = splitext(filename)[0]

            frame = self.get_trailing_number(filename)

            if frame!=None and frame<3000:
                frames.append(frame)

        frames.sort()

        return frames


    def get_trailing_number(self, s):
        m = re.search(r'\d+$', s)

        return int(m.group()) if m else None

    ###########################################################################
    ### PROPERTIES ############################################################
    ###########################################################################


    def __apply_event(self):
        pass

if __name__ == '__main__': 
    pyforms.startApp(DeepLabWindow)
