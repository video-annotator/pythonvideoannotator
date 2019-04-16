import pyforms
from confapp import conf
from pyforms.basewidget import BaseWidget

from pyforms.controls import ControlButton
from pyforms.controls import ControlText
from pyforms.controls import ControlDir
from pyforms.controls import ControlFile

from pythonvideoannotator_models.models.video.objects.object2d.datasets.path import Path
from pythonvideoannotator_models.models.video import Video

from os import listdir
from os.path import isfile, join, splitext, abspath, dirname, basename
import csv
import deeplabcut

import re, yaml

if conf.PYFORMS_MODE=='GUI':
    from AnyQt.QtWidgets import QMessageBox

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

        self._scorer = ""
        self._videos = []
        self._bodyparts = []
        self._crop = []

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
        self.videos = dict_yaml.get("video_sets")
        self.bodyparts = dict_yaml.get("bodyparts")
        self.crop = dict_yaml.get("crop")

        if len(self.videos) != len(set(self.videos)):
            print("Two videos can't have the same name!")
            return

        if len(self.bodyparts) != len(set(self.bodyparts)):
            print("Two bodyparts can't have the same name!")
            return

        for video in self.videos.keys():

            v = self.mainwindow.project.create_video()
            v.filepath = abspath(video)

            for part in self.bodyparts:
                obj = v.create_object()
                obj.name = part
                obj.create_path()
            
            #adds the pair video and track to the videos dictionary
            track = self.mainwindow.timeline.add_track(title=v.name)

            deeplabcut.extract_frames(config_path, userfeedback=False)
    
            frames_directory = join(abspath(dirname(config_path)), "labeled-data", v.name)
    
            frames = self.get_frames_from_directory_with_images(frames_directory)
            for frame in frames:
                self.mainwindow.timeline.add_event(begin=frame, end=frame+1, track=track)


        QMessageBox.information(self, "Import finished", "Completed import from YAML file")


    def __exportToCSVFile(self):

        video_names = []
        for video_path in self.videos.keys():
            video_names.append(splitext(basename(video_path))[0])
    
        for video in self.mainwindow.project.videos:

            if video.name not in video_names:
                continue

            csv_file_name = "res" + video.name + ".csv"
            with open(csv_file_name, mode='w') as csv_file:

                writer = csv.writer(csv_file, delimiter=',')

                # write row with the name of the scorer(person labeling the frames)
                currentRow = []
                currentRow.append("scorer")
                for _ in range(len(self.bodyparts)*2):
                    currentRow.append(self.scorer)
                writer.writerow(currentRow)


                # write row with the name of the bodyparts
                currentRow = []
                currentRow.append("bodyparts")
                for bodypart in self.bodyparts:
                    currentRow.append(bodypart)
                    currentRow.append(bodypart)
                writer.writerow(currentRow)


                # write row with just x and y
                currentRow = []
                currentRow.append("coords")
                for _ in range((len(self.bodyparts))):
                    currentRow.append("x")
                    currentRow.append("y")
                writer.writerow(currentRow)


                #order the video objects to match the order of the bodyparts
                ordered_objects = []
                for bodypart in self.bodyparts:
                    for obj in video.objects:
                        if obj.name==bodypart:
                            ordered_objects.append(obj)
                            break

                print(len(ordered_objects))

                #write the coords of each bodypart for every labeled frame
                track = self.mainwindow.timeline.get_track(video.name)
                if track==None:
                    print("No track was found with the name: "+ video.name)
                    print("Stopped exporting to CSV file")
                    return

                for event in track.events:
                    currentRow = []

                    frame=event.begin
                    currentRow.append("labeled-data/"+video.name+"/img"+str(frame)+".png")

                    for obj in ordered_objects:
                        for path in obj.paths:

                            data = path.data

                            if data[frame] is not None:
                                currentRow.append(data[frame][0])
                                currentRow.append(data[frame][1])

                            break #there should only be one path for each object
                        
                        else:
                            print("Object has no path")

                    writer.writerow(currentRow)

        QMessageBox.information(self, "Export finished", "Completed export to CSV file")

    
    def save_form(self, data, folder):

        return {"scorer" : self.scorer, "videos" : self.videos, "bodyparts" : self.bodyparts, "crop" : self.crop}

    def load_form(self, data, folder):

        self.scorer = data["scorer"]
        self.videos = data["videos"]
        self.bodyparts = data["bodyparts"]
        self.crop = data["crop"]


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
