import cv2
from PyQt4 import QtCore, QtGui
from pythonvideoannotator.modules.PathEditor.TrackingDataFile import TrackingDataFile, interpolatePositions
from pythonvideoannotator.modules.PathEditor.ChooseColumnsWindow import ChooseColumnsWindow


class VideoAnnotationPathEditor(object):

    def __init__(self, title):
        """
        This implements the Path edition functionality
        """
        super(VideoAnnotationPathEditor, self).__init__(title)
        self._selectedItems = []  # Stores the selected tracked objects
        self._data = TrackingDataFile()  # Stores the tracked path
        self._points = []  # Temporary points. Draw in blue
        self._pathEditMode = False  # Path edit mode flag
        self._interpolationMode = None
        self._DEFAULT_HELP_MSG = 'Click in the tracked points to select. Use the Control key for multiple selection.'

        self._fileSetupWindow = ChooseColumnsWindow()
        self._fileSetupWindow.loadFileEvent = self.__load_tracking_file

        self.mainmenu.append(
            {'Path': [
                {'Import': self.__import_tracking_file},
                {'Export as': self.__export_tracking_file},
                '-',
                {'Save changes': self.__save_tracking_file},
                '-',
                {'Edit': self.__editPath},
                {'Interpolate': self.__interpolatePathPoints},
                {'Interpolation mode': self.__setInterpolationType},
                '-',
                {'Delete': self.__deletePath}
            ]
            }
        )

    def initForm(self):
        # Add the options to the player popup menu
        self._player.addPopupSubMenuOption('Path',
                                           {
                                               'Delete': self.__deletePath,
                                               'Edit': self.__editPath,
                                               'Interpolate': self.__interpolatePathPoints
                                           })

        
        super(VideoAnnotationPathEditor, self).initForm()

    def __setInterpolationType(self):
        items = ("Auto", "Linear", "Quadratic", "Cubic")
        index = 0
        if self._interpolationMode == 'slinear':
            index = 1
        if self._interpolationMode == 'quadratic':
            index = 2
        if self._interpolationMode == 'cubic':
            index = 3

        item, ok = QtGui.QInputDialog.getItem(self, "QInputDialog.getItem()",
                                              "Interpolation mode:", items, index, False)
        if ok and item:
            if item == items[0]:
                self._interpolationMode = None
            if item == items[1]:
                self._interpolationMode = 'slinear'
            if item == items[2]:
                self._interpolationMode = 'quadratic'
            if item == items[3]:
                self._interpolationMode = 'cubic'
            self.__calculateTmpInterpolation()
            self._player.refresh()

    def __import_tracking_file(self):
        self._fileSetupWindow.show()

    def __load_tracking_file(self):
        if self._fileSetupWindow.filename != None:

            separator = self._fileSetupWindow.separator
            frame = self._fileSetupWindow.frameColumn
            x = self._fileSetupWindow.xColumn
            y = self._fileSetupWindow.yColumn
            z = self._fileSetupWindow.zColumn

            self._data = TrackingDataFile(self._fileSetupWindow.filename, separator, frame, x, y, z)
            self._player.help_text = self._DEFAULT_HELP_MSG

            self._fileSetupWindow.close()

    def __export_tracking_file(self):
        csvfilename = QtGui.QFileDialog.getSaveFileName(parent=self,
                                                        caption="Save file",
                                                        directory="",
                                                        filter="*.csv",
                                                        options=QtGui.QFileDialog.DontUseNativeDialog)

        if csvfilename != None and self._data != None:
            self._data.exportCSV(csvfilename)

    def __save_tracking_file(self):
        csvfilename = self._fileSetupWindow.filename
        if csvfilename != '' and csvfilename != None and self._data != None:

            reply = QtGui.QMessageBox.question(self, 'Please confirm',
                                               "Are you sure you want to replace the file {0}?".format(csvfilename),
                                               QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                self._data.exportCSV(csvfilename)

        else:
            QtGui.QMessageBox.about(self, "No file imported", "No file imported yet.")

    def __deletePath(self):
        if len(self._selectedItems) == 2:
            reply = QtGui.QMessageBox.question(self, 'Confirmation',
                                               "Are you sure you want to delete this path?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                start, end = self._selectedItems[0].frame, self._selectedItems[1].frame
                self._data.deleteRange(start + 1, end)
                self._time.addPeriod([start + 1, end - 1, 'Deleted path'])
                self._player.refresh()
        else:
            QtGui.QMessageBox.about(self, "Error", "You need to select 2 frames.")

    def __editPath(self):
        self.pathEditMode = not self.pathEditMode

    def __interpolatePathPoints(self):
        if len(self._selectedItems) == 2:
            self._data.interpolateRange(self._selectedItems[0].frame, self._selectedItems[1].frame, interpolationMode=self._interpolationMode)
            self.pathEditMode = False
        else:
            QtGui.QMessageBox.about(self, "Error", "You need to select 2 frames.")

    def onPlayerClick(self, event, x, y):

        if event.button() == 1 and not self._pathEditMode:
            selected = self._data.select(self._player.video_index, x, y)
            if selected != None:
                modifier = int(event.modifiers())
                # If the control button is pressed will add the blob to the previous selections
                if modifier == QtCore.Qt.ControlModifier:
                    if selected not in self._selectedItems:
                        self._selectedItems.append(selected)
                    else:
                        # Remove the blob in case it was selected before
                        self._selectedItems.remove(selected)
                else:
                    # The control key was not pressed so will select only one
                    self._selectedItems = [selected]
            else:
                self._selectedItems = []  # No object selected: remove previous selections
            self._selectedItems = sorted(self._selectedItems, key=lambda x: x.frame)

        if event.button() == 1 and self._pathEditMode:
            self._data.setPosition(self._player.video_index, x, y)

            #########################################################
            #In case 2 frames are selected, draw the temporary path##
            #########################################################
            if len(self._selectedItems) == 2:
                self.__calculateTmpInterpolation()
            else:
                self.pathEditMode = False
            #########################################################

    def __calculateTmpInterpolation(self):
        begin = self._selectedItems[0].frame
        end = self._selectedItems[1].frame
        positions = []
        for i in range(begin, end + 1):
            data = self._data[i]
            if data != None and data.position != None:
                positions.append([i, data.position])
        positions = interpolatePositions(positions, begin, end, interpolationMode=self._interpolationMode)
        self._points = [pos for frame, pos in positions]

    def process_frame(self, frame):
        """
        Function called before render each frame
        """
        index = self._player.video_index
        if self._update_time:
            self._time.value = index

        # Draw the current blobs position
        if self._player.isPainted and len(self._data) > 0:
            v = self._data[index]

            if v:
                v.draw(frame)
                #if len(v.position)==3: self._player.point = v.position

        # Draw the selected blobs
        for item in self._selectedItems:
            item.drawCircle(frame)

        # Draw the selected path
        if 1 <= len(self._selectedItems) <= 2:
            start = self._selectedItems[0].frame
            end = index if len(self._selectedItems) == 1 else self._selectedItems[1].frame
            for i in range(start, end - 1):
                v1 = self._data[i]
                v2 = self._data[i + 1]
                if v1 != None and v2 != None and v2.position != None and v1.position != None:
                    cv2.line(frame, v1.position, v2.position, (0, 0, 255), 1)

        # Draw a temporary path
        for i in range(len(self._points) - 1):
            p1 = self._points[i]
            p2 = self._points[i + 1]
            p1 = (int(p1[0]), int(p1[1]))
            p2 = (int(p2[0]), int(p2[1]))
            cv2.line(frame, p1, p2, (255, 0, 0), 1)

        return frame

    @property
    def pathEditMode(self): return self._pathEditMode

    @pathEditMode.setter
    def pathEditMode(self, value):
        self._pathEditMode = value
        if value:
            self._player.help_text = 'Click to set a point'
        else:
            self._player.help_text = self._DEFAULT_HELP_MSG
            self._points = []
        self._player.refresh()
