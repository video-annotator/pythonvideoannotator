#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pip, os
from subprocess import call

SUBMODULES_FOLDERS = [
    os.path.join('..','libraries','geometry-designer'),
    os.path.join('..','libraries','logging-bootstrap'),
    os.path.join('..','libraries','mcv-api'),
    os.path.join('..','libraries','mcv-gui'),
    os.path.join('..','libraries','mcv-gui-editor'),
    os.path.join('..','libraries','pyforms-gui'),
    os.path.join('..','base','pythonvideoannotator'),
    os.path.join('..','base','pythonvideoannotator-models'),
    os.path.join('..','base','pythonvideoannotator-models-gui'),
    os.path.join('..','plugins','pythonvideoannotator-module-backgroundfinder'),
    os.path.join('..','plugins','pythonvideoannotator-module-contoursimages'),
    os.path.join('..','plugins','pythonvideoannotator-module-createpaths'),
    os.path.join('..','plugins','pythonvideoannotator-module-distances'),
    os.path.join('..','plugins','pythonvideoannotator-module-eventsstats'),
    os.path.join('..','plugins','pythonvideoannotator-module-findorientation'),
    os.path.join('..','plugins','pythonvideoannotator-module-importexport'),
    os.path.join('..','plugins','pythonvideoannotator-module-motioncounter'),
    os.path.join('..','plugins','pythonvideoannotator-module-patheditor'),
    os.path.join('..','plugins','pythonvideoannotator-module-regionsfilter'),
    os.path.join('..','plugins','pythonvideoannotator-module-smoothpaths'),
    os.path.join('..','plugins','pythonvideoannotator-module-timeline'),
    os.path.join('..','plugins','pythonvideoannotator-module-tracking'),
    os.path.join('..','plugins','pythonvideoannotator-module-virtualobjectgenerator'),
    os.path.join('..','plugins','pythonvideoannotator-module-pathmap')
    ]



def install():
    for submodule in SUBMODULES_FOLDERS:
        call(['pip', 'install', '-e', os.path.join(submodule,'.')])

if __name__=='__main__': 
    install()