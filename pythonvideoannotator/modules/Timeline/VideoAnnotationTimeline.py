import os


class VideoAnnotationTimeline(object):

    def __init__(self, title):
        """
        This implements the Path edition functionality
        """
        super(VideoAnnotationTimeline, self).__init__(title)
        self._update_time = True  # Use to avoid double video jump 2 frame trigger

    def initForm(self):
        self._time.pointerChanged = self.__time_changed
        self._time.isPlaying = self.__timeline_play_video
        self._time.fpsChanged = self.__timeline_fps_changed
        #self._time.getExportFilename= self.__createFilename2Export

        super(VideoAnnotationTimeline, self).initForm()

    ######################################################################################
    #### HELPERS #########################################################################
    ######################################################################################

    def __createFilename2Export(self, nameformat="%s_events.csv"):
        if self._filename.value == '':
            return 'untitled.csv'
        filepath = os.path.dirname(self._filename.value)
        filename = os.path.basename(self._filename.value)
        name, ext = os.path.splitext(filename)
        return os.path.join(filepath, nameformat % name)

    ######################################################################################
    #### EVENTS ##########################################################################
    ######################################################################################

    def __time_changed(self):
        """
        If the timeline pointer is changed the player position is also changed
        """
        # Flag to avoid recursive position change, between the player and the timeline
        self._update_time = False
        self._player.video_index = self._time.value
        self._player.update_frame()
        self._update_time = True

    def __timeline_play_video(self):
        """
        Function called when the Play/Pause control is issued from
        the timeline.
        """
        if self._time._time._video_playing:
            timeout_interval = (1000 / self._player.fps)
            print("VIDEO PLAYING @", self._player.fps, "FPS")
            self._player._timer.start(timeout_interval)
        else:
            print("VIDEO STOPPED")
            self._player._timer.stop()

    def __timeline_fps_changed(self):
        """Function called when the FPS rate is changed by the timeline."""
        self._player._form.videoFPS.setValue(self._time._time.fps)
        self._player.videoFPS_valueChanged()
