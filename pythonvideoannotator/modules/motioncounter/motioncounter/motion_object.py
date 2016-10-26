import csv, cv2, os, numpy as np

class MotionObject(object):

	def __init__(self, obj2d):
		self._object2D 		= obj2d
		self._motion 		= []
		self._absmotion 	= []
		self._last_img  	= None
		self._last_diff 	= None
		self._mask			= None

		self.threshold 	= 5
		self.radius 	= 30

	def create_motion_tree_nodes(self): self._object2D.create_motion_tree_nodes()

	def position(self, index):
		m = self._object2D[index]
		return m.position if m else None

	def set_motion(self, index, value):
		self._object2D[index].motion = value

	def init(self):
		self._last_img  	= None
		self._last_diff 	= None
		

	def process(self, index, frame):
		pos = self.position(index)
		if pos is None: return None
		x,y		= pos
		cutx 	= int(round(x-self._radius))
		cuty 	= int(round(y-self._radius))
		cutxx 	= int(round(x+self._radius))
		cutyy 	= int(round(y+self._radius))
		if cutx<0: cutx=0; cutxx=self._radius*2
		if cuty<0: cuty=0; cutyy=self._radius*2

		small	= frame[cuty:cutyy, cutx:cutxx].copy()
		gray	= cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

		
		#print self._mask.shape, gray.shape
		small_masked = cv2.bitwise_and(self._mask, gray)
		if self._last_img==None: self._last_img = small_masked


		diff = cv2.absdiff(small_masked, self._last_img)
		self._last_diff = diff.copy()
		self._last_diff[self._last_diff>self._threshold] = 255

		diff[diff<=self._threshold] = 0
		diff[diff>self._threshold]	= 1

		self._absmotion.append( np.sum(diff) )

		diff = np.float32(small_masked)-np.float32(self._last_img)
		self._motion.append( np.sum(diff) )
		self._last_img 	= small_masked
		
		return self._motion[-1]
		


	def draw(self, index, frame, show_diff=True):
		pos = self.position(index)
		if pos is None: return
		x,y		= pos
		
		if show_diff:
			cv2.circle(frame, (x,y), self._radius, (0,0,0), -1)
			frame[y-self._radius:y+self._radius, x-self._radius:x+self._radius] += cv2.merge( (self._last_diff, self._last_diff, self._last_diff) )
		else:
			cv2.circle(frame, (x,y), self._radius, (0,0,255))



	def export_2_csv(self, path, fly_index, led, total_n_flies=1, data2save=None):
		with open(os.path.join(path,'fly{0}_motion.csv'.format(self._name)), 'w') as csvfile:
			if data2save: csvfile.write( ';'.join(map(str,data2save))+'\n')

			self._events = sorted(self._events, key=lambda x: x)

			csvfile.write( ';'.join(['Frame','Motion','Abs motion','Velocity','Acceleration','Position X','Position Y','Led','Collided']+['Fly {0}'.format(i) for i in range(total_n_flies)])+'\n')
			for i, diff in enumerate(self._motion):
				pos 	= self._positions[i]
				vel 	= self._velocities[i]
				acc 	= self._accels[i]
				absdiff = self._absmotion[i]

				collisions = map(int, self._collisions[i])
				csvfile.write(';'.join(map(str,[i, diff, absdiff, vel, acc, pos[0], pos[1], led[i],int(sum(self._collisions[i])>0) ]+collisions))+'\n')


		with open(os.path.join(path,'fly{0}_events.csv'.format(self._name)), 'w') as csvfile:
			for i in range(fly_index):
				csvfile.write(';'.join(map(str,['T','Fly {0}'.format(i),'#6464ff']))+'\n')

			for i, (start,end,event) in enumerate(self._events):
				csvfile.write(';'.join(map(str,['P',False,start,end,'Collided with Fly {0}'.format(event),'#6464ff',fly_index]))+'\n')


	@property
	def radius(self): return self._radius
	@radius.setter
	def radius(self, value): 
		self._radius = value
		self._mask 	 = np.zeros( (self._radius*2, self._radius*2), dtype=np.uint8 ); 
		cv2.circle(self._mask, (self._radius, self._radius), self._radius, 255, -1 )
		self.init()
	
	@property
	def threshold(self): return self._threshold
	@threshold.setter
	def threshold(self, value): self._threshold = value