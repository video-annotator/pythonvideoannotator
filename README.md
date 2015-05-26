# Python Video Annotator

The software is a standalone application writen in python, which intend to provide a GUI for users to take notes of events occurred in the videos.

## Initial propose

It was initially developed in collaboration with the Innate Behavior Lab to correct the result of a Computer Vision software to track flies in an arena.

Later was modified to become more generic.

## Developers

* Ricardo Ribeiro - working in the [Scientific Software Platform](http://neuro.fchampalimaud.org/en/research/platforms/staff/Scientific%20Software/) of the Champalimaud Foundation
* Hugo Cachitas working - working in the [Innate Behavior Lab](http://neuro.fchampalimaud.org/en/research/investigators/research-groups/group/Vasconcelos/) of the Champalimaud Foundation


![Video annotator screenshot](/docs/screencapture.png?raw=true "Screen")

## Installation & Running

The application was developed and tested with Ubuntu 12.04 and 14.0.

### Dependencies

* Python 2.7
* PyQt4
	* sudo apt-get install pyqt4-dev-tools python-qt4 python-qt4-gl
* Numpy
	* sudo apt-get install python-numpy
* PyOpenGL
	* sudo pip install pyopengl
* Python OpenCV
	* sudo apt-get install python-opencv

### Running

From the Terminal run:

```
python VideoAnnotationEditor.py
```