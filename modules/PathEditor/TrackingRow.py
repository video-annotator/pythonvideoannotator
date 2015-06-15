import csv, cv2, math, numpy as np
import cv2
import Utils.tools as tools
from scipy.interpolate import interp1d

class TrackingRow(object):
	def __init__(self, row):
		self.row 	= row
		self._index	= None

	@property
	def row(self):
	    return [ self._frame, self._position[0], self._position[1] ]

	@row.setter
	def row(self, row):
		self._frame 	= int(float(row[0]))
		self._position 	= int(float(row[1])), int(float(row[2]))

	@property
	def frame(self): return self._frame

	@property
	def position(self): return self._position


	def drawCircle(self, frame):
		cv2.circle(frame, self.position, 20, (255,255,255), 4, lineType=cv2.CV_AA)
		cv2.circle(frame, self.position, 20, (50,50,255), 1, lineType=cv2.CV_AA)

		cv2.putText(frame, str(self._frame), self._position, cv2.FONT_HERSHEY_PLAIN, 1.0, (0,0,0), thickness=2, lineType=cv2.CV_AA)
		cv2.putText(frame, str(self._frame), self._position, cv2.FONT_HERSHEY_PLAIN, 1.0, (255,255,255), thickness=1, lineType=cv2.CV_AA)

	def draw(self, frame):
		cv2.circle(frame, self.position, 5, (255,255,255), -1, lineType=cv2.CV_AA)
		cv2.circle(frame, self.position, 3, (255,0,255), -1, lineType=cv2.CV_AA)

	def collide(self, x, y): return tools.lin_dist(self.position, (x,y))<20
