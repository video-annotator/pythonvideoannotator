#! /usr/bin/python
from __init__ import *
import os, cv2
from PyQt4                                        import QtCore, QtGui
from modules.PathEditor.TrackingDataFile          import TrackingDataFile
from modules.PathEditor.VideoAnnotationPathEditor import VideoAnnotationPathEditor
from modules.Timeline.VideoAnnotationTimeline     import VideoAnnotationTimeline

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

        
        # Experiment related information

        #self._video.value = '/home/ricardo/Downloads/output/apt_82_mtout_copy.avi'
        #self._video.value = '/home/ricardo/subversion/MEShTracker/Dolphin/DOLPHINS/New Videos/2013.03.16_12.18/2013 03 16 12 18_Cascata.MP4'
        """
        with open('/home/ricardo/subversion/opencsp/applications/dolphin3Dposition/output/total_velocities.csv', 'rb') as csvfile:
            import csv
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            self._time._time.importchart_csv(spamreader)
        with open('/home/ricardo/subversion/opencsp/applications/dolphin3Dposition/output/3dpositions_z.csv', 'rb') as csvfile:
            import csv
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            self._time._time.importchart_csv(spamreader)"""
        #self._data = TrackingDataFile('/home/ricardo/Downloads/2013.03.16_12.18/Camera2_corrected.csv')
        

        #self._video.value = '/home/ricardo/Desktop/GOPR0444.MP4'

   
    ######################################################################################
    #### EVENTS ##########################################################################
    ######################################################################################

    def __video_changed(self):
        self._player.value = self._video.value
        self._time.max = self._player.max

        # Update fps info on timeline
        self._time._time._video_fps = self._player.fps
        self._time._time._video_fps_min = self._player.videoFPS.minimum()
        self._time._time._video_fps_max = self._player.videoFPS.maximum()
        self._time._time._video_fps_inc = self._player.videoFPS.singleStep()



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
