import cv2
from PyQt4 import QtCore, QtGui
from TrackingDataFile import TrackingDataFile, interpolatePositions

class VideoAnnotationPathEditor(object):

    def __init__(self, title):
        """
        This implements the Path edition functionality
        """
        super(VideoAnnotationPathEditor,self).__init__(title)
        self._selectedItems = []                    #Stores the selected tracked objects
        self._data          = TrackingDataFile()    #Stores the tracked path
        self._points        = []                    #Temporary points. Draw in blue
        self._pathEditMode  = False                 #Path edit mode flag
        self._DEFAULT_HELP_MSG = 'Click in the tracked points to select. Use the Control key for multiple selection.'

    def initForm(self):
        #Add the options to the player popup menu
        self._player.addPopupSubMenuOption('Path', 
            {
                'Delete':           self.__deletePath, 
                'Edit':             self.__editPath,
                'Interpolate':      self.__interpolatePathPoints
            })

        self.mainmenu.append(
                { 'Path': [
                        {'Import': self.__open_tracking_file},
                        {'Export': self.__save_tracking_file},
                        '-',
                        {'Edit': self.__editPath},
                        {'Interpolate': self.__interpolatePathPoints},
                        '-',
                        {'Delete': self.__deletePath}
                    ]
                }
            )

        super(VideoAnnotationPathEditor,self).initForm()




    def __open_tracking_file(self):
        csvfilename = QtGui.QFileDialog.getOpenFileName(parent=self,
            caption="Import annotations file",
            directory="",
            filter="*.csv",
            options=QtGui.QFileDialog.DontUseNativeDialog)

        if csvfilename!=None: 
            self._data = TrackingDataFile(csvfilename)
            self._player.helpText = self._DEFAULT_HELP_MSG

    def __save_tracking_file(self):
        csvfilename = QtGui.QFileDialog.getSaveFileName(parent=self,
            caption="Save file",
            directory="",
            filter="*.csv",
            options=QtGui.QFileDialog.DontUseNativeDialog)

        if csvfilename!=None and self._data!=None: self._data.exportCSV(csvfilename)



    def __deletePath(self):
        if len(self._selectedItems)==2:
            reply = QtGui.QMessageBox.question(self, 'Confirmation', 
                "Are you sure you want to delete this path?", QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                start, end = self._selectedItems[0].frame, self._selectedItems[1].frame
                self._data.deleteRange(start+1, end)
                self._time.addPeriod([start+1, end-1, 'Deleted path'])
                self._player.refresh()
        else:
            QtGui.QMessageBox.about(self, "Error", "You need to select 2 frames.");

    def __editPath(self):
        self._pathEditMode  = not self._pathEditMode
        if self._pathEditMode: 
            self._player.helpText = 'Path edit mode: Contruct the path by selecting a pixel per frame.'
        else:
            self._player.helpText = self._DEFAULT_HELP_MSG
            self._points = []

    def __interpolatePathPoints(self):
        if len(self._selectedItems)==2:
            self._data.interpolateRange(self._selectedItems[0].frame, self._selectedItems[1].frame)
            self._pathEditMode      = False
            self._player.helpText   = self._DEFAULT_HELP_MSG
            self._points            = []
            self._player.refresh()
        else:
            QtGui.QMessageBox.about(self, "Error", "You need to select 2 frames.");


    def onPlayerClick(self, event, x, y):

        if event.button()==1 and not self._pathEditMode: 
            selected = self._data.select(self._player.video_index,x,y)
            if selected!=None:
                modifier = int(event.modifiers())
                #If the control button is pressed will add the blob to the previous selections
                if modifier==QtCore.Qt.ControlModifier:
                    if selected not in self._selectedItems:
                        self._selectedItems.append(selected)
                    else:
                        #Remove the blob in case it was selected before
                        self._selectedItems.remove(selected)
                else:
                    #The control key was not pressed so will select only one
                    self._selectedItems = [ selected ]
            else: self._selectedItems = [] #No object selected: remove previous selections
            self._selectedItems = sorted(self._selectedItems, key=lambda x: x.frame)


        if event.button()==1 and self._pathEditMode: 
            self._data.setPosition(self._player.video_index,x,y)

            #########################################################
            #In case 2 frames are selected, draw the temporary path##
            #########################################################
            if len(self._selectedItems)==2:
                begin   = self._selectedItems[0].frame
                end     = self._selectedItems[1].frame
                positions = []
                for i in range(begin, end+1):
                    data = self._data[i]
                    if data!=None: positions.append([i, data.position])
                positions    = interpolatePositions(positions, begin, end)
                self._points = [pos for frame, pos in positions]
            else:
                self._pathEditMode  = False
            #########################################################



    def process_frame(self, frame):
        """
        Function called before render each frame
        """
        index = self._player.video_index
        if self._update_time: self._time.value = index

        # Draw the current blobs position
        if self._player.isPainted: 
            v = self._data[index]
            if v: v.draw(frame)

        #Draw the selected blobs
        for item in self._selectedItems: item.drawCircle(frame)

        #Draw the selected path
        if 1<=len(self._selectedItems)<=2:
            start = self._selectedItems[0].frame
            end   = index if len(self._selectedItems)==1 else self._selectedItems[1].frame
            for i in range(start, end-1):
                v1 = self._data[i]
                v2 = self._data[i+1]
                if v1!=None and v2!=None:
                    cv2.line( frame, v1.position, v2.position, (0,0,255), 1 )

        #Draw a temporary path
        for i in range(len(self._points)-1):
            p1 = self._points[i]
            p2 = self._points[i+1]
            p1 = ( int(p1[0]),int(p1[1]) )
            p2 = ( int(p2[0]),int(p2[1]) )
            cv2.line( frame, p1, p2, (255,0,0), 1 )

        return frame
