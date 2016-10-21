import csv
from pythonvideoannotator.modules.patheditor.object2d.moment import Moment

from pyforms import BaseWidget
from pyforms.Controls import ControlButton





class Object2d(BaseWidget):

    def __init__(self, filename=None, separator=',', frameCol=0, xCol=1, yCol=2, zCol=None):
        super(Object2d, self).__init__('2D Object')

        self._mark_pto_btn = ControlButton('Mark point')

        self._formset   = [ '_mark_pto_btn' ]

        self._data = []

        Moment.FRAME_COL = frameCol
        Moment.X_COL = xCol
        Moment.Y_COL = yCol
        Moment.Z_COL = zCol

        self._separator = separator
        if filename != None and filename != '':
            self.importCSV(filename)

    def importCSV(self, filename):
        with open(filename, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=self._separator, quotechar='"')
            data = []

            for i, row in enumerate(spamreader):
                if Moment.TOTAL_COLS < len(row):
                    Moment.TOTAL_COLS = len(row)

                rowdata = Moment(row)

                # If the first frame is not 0 then insert none values until the first frame with the position
                if len(data) == 0 and rowdata.frame > 0:
                    data = [None for i in range(rowdata.frame)]
                # Add none values for missing frames
                if len(data) > 0 and data[-1] != None and (rowdata.frame - data[-1].frame) > 1:
                    for i in range(data[-1].frame + 1, rowdata.frame):
                        data.append(None)

                data.append(rowdata)
            self._data = data

    def deleteRange(self, begin, end):
        for index in range(begin + 1, end):
            if index <= len(self._data) and self._data[index] != None:
                self._data[index].position = None

    def interpolateRange(self, begin, end, interpolationMode=None):
        positions = []
        for i, data in enumerate(self._data[begin:end + 1]):
            if data != None and data.position != None:
                positions.append([i + begin, data.position])

        positions = interpolatePositions(positions, begin, end, interpolationMode)

        for frame, pos in positions:
            if self._data[frame] != None:
                self._data[frame].position = pos
            else:
                v = Moment()
                v.frame = frame
                v.position = pos
                self._data[frame] = v

    def exportCSV(self, filename):
        with open(filename, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=self._separator)
            #spamwriter.writerow(['Frame','Name','pos X','pos Y','head X','head Y','tail X','tail Y'])
            for data in self._data:
                if data != None:
                    spamwriter.writerow(data.row)

    def setPosition(self, index, x, y):
        # add positions in case they do not exists
        if index >= len(self._data):
            for i in range(len(self._data), index + 1):
                self._data.append(None)

        if self._data[index] == None:
            v = Moment()
            v.frame = index
            v.position = (x, y)
            self._data[index] = v
        else:
            v = self._data[index]
            v.position = (x, y)

    def select(self, index, x, y):
        if index <= len(self._data) and index>=0:
            item = self._data[index]
            if item != None and item.collide(x, y):
                return item
        return None

    def __getitem__(self, index):
        if index < len(self._data):
            return self._data[index]
        else:
            return None

    def __len__(self): return len(self._data)


if __name__ == '__main__':
    data = TrackingDataFile('tmp/output/virgin_wt_CS_2_2014-02-26-103556-0000_mtout.csv')
