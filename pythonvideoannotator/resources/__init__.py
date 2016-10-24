# !/usr/bin/python3
# -*- coding: utf-8 -*-
SETTINGS_PRIORITY = 10

import os
from PyQt4 import QtGui

def path(filename): return os.path.join(os.path.dirname(__file__), 'icons', filename)


PYFORMS_ICON_VIDEOPLAYER_PAUSE_PLAY = QtGui.QIcon()
PYFORMS_ICON_VIDEOPLAYER_PAUSE_PLAY.addPixmap(QtGui.QPixmap(path('play.png')), mode=QtGui.QIcon.Normal, state=QtGui.QIcon.Off)
PYFORMS_ICON_VIDEOPLAYER_PAUSE_PLAY.addPixmap(QtGui.QPixmap(path('pause.png')),mode=QtGui.QIcon.Normal, state=QtGui.QIcon.On)


PYFORMS_ICON_CODEEDITOR_SAVE 		  = QtGui.QIcon(path('export.png'))

PYFORMS_PIXMAP_EVENTTIMELINE_ZOOM_IN  = QtGui.QPixmap(path('zoom_in.png'))
PYFORMS_PIXMAP_EVENTTIMELINE_ZOOM_OUT = QtGui.QPixmap(path('zoom_out.png'))

PYFORMS_ICON_EVENTTIMELINE_IMPORT = QtGui.QIcon(path('import.png'))
PYFORMS_ICON_EVENTTIMELINE_EXPORT = QtGui.QIcon(path('export.png'))


PYFORMS_ICON_FILE_OPEN = QtGui.QIcon(path('link.png'))

ANNOTATOR_ICON_OPEN 	= QtGui.QIcon(path('open.png'))
ANNOTATOR_ICON_SAVE 	= QtGui.QIcon(path('save.png'))
ANNOTATOR_ICON_EXIT 	= QtGui.QIcon(path('exit.png'))
ANNOTATOR_ICON_EDIT 	= QtGui.QIcon(path('edit.png'))
ANNOTATOR_ICON_DELETE 	= QtGui.QIcon(path('delete.png'))
ANNOTATOR_ICON_INTERPOLATE 	= QtGui.QIcon(path('interpolate.png'))
ANNOTATOR_ICON_INTERPOLATION_SETTINGS 	= QtGui.QIcon(path('settings.png'))