import csv
import numpy as np
from scipy.interpolate import interp1d
from pythonvideoannotator.modules.PathEditor.TrackingRow import TrackingRow


def interpolatePositions(values, begin, end, interpolationMode=None):
    computed_time = np.array(range(begin, end + 1))  # pylint: disable=no-member
    frames = []
    measures_x = []
    measures_y = []

    for i, pos in values:
        x, y = pos
        frames.append(i)
        measures_x.append(x)
        measures_y.append(y)

    frames = np.array(frames)  # pylint: disable=no-member
    measures_x = np.array(measures_x)  # pylint: disable=no-member
    measures_y = np.array(measures_y)  # pylint: disable=no-member

    if interpolationMode == None:
        kind = 'slinear'
        if len(frames) == 3:
            kind = 'quadratic'
        if len(frames) >= 4:
            kind = 'cubic'
    else:
        kind = interpolationMode

    cubic_interp = interp1d(frames, measures_x, kind=kind)
    measures_x = cubic_interp(computed_time)
    cubic_interp = interp1d(frames, measures_y, kind=kind)
    measures_y = cubic_interp(computed_time)

    results = []
    for frame, x, y in zip(range(begin, end + 1), measures_x, measures_y):
        results.append([frame, (x, y)])
    return results


class TrackingDataFile:

    def __init__(self, filename=None, separator=',', frameCol=0, xCol=1, yCol=2, zCol=None):
        self._data = []

        TrackingRow.FRAME_COL = frameCol
        TrackingRow.X_COL = xCol
        TrackingRow.Y_COL = yCol
        TrackingRow.Z_COL = zCol

        self._separator = separator
        if filename != None and filename != '':
            self.importCSV(filename)

    def importCSV(self, filename):
        with open(filename, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=self._separator, quotechar='"')
            data = []

            for i, row in enumerate(spamreader):
                if TrackingRow.TOTAL_COLS < len(row):
                    TrackingRow.TOTAL_COLS = len(row)

                rowdata = TrackingRow(row)

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
                v = TrackingRow()
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
            v = TrackingRow()
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
