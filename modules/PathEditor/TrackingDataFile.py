import csv, cv2, math, numpy as np
import Utils.tools as tools
from scipy.interpolate import interp1d


def interpolatePositions(values, begin, end, interpolationMode=None):
	computed_time = np.array(range(begin, end+1))
	frames 		= []
	measures_x 	= []
	measures_y 	= []
	
	for i, pos in values:
		x, y = pos
		frames.append(i)
		measures_x.append(x)
		measures_y.append(y)
	
	frames 		= np.array(frames)
	measures_x 	= np.array(measures_x)
	measures_y 	= np.array(measures_y)

	if interpolationMode==None:
		kind = 'slinear'
		if len(frames)==3: kind = 'quadratic'
		if len(frames)>=4: kind = 'cubic'
	else:
		kind = interpolationMode

	
	cubic_interp  = interp1d(frames, measures_x, kind=kind)
	measures_x 	  = cubic_interp(computed_time)
	cubic_interp  = interp1d(frames, measures_y, kind=kind)
	measures_y    = cubic_interp(computed_time)

	results = []
	for frame, x,y in zip( range(begin,end+1), measures_x, measures_y):
		results.append( [frame, (x,y)] )
	return results

class TrackingValue(object):
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







class TrackingDataFile:

	def __init__(self, filename=None):
		self._data = []

		if filename!=None: self.importCSV(filename)

	def importCSV(self, filename):
		with open(filename, 'rb') as csvfile:
			data = []
			spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
			for i, row in enumerate(spamreader):
				rowdata = TrackingValue(row)

				#If the first frame is not 0 then insert none values until the first frame with the position
				if len(data)==0 and rowdata.frame>0:  data = [None for i in range(rowdata.frame)]
				#Add none values for missing frames
				if len(data)>0 and data[-1]!=None and (rowdata.frame-data[-1].frame)>1:
					for i in range(data[-1].frame+1, rowdata.frame): data.append(None)

				data.append(rowdata)
			self._data = data
			
	def deleteRange(self, begin, end):
		for index in range(begin+1, end):
			if index<=len(self._data): self._data[index] = None

	def interpolateRange(self, begin, end, interpolationMode=None):
		positions = []
		for i, data in enumerate(self._data[begin:end+1]):
			if data!=None: positions.append([i+begin, data.position])

		positions = interpolatePositions(positions, begin, end, interpolationMode)

		for frame, (x,y) in positions:
			row = [frame,x,y]
			self._data[frame] = TrackingValue(row)
		

	

	def exportCSV(self, filename):
		with open(filename, 'wb') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='"')
			#spamwriter.writerow(['Frame','Name','pos X','pos Y','head X','head Y','tail X','tail Y'])
			for data in self._data:
				if data!=None:
					spamwriter.writerow([data.frame, data.position[0], data.position[1]])

	def setPosition(self, index, x, y):
		#add positions in case they do not exists
		if index>=len(self._data):
			for i in range(len(self._data), index+1): self._data.append(None)

		row = [index,x,y]
		self._data[index] = TrackingValue(row)


	def select(self, index, x, y):
		if  index<=len(self._data):
			item = self._data[index]
			if item!=None and item.collide(x,y):
				return item		
		return None



	def __getitem__(self, index):
		if index<len(self._data):
			return self._data[index]
		else:
			return None



	def __len__(self): return len(self._data)



if __name__=='__main__':
	data = TrackingDataFile('tmp/output/virgin_wt_CS_2_2014-02-26-103556-0000_mtout.csv')
