#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pip, os
from subprocess import call

SUBMODULES_FOLDERS = [
    'libraries/geometry-designer',
    'libraries/logging-bootstrap',
    'libraries/mcv-api',
    'libraries/mcv-gui',
    'libraries/mcv-gui-editor',
    'libraries/pyforms-gui',
    'base/pythonvideoannotator',
    'base/pythonvideoannotator-models',
    'base/pythonvideoannotator-models-gui',
    'plugins/pythonvideoannotator-module-backgroundfinder',
    'plugins/pythonvideoannotator-module-contoursimages',
    'plugins/pythonvideoannotator-module-createpaths',
    'plugins/pythonvideoannotator-module-distances',
    'plugins/pythonvideoannotator-module-eventsstats',
    'plugins/pythonvideoannotator-module-findorientation',
    'plugins/pythonvideoannotator-module-importexport',
    'plugins/pythonvideoannotator-module-motioncounter',
    'plugins/pythonvideoannotator-module-patheditor',
    'plugins/pythonvideoannotator-module-regionsfilter',
    'plugins/pythonvideoannotator-module-smoothpaths',
    'plugins/pythonvideoannotator-module-timeline',
    'plugins/pythonvideoannotator-module-tracking',
    'plugins/pythonvideoannotator-module-virtualobjectgenerator',
    'plugins/pythonvideoannotator-module-pathmap'
]



def install():
    for submodule in SUBMODULES_FOLDERS:
        call(['pip', 'install', '-e', os.path.join(submodule,'.')])

if __name__=='__main__': 
    install()