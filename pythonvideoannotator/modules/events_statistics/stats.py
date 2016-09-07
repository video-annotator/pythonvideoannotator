# !/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import numpy as np
import csv

from PyQt4 import QtGui

import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlProgress
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlCheckBox
from pyforms.Controls import ControlVisVis
from pyforms.Controls import ControlNumber
from pyforms.Controls import ControlBoundingSlider
from pyforms.Controls import ControlCheckBoxList


class Stats(BaseWidget):
	def __init__(self, parent=None, parentWindow=None):
		BaseWidget.__init__(self, 'Events stats', parentWindow=parentWindow)
		self._parent = parent

		self._bounds = ControlBoundingSlider('Frames range', 1, 100, horizontal=True)
		self._nframes = ControlNumber('Merge in a group of', 1800)
		self._videofsp = ControlNumber('FPS', 30.0)
		self._analyseButton = ControlButton('Calculate graphs')
		self._events = ControlCheckBoxList()
		self._graph = ControlVisVis('Graph')
		self._showTotalCounts = ControlCheckBox('Show total events counting')
		self._showEvtsCounts = ControlCheckBox('Show events counting', True)
		self._progress = ControlProgress()
		self._exportDurations = ControlButton('Export durations')
		self._exportTotals = ControlButton('Export totals')

		self._formset = [
			(' ', '_showEvtsCounts', '|', '_showTotalCounts', '|', '_nframes', '_videofsp', '_analyseButton',
			 '_exportDurations', '_exportTotals'),
			'_bounds',
			{'a:Graph': ['_graph'],
			 'c:Events selection': ['_events']},
			'_progress'
		]

		self._analyseButton.value = self.__generate_graph
		self._exportDurations.value = self.__export_durations
		self._exportTotals.value = self.__export_totals
		self._progress.hide()

		self.__load_events()

		self.setMinimumWidth(800)
		self.setMinimumHeight(600)

	def __load_events(self):
		"""
		This function load the events present in the main window
		"""
		self._events_list = []

		event_types = []
		start = None
		end = None
		for track in self._parent.tracks:
			for delta in track.periods:
				if delta.title not in event_types:
					self._events += (delta.title, True)
					event_types.append(delta.title)

				if start == None or start > delta._begin:
					start = delta._begin
				if end == None or end < delta._end:
					end = delta._end

				self._events_list.append((delta._begin, delta._end, delta.title))

		if len(self._events_list) == 0:
			return

		self._events_list = sorted(self._events_list, key=lambda x: (x[1], x[0]))

		# Set the bounding bar for the frames selection
		self._bounds.min = start - 10
		self._bounds.max = end + 10
		self._bounds.value = (start, end)
		self._nframes.min = 1
		self._nframes.max = end

		self.__generate_graph()

	def __do_the_calculations(self):
		self._values2display = []
		self._legends = []
		self._duration = {}

		events_to_include = self._events.value

		# If no events are selected, clean the graph and exit the function
		if len(events_to_include) == 0 or \
				(not self._showTotalCounts.value and not self._showEvtsCounts.value):
			return

		self._progress.min = 0
		self._progress.max = self._bounds.value[1]
		self._progress.value = 0
		self._progress.show()

		framesBin = self._nframes.value
		totalFrames = int(self._bounds.value[1] + 1)
		# Stores the counting related to a all the events
		totalcounts = np.array([0 for x in range(totalFrames)])
		# Stores the counting related each event
		counts = {}

		for label in events_to_include:
			counts[label] = np.array([0 for x in range(totalFrames)])
			self._duration[label] = np.array([0 for x in range(totalFrames)])

		for i in range(0, totalFrames):
			# events_counted - this variable is used to
			# avoid repeating the same event in the current BIN counting
			if (i % framesBin) == 0:
				events_counted = []

			self._progress.value = i

			for j, (start, end, event) in enumerate(self._events_list):
				if start <= i and end >= i and \
						(event in events_to_include) and \
						(j not in events_counted):  # Do not count again a event that was already counted for this BIN

					lowerBound = i - (i % framesBin)
					upperBound = lowerBound + framesBin
					totalcounts[lowerBound:upperBound] += 1
					counts[event][lowerBound:upperBound] += 1

					events_counted.append(j)

				if start <= i and end >= i and (event in events_to_include):
					self._duration[event][i] += 1

		if self._showTotalCounts.value:
			self._values2display.append(totalcounts)
			self._legends.append('All selected events')

		if self._showEvtsCounts.value:
			for label, values in counts.items():
				self._legends.append(label)
				self._values2display.append(values)

		self._progress.hide()

	def __export_durations(self):
		directory = str(QtGui.QFileDialog.getExistingDirectory(self, "Select directory to save the data"))
		if directory != '':
			self.__do_the_calculations()

			events_to_include = self._events.value

			self._progress.min = 0
			self._progress.max = self._bounds.value[1] * len(events_to_include)
			self._progress.value = 0
			self._progress.show()

			framesBin = self._nframes.value
			totalFrames = int(self._bounds.value[1] + 1)

			for j, label in enumerate(events_to_include):
				with open(os.path.join(directory, '{0}.csv'.format(label)), 'wb') as csvfile:

					spamwriter = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
					spamwriter.writerow(
						['Period', 'event', 'start frame', 'end frame', 'duration in frames', 'duration in seconds'])
					for k, i in enumerate(range(0, totalFrames, framesBin)):
						count = sum(self._duration[label][i:i + framesBin])
						time = float(count) / float(self._videofsp.value)
						if count > 0:
							spamwriter.writerow([k, label, i, i + framesBin, count, time])
						self._progress.value = i + self._bounds.value[1] * j

	def __export_totals(self):
		directory = str(QtGui.QFileDialog.getExistingDirectory(self, "Select directory to save the data"))
		if directory != '':
			self.__do_the_calculations()

			events_to_include = self._events.value
			all_periods_ordered_by_time = sorted(self._get_all_periods(), key=lambda x: x._begin)

			# these are special point events to mark experiment start and end
			experiment_start_frame_idx = int(all_periods_ordered_by_time[0].begin)
			experiment_end_frame_idx = int(all_periods_ordered_by_time[-1].begin)

			try:
				# these are special point events to mark experiment start and end
				events_to_include.remove(all_periods_ordered_by_time[0]._title)
				events_to_include.remove(all_periods_ordered_by_time[-1].title)
			except Exception as err:
				print("Warning: {0}".format(str(err)))

			self._progress.min = 0
			self._progress.max = self._bounds.value[1] * len(events_to_include)
			self._progress.value = 0
			self._progress.show()

			framesBin = self._nframes.value  # e.g. 1800 if we want separation in minutes and have 30fps
			totalFrames = int(self._bounds.value[1] + 1)
			# totalFrames = int((experiment_end_time - experiment_start_time) + 1)

			with open(os.path.join(directory, 'totals.csv'), 'wb') as csvfile:
				spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

				for j, label in enumerate(events_to_include):
					spamwriter.writerow([label])
					spamwriter.writerow(['Period', ' Duration (s)', ' Total', ' Occurrences'])
					events_occur = self._find_occurrences(self._duration[label])
					for k, frame_idx in enumerate(
							range(experiment_start_frame_idx, experiment_end_frame_idx, int(framesBin))):

						groups = self.__event_groups_in_frames_threshold(events_occur, frame_idx, frame_idx + framesBin)
						groups_count = len(groups)
						frames_count = sum(self._duration[label][frame_idx:frame_idx + framesBin])
						groups_start_times_str = " ".join(
							[format(((group[0] - experiment_start_frame_idx) / float(framesBin)), ".2f") for group in
							 groups])
						# frames_count = sum(list(len(group) for group in groups))
						time = float(frames_count) / float(self._videofsp.value)
						if frames_count > 0:
							# spamwriter.writerow([k, label, i, i + framesBin, frames_count, "{0:.2f}".format(time), groups_count])
							# spamwriter.writerow(["{period:6}".format(period=k), "{start_second:11}".format(start_second=groups_start_times), "{start_second:15}".format(start_second=i), "{0:13.2f}".format(time), "{count:12}".format(count=groups_count)])

							spamwriter.writerow(["{period:6}".format(period=k), "{0:13.2f}".format(time),
							                     "{count:6}".format(count=groups_count),
							                     "{occur:15}".format(occur=groups_start_times_str)])
						else:
							# spamwriter.writerow([k, label, i, i + framesBin, 0, 0, 0])
							# spamwriter.writerow(["{period:6}".format(period=k), "{start_second:11}".format(start_second=groups_start_times), "{start_second:15}".format(start_second=i), "{dur:13.2f}".format(dur=0), "{count:12}".format(count=0)])
							spamwriter.writerow(["{period:6}".format(period=k), "{dur:13.2f}".format(dur=0),
							                     "{count:6}".format(count=0), "{:15}".format("--")])
						self._progress.value = frame_idx + self._bounds.value[1] * j

					spamwriter.writerow([])
					spamwriter.writerow([])

	def _find_occurrences(self, events):
		"""
		Returns list with indexes of where value is equal to 1
		In other words, indexes represent frames that correspond to event occurrences
		:param events: all durations occurrences list
		e.g. [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
		returns [1, 2, 4, 5, 6, 8, 11, 12, 13, 14, 15, 16, 17, 18]
		"""

		return list(k for k, i in enumerate(events) if i)  # all indexes of 1

	def __event_groups_in_frames_threshold(self, events_occur, frames_threshold_first_index,
	                                       frames_threshold_last_index):
		"""
		Returns list with events occurrences (groups) starting at frames_threshold_first_index, and before frames_threshold_last_index
		e.g.
		events_occur = [1, 2, 4, 5, 6, 8, 11, 12, 13, 14, 15, 16]
		frames_threshold_first_index = 5
		frames_threshold_last_index = 15
		returns [[8], [11, 12, 13, 14, 15, 16]
		"""
		prev = events_occur[0]
		last = 0
		final = []
		for k, i in enumerate(events_occur):
			if (i - prev) > 1:
				final.append(events_occur[last:k])
				last = k
			prev = i
		final.append(events_occur[last:])

		return list(occur for occur in final if
		            occur[0] >= frames_threshold_first_index and occur[0] < frames_threshold_last_index)

	def __generate_graph(self):
		self.__do_the_calculations()

		self._graph.value = self._values2display
		self._graph.legends = self._legends

	def _get_all_periods(self):
		self._time = self._parent
		res = []
		for track in self._time.tracks:
			for delta in track._periods:
				res.append(delta)
		return res


if __name__ == "__main__":
	pyforms.startApp(Stats)
