import pyforms
from confapp import conf
from pyforms.basewidget import BaseWidget

from pyforms_gui.controls.control_button import ControlButton
from pyforms_gui.controls.control_text import ControlText
from pyforms_gui.controls.control_dir import ControlDir
from pyforms_gui.controls.control_file import ControlFile

from os import listdir
from os.path import isfile, join, splitext, abspath, dirname

#from deeplabcut import extract_frames

import re, yaml

class DeepLabWindow(BaseWidget):

    def __init__(self, parent=None):
        super(DeepLabWindow, self).__init__('DeepLab', parent_win=parent)
        self.mainwindow = parent


        self._file         = ControlFile('YAML  to import from:')
        self._importButton  = ControlButton('Import')

        self._outdir        = ControlDir('Output directory')
        self._outfile       = ControlText('Output file name')
        self._exportButton  = ControlButton('Export')

        self._formset = [
            ('_file', '_importButton'),
            '_outdir',
            '_outfile',
            '_exportButton'
        ]

        self._importButton.value = self.__importFromYAMLFile
        self._exportButton.value = self.__exportToCSVFile


        self.set_margin(5)
        #self.layout().setMargin(5)
        self.setMinimumHeight(400)
        self.setMinimumWidth(800)

    ###########################################################################
    ### EVENTS ################################################################
    ###########################################################################

    def __importFromYAMLFile(self):

        config_path = self._file.value

        with open(config_path, 'r') as f:
            try:
                dict_yaml = yaml.load(f)
            except yaml.YAMLError as exc:
                print(exc)
                return

        self.scorer = dict_yaml.get("scorer")
        self.videos = dict_yaml.get("video_sets").keys()
        self.bodyparts = dict_yaml.get("bodyparts")
        self.crop = dict_yaml.get("crop")

        for video in self.videos:

            v = self.mainwindow.project.create_video()
            v.filepath = abspath(video)

            for part in self.bodyparts:
                obj = v.create_object()
                obj.name = part
                obj.create_path()

            track = self.mainwindow.timeline.add_track(title=v.name)


            """
            extract_frames(config_path, userfeedback=False)
    
            frames_directory = join(abspath(dirname(config_path)), "labeled-data", v.name)
    
            frames = self.get_frames_from_directory_with_images(frames_directory)
            for frame in frames:
                self.mainwindow.timeline.add_event(begin=frame, end=frame+1, track=track)
            """


    def __exportToCSVFile(self):

        for video in self.videos:
            #export paths
            pass

    ###########################################################################
    ### HELPER FUNCTIONS ######################################################
    ###########################################################################

    def get_frames_from_directory_with_images(self, directory):
        """
        Given a directory, assumes all files are images and extracts the frame number of each image from the image
        name. Example: filename=image0015.jpg  -> frame=0015

        :param directory: A directory with image files
        :return: A list with all the frames
        """

        files = [f for f in listdir(directory) if isfile(join(directory, f))]

        frames = []

        for filename in files:

            filename = splitext(filename)[0]

            frame = self.get_trailing_number(filename)

            if frame!=None:
                frames.append(frame)

        frames.sort()

        return frames


    def get_trailing_number(self, s):
        """
        :param s: A string with the format: imagexxxx.yyy
        :return: The frame of the image, in the above example returns xxxx
        """
        m = re.search(r'\d+$', s)

        return int(m.group()) if m else None

    ###########################################################################
    ### PROPERTIES ############################################################
    ###########################################################################
 
    @property
    def scorer(self): return self._scorer

    @scorer.setter
    def scorer(self, value): 
        self._scorer = value

    @property
    def videos(self): return self._videos

    @videos.setter
    def videos(self, value): 
        self._videos = value

    @property
    def bodyparts(self): return self._bodyparts

    @bodyparts.setter
    def bodyparts(self, value): 
        self._bodyparts = value

    def __apply_event(self):
        pass

if __name__ == '__main__': 
    pyforms.startApp(DeepLabWindow)
