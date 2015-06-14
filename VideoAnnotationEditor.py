#! /usr/bin/python
from __init__ import *
import os, cv2
from PyQt4 import QtCore, QtGui
from modules.PathEditor.TrackingDataFile import TrackingDataFile
from modules.PathEditor.VideoAnnotationPathEditor import VideoAnnotationPathEditor
from modules.Timeline.VideoAnnotationTimeline import VideoAnnotationTimeline

class VideoAnnotationEditor(VideoAnnotationPathEditor, VideoAnnotationTimeline, BaseWidget):
    """Application form"""

    def __init__(self):
        super(VideoAnnotationEditor,self).__init__('Video annotation editor')

        self._video     = ControlFile('Video')
        self._player    = ControlPlayer("Player")
        self._time      = ControlEventTimeline('Time')
        
        self._formset = ['_video', '_player', '=', '_time']

        self._video.changed         = self.__video_changed
        self._player.processFrame   = self.process_frame
        self._player.onClick        = self.onPlayerClick
        
        self.mainmenu = [
                { 'File': [
                        {'Exit': exit}
                    ]
                }
            ]

        self.initForm()

        # Experiment related information

        #self._video.value = '/home/ricardo/subversion/MEShTracker/Dolphin/DOLPHINS/New Videos/2013.04.21_12.51/2013 04 21 12 51_Entrada (1).MP4'
        #with open('/home/ricardo/Downloads/velocities.csv', 'rb') as csvfile:
        #    import csv
        #    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        #    self._time._time.importchart_csv(spamreader)
        #self._data = TrackingDataFile('/home/ricardo/Downloads/2013 04 21 12 51 (2)_version_08.06.2015.csv')


   
    ######################################################################################
    #### EVENTS ##########################################################################
    ######################################################################################

    def __video_changed(self):
        self._player.value = self._video.value
        self._time.max = self._player.max

        # Update fps info on timeline
        self._time._time._video_fps = self._player.fps
        self._time._time._video_fps_min = self._player._form.videoFPS.minimum()
        self._time._time._video_fps_max = self._player._form.videoFPS.maximum()
        self._time._time._video_fps_inc = self._player._form.videoFPS.singleStep()



    def onPlayerClick(self, event, x, y):
        """
        Code to select a blob with the mouse
        """
        super(VideoAnnotationEditor, self).onPlayerClick(event, x, y)
        self._player.refresh()


    
    def process_frame(self, frame):
        """
        Function called before render each frame
        """
        return super(VideoAnnotationEditor, self).process_frame(frame)









if __name__ == "__main__":  app.startApp(VideoAnnotationEditor)
