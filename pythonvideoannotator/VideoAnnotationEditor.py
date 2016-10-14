#! /usr/bin/python2
# -*- coding: utf-8 -*-
from pysettings import conf
from pyforms import BaseWidget
from PyQt4 import QtGui, QtCore
from pyforms.Controls import ControlPlayer
from pyforms.Controls import ControlFile
from pyforms.Controls import ControlEventTimeline
from pyforms.Controls import ControlDockWidget



from pythonvideoannotator.modules.PathEditor.VideoAnnotationPathEditor import VideoAnnotationPathEditor
from pythonvideoannotator.modules.Timeline.VideoAnnotationTimeline import VideoAnnotationTimeline
from pythonvideoannotator.modules.events_statistics.events_statistics import EventsStatistics


def Exit():
	exit()


class VideoAnnotationEditor(EventsStatistics, VideoAnnotationPathEditor, VideoAnnotationTimeline, BaseWidget):
	"""Application form"""

	def __init__(self):
		super(VideoAnnotationEditor, self).__init__('Video annotation editor')

		self._video = ControlFile('Video')
		self._player = ControlPlayer("Player")
		self._time = ControlEventTimeline('Time')

		self._dock = ControlDockWidget("Timeline", side='bottom')

		self._formset = ['_video', '_player']

		self._dock.value = self._time

		self._video.changed = self.__video_changed
		self._player.processFrame = self.process_frame
		self._player.onClick = self.onPlayerClick
		self._time.key_release_event = self.__time_key_release_event

		self.mainmenu.insert(0,
		                     {'File': [
			                     {'Exit': Exit}
		                     ]
		                     }
		                     )

		if conf.VIDEO_FILE_PATH: self._video.value = conf.VIDEO_FILE_PATH

	######################################################################################
	#### EVENTS ##########################################################################
	######################################################################################

	def __video_changed(self):
		self._player.value = self._video.value
		self._time.max = self._player.max

		# Update fps info on timeline
		#self._time._time._video_fps = self._player.fps
		#self._time._time._video_fps_min = self._player.videoFPS.minimum()
		#self._time._time._video_fps_max = self._player.videoFPS.maximum()
		#self._time._time._video_fps_inc = self._player.videoFPS.singleStep()

	def __time_key_release_event(self, event):
		print(event)
		# Control video playback using the space bar to Play/Pause
		if event.key() == QtCore.Qt.Key_Space:
			if self._video.is_playing:
				self._video.stop()
			else:
				self._video.play()
			
		
		


		

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


if __name__ == "__main__":
	pass
