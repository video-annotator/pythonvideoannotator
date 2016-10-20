import math
import cv2


class TrackingRow(object):

    FRAME_COL = 0
    X_COL = 1
    Y_COL = 2
    Z_COL = None
    TOTAL_COLS = 3

    def __init__(self, row=None): self.row = row

    @property
    def row(self):
        if self._row == None:
            z = 0 if self.Z_COL != None else self.Z_COL
            self._row = [None for x in range(max(self.FRAME_COL, self.X_COL, self.Y_COL, z) + 1)]

        self._row[self.FRAME_COL] = self._frame
        if self.position == None:
            self._row[self.X_COL] = None
            self._row[self.Y_COL] = None
            if self.Z_COL != None:
                self._row[self.Z_COL] = None
        else:
            self._row[self.X_COL] = self._position[0]
            self._row[self.Y_COL] = self._position[1]
            if self.Z_COL != None:
                self._row[self.Z_COL] = self._position[2]
        return self._row

    @row.setter
    def row(self, row):
        self._row = row
        if row != None:
            self.frame = int(float(row[self.FRAME_COL]))
            if 	len(row) > max(self.X_COL, self.Y_COL, 0 if self.Z_COL != None else self.Z_COL) \
                    and len(row[self.X_COL]) > 0 and len(row[self.Y_COL]) > 0:
                if self.Z_COL != None:
                    self.position = int(float(row[self.X_COL])), int(float(row[self.Y_COL])), float(row[self.Z_COL])
                else:
                    self.position = int(float(row[self.X_COL])), int(float(row[self.Y_COL]))
            else:
                self.position = None

    @property
    def frame(self): return self._frame

    @frame.setter
    def frame(self, value): self._frame = value

    @property
    def position(self): return self._position

    @position.setter
    def position(self, value):
        if value != None:
            if len(value) == 3:
                self._position = (int(round(value[0])), int(round(value[1])), int(round(value[2])))
            else:
                self._position = (int(round(value[0])), int(round(value[1])))
        else:
            self._position = None

    def drawCircle(self, frame):
        if self.position != None:
            cv2.circle(frame, self.position[:2], 20, (255, 255, 255), 4, lineType=cv2.LINE_AA)  # pylint: disable=no-member
            cv2.circle(frame, self.position[:2], 20, (50, 50, 255), 1, lineType=cv2.LINE_AA)  # pylint: disable=no-member

            cv2.putText(frame, str(self._frame), self._position[:2], cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness=2, lineType=cv2.LINE_AA)  # pylint: disable=no-member
            cv2.putText(frame, str(self._frame), self._position[:2], cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), thickness=1, lineType=cv2.LINE_AA)  # pylint: disable=no-member

    def draw(self, frame):
        if self.position != None:
            cv2.circle(frame, self.position[:2], 5, (255, 255, 255), -1, lineType=cv2.LINE_AA)  # pylint: disable=no-member
            cv2.circle(frame, self.position[:2], 3, (255, 0, 255), -1, lineType=cv2.LINE_AA)  # pylint: disable=no-member

    def collide(self, x, y):
        if self.position == None:
            return False
        return math.sqrt((self.position[0] - x)**2 + (self.position[1] - y)**2) < 20
