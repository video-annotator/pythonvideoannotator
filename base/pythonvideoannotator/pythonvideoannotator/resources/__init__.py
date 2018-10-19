# !/usr/bin/python3
# -*- coding: utf-8 -*-
SETTINGS_PRIORITY = 10

import os, AnyQt
from confapp import conf

if conf.PYFORMS_MODE=='GUI':
	from AnyQt import QtGui

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

ANNOTATOR_ICON_REFRESH 	= QtGui.QIcon(path('refresh.png'))
ANNOTATOR_ICON_PATH 	= QtGui.QIcon(path('path.png'))
ANNOTATOR_ICON_DATASETS 	= QtGui.QIcon(path('datasets.png'))
ANNOTATOR_ICON_OBJECT 	= QtGui.QIcon(path('object.png'))
ANNOTATOR_ICON_OPEN 	= QtGui.QIcon(path('open.png'))
ANNOTATOR_ICON_SAVE 	= QtGui.QIcon(path('save.png'))
ANNOTATOR_ICON_EXIT 	= QtGui.QIcon(path('exit.png'))
ANNOTATOR_ICON_EDIT 	= QtGui.QIcon(path('edit.png'))
ANNOTATOR_ICON_DELETE 	= QtGui.QIcon(path('delete.png'))
ANNOTATOR_ICON_INTERPOLATE 	= QtGui.QIcon(path('interpolate.png'))
ANNOTATOR_ICON_INTERPOLATION_SETTINGS 	= QtGui.QIcon(path('settings.png'))
ANNOTATOR_ICON_X 	= QtGui.QIcon(path('x.png'))
ANNOTATOR_ICON_Y 	= QtGui.QIcon(path('y.png'))
ANNOTATOR_ICON_TIMELINE 	= QtGui.QIcon(path('timeline.png'))
ANNOTATOR_ICON_VELOCITY 	= QtGui.QIcon(path('velocity.png'))
ANNOTATOR_ICON_ACCELERATION 	= QtGui.QIcon(path('acceleration.png'))
ANNOTATOR_ICON_POSITION 	= QtGui.QIcon(path('position.png'))
ANNOTATOR_ICON_ADD 	= QtGui.QIcon(path('add.png'))
ANNOTATOR_ICON_REMOVE 	= QtGui.QIcon(path('remove.png'))
ANNOTATOR_ICON_MARKPLACE 	= QtGui.QIcon(path('mark-place.png'))
ANNOTATOR_ICON_SELECTPOINT 	= QtGui.QIcon(path('select-point.png'))
ANNOTATOR_ICON_DELETEPATH 	= QtGui.QIcon(path('delete-path.png'))
ANNOTATOR_ICON_MOTION 	= QtGui.QIcon(path('motion.png'))
ANNOTATOR_ICON_CONTOUR 	= QtGui.QIcon(path('contour.png'))
ANNOTATOR_ICON_AREA 	= QtGui.QIcon(path('area.png'))
ANNOTATOR_ICON_REGIONS 	= QtGui.QIcon(path('regions.png'))
ANNOTATOR_ICON_VIDEO 	= QtGui.QIcon(path('video.png'))
ANNOTATOR_ICON_COLORS 	= QtGui.QIcon(path('colors.png'))
ANNOTATOR_ICON_COLOR_COMPONENT 	= QtGui.QIcon(path('color-component.png'))
ANNOTATOR_ICON_CIRCLE 	= QtGui.QIcon(path('circle.png'))
ANNOTATOR_ICON_ELLIPSE 	= QtGui.QIcon(path('ellipse.png'))
ANNOTATOR_ICON_HULL 	= QtGui.QIcon(path('hull.png'))
ANNOTATOR_ICON_BLACK_CIRCLE 	= QtGui.QIcon(path('black-circle.png'))
ANNOTATOR_ICON_WIDTH 	= QtGui.QIcon(path('width.png'))
ANNOTATOR_ICON_HEIGHT 	= QtGui.QIcon(path('height.png'))
ANNOTATOR_ICON_ASPECT_RATIO 	= QtGui.QIcon(path('aspect-ratio.png'))
ANNOTATOR_ICON_INFO 	= QtGui.QIcon(path('info.png'))
ANNOTATOR_ICON_ANGLE 	= QtGui.QIcon(path('angle.png'))
ANNOTATOR_ICON_POINT 	= QtGui.QIcon(path('point.png'))

ANNOTATOR_ICON_PICTURE	= QtGui.QIcon(path('picture.png'))
ANNOTATOR_ICON_SMOOTH	= QtGui.QIcon(path('smooth.png'))
ANNOTATOR_ICON_NEW	= QtGui.QIcon(path('new.png'))
ANNOTATOR_ICON_IMAGE	= QtGui.QIcon(path('image.png'))

ANNOTATOR_ICON_BACKGROUND	= QtGui.QIcon(path('background.png'))
ANNOTATOR_ICON_MOVIE	= QtGui.QIcon(path('movie.png'))
ANNOTATOR_ICON_MOVIES	= QtGui.QIcon(path('movies.png'))


ANNOTATOR_ICON_NOTE	= QtGui.QIcon(path('note.png'))
ANNOTATOR_ICON_GEOMETRY	= QtGui.QIcon(path('geometry.png'))

ANNOTATOR_ICON_PATHMAP	= QtGui.QIcon(path('pathmap.png'))


ANNOTATOR_ICON_DISTANCES	= QtGui.QIcon(path('distances.png'))

ANNOTATOR_ICON_DUPLICATE	= QtGui.QIcon(path('duplicate.png'))