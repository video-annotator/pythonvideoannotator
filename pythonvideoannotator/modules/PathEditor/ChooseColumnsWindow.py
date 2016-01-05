from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlFile
from pyforms.Controls import ControlCheckBox
from pyforms.Controls import ControlList
from pyforms.Controls import ControlNumber

import pyforms

import csv


class ChooseColumnsWindow(BaseWidget):

    def __init__(self):
        super(ChooseColumnsWindow, self).__init__('CSV Choose the columns')
        self._filename = None

        # Definition of the forms fields
        self._filename = ControlFile('File')
        self._separator = ControlText('Separator', ';')
        self._frameCol = ControlNumber('Frame column', 0, 0, 100)
        self._xCol = ControlNumber('X column', 1, 0, 100)
        self._yCol = ControlNumber('Y column', 2, 0, 100)
        self._showZ = ControlCheckBox('Import Z value')			# Not being used yet
        self._zCol = ControlNumber('Z column', 0, 0, 100)		# Not being used yet
        self._filePreview = ControlList('Preview')
        self._loadButton = ControlButton('Load')

        self._formset = ['_filename', ('_separator', '_frameCol', '_xCol', '_yCol', '_loadButton'), '_filePreview']
        self._separator.changed = self.__refreshPreview
        self._filename.changed = self.__refreshPreview

        self._zCol.hide()
        self._showZ.changed = self.__showZChanged

    def __showZChanged(self):
        if self._showZ.value:
            self._zCol.show()
        else:
            self._zCol.hide()

    @property
    def filename(self): return self._filename.value

    @filename.setter
    def filename(self, value):
        self._filename.value = value
        self.__refreshPreview()

    @property
    def loadFileEvent(self): return self._loadButton.value

    @loadFileEvent.setter
    def loadFileEvent(self, value): self._loadButton.value = value

    @property
    def separator(self): return self._separator.value

    @property
    def frameColumn(self): return self._frameCol.value

    @property
    def xColumn(self): return self._xCol.value

    @property
    def yColumn(self): return self._yCol.value

    @property
    def zColumn(self):
        if self._showZ.value:
            return self._zCol.value
        else:
            return None

    def __refreshPreview(self):
        if self._filename.value != None and self._filename.value != '':
            with open(self._filename.value) as csvfile:
                spamreader = csv.reader(csvfile, delimiter=self._separator.value)
                self._filePreview.value = []
                self._filePreview.horizontalHeaders = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", ]
                for i, row in enumerate(spamreader):
                    self._filePreview += row
                    if i >= 10:
                        break

##################################################################################################################
##################################################################################################################
##################################################################################################################

# Execute the application
if __name__ == "__main__":
    pyforms.startApp(ChooseColumnsWindow)
