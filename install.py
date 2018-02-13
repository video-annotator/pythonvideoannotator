#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pip, os
from subprocess import call

SUBMODULES_FOLDERS = [
    'geometry-designer',
    'logging-bootstrap',
    'mcv-api',
    'mcv-gui',
    'mcv-gui-editor',
    'pyforms',
    'pyforms',
    '.',
    'pythonvideoannotator-models',
    'pythonvideoannotator-models-gui',
    'pythonvideoannotator-module-backgroundfinder',
    'pythonvideoannotator-module-contoursimages',
    'pythonvideoannotator-module-createpaths',
    'pythonvideoannotator-module-distances',
    'pythonvideoannotator-module-eventsstats',
    'pythonvideoannotator-module-findorientation',
    'pythonvideoannotator-module-importexport',
    'pythonvideoannotator-module-motioncounter',
    'pythonvideoannotator-module-patheditor',
    'pythonvideoannotator-module-regionsfilter',
    'pythonvideoannotator-module-smoothpaths',
    'pythonvideoannotator-module-timeline',
    'pythonvideoannotator-module-tracking',
    'pythonvideoannotator-module-virtualobjectgenerator'
]



def install():
    for submodule in SUBMODULES_FOLDERS:
        pip.main(['install', '--upgrade', os.path.join(submodule,'.')])

def check_submodules():
    for submodule in SUBMODULES_FOLDERS:
        if not os.path.exists(os.path.join(submodule,'setup.py')):
            call(["git", "submodule", "update", "--init", "--recursive"])
            break



if __name__=='__main__': 
    check_submodules()
    install()