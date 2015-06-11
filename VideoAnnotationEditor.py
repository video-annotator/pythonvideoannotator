#! /usr/bin/python
from __init__ import *
import os
from PyQt4 import QtCore, QtGui

class VideoAnnotationEditor(BaseWidget):
    """Application form"""

    def __init__(self):
        super(VideoAnnotationEditor,self).__init__('Video annotation editor')

        self._video     = ControlFile('Video')
        self._player    = ControlPlayer("Player")
        self._time      = ControlEventTimeline('Time')
        
        self._formset = ['_video', '_player', '=', '_time']

        self._update_time   = True      #Use to avoid double video jump 2 frame trigger
        self._selectedItems = []        #Stores the selected tracked objects
        
        self._video.changed         = self.__video_changed
        self._time.pointerChanged   = self.__time_changed
        self._time.isPlaying        = self.__timeline_play_video
        self._time.fpsChanged       = self.__timeline_fps_changed
        self._time.getExportFilename= self.__createFilename2Export
        self._player.processFrame   = self.__process_frame

        

        self._player.onKeyRelease = self.__onPlayerKeyRelease

        
        self.mainmenu = [
                { 'File': [
                        # {'Open scene': self.__createFilename2Export},
                        # {'Save scene as': self.__createFilename2Export}
                    ]
                }
            ]

        self.initForm()

        # RICARDO TESTING VIDEOS
        #self._video.value = "/home/ricardo/Desktop/animal4_10hz_5sec_25mW_new3_2015-03-16-174109-0000.avi"
        #self._filename.value = "/home/ricardo/Downloads/MA_1_mtout.csv"

        # HUGO TESTING VIDEOS
        # self._video.value = "/home/hugo/subversion_data/20140527_wt-CS-virgin_1_2014-05-27-095957-0000.avi"
        # self._filename.value = "/home/hugo/subversion_data/20140527_wt-CS-virgin_1_2014-05-27-095957-0000_mtout.csv"

        # Experiment related information

        
        #self._video.value = '/home/ricardo/subversion/MEShTracker/Dolphin/DOLPHINS/New Videos/2013.04.21_12.51/2013 04 21 12 51_Entrada (1).MP4'
        #with open('/home/ricardo/Downloads/velocities.csv', 'rb') as csvfile:
        #    import csv
        #    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        #    self._time._time.importchart_csv(spamreader)



    ######################################################################################
    #### HELPERS #########################################################################
    ######################################################################################

    def __createFilename2Export(self, nameformat="%s_events.csv"):
        return 'untitled.csv'
        



    ######################################################################################
    #### EVENTS ##########################################################################
    ######################################################################################
    
    def __onPlayerKeyRelease(self, event):
        """
        Implement the shortcuts keys for the player
        """
        modifier = int(event.modifiers())
        if modifier==QtCore.Qt.ControlModifier and event.key()==QtCore.Qt.Key_O: self.__switchObject()
        if modifier==QtCore.Qt.ControlModifier and event.key()==QtCore.Qt.Key_H: self.__switchHeadTail()
        if modifier==QtCore.Qt.ControlModifier and event.key()==QtCore.Qt.Key_D: self.__searchMismatch()
    



    def __video_changed(self):
        self._player.value = self._video.value
        self._time.max = self._player.max

        # Update fps info on timeline
        self._time._time._video_fps = self._player.fps
        self._time._time._video_fps_min = self._player._form.videoFPS.minimum()
        self._time._time._video_fps_max = self._player._form.videoFPS.maximum()
        self._time._time._video_fps_inc = self._player._form.videoFPS.singleStep()

    def __time_changed(self):
        """
        If the timeline pointer is changed the player position is also changed
        """
        #Flag to avoid recursive position change, between the player and the timeline
        self._update_time = False
        self._player.video_index = self._time.value
        self._player.updateFrame()
        self._update_time = True

    def __timeline_play_video(self):
        """
        Function called when the Play/Pause control is issued from
        the timeline.
        """
        if self._time._time._video_playing:
            timeout_interval = (1000 / self._player.fps)
            print "VIDEO PLAYING @", self._player.fps, "FPS"
            self._player._timer.start(timeout_interval)
        else:
            print "VIDEO STOPPED"
            self._player._timer.stop()

    def __timeline_fps_changed(self):
        """Function called when the FPS rate is changed by the timeline."""
        self._player._form.videoFPS.setValue(self._time._time.fps)
        self._player.videoFPS_valueChanged()

    def __process_frame(self, frame):
        """
        Function called before render each frame
        """
        index = self._player.video_index
        if self._update_time: self._time.value = index

        return frame #Return the frame 2 display




if __name__ == "__main__":  app.startApp(VideoAnnotationEditor)
