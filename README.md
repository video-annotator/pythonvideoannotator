# Python Video Annotator

[Binary downloads](https://bitbucket.org/fchampalimaud/pythonvideoannotator/downloads)


The software is a standalone application written in python, which provides a GUI for users to analyse and to take notes of events occurred in the videos.

Features:
* Timeline for video navigation.
* Multiple events edition in the timeline.
* Graphs visualization over time.
* Objects tracking path edition.


[![Video](/docs/video.png)](https://www.youtube.com/watch?v=IE_mtCHc9bQ)


### Developers

* Ricardo Ribeiro - collaborator of the [Scientific Software Platform](http://neuro.fchampalimaud.org/en/research/platforms/staff/Scientific%20Software/) of the [Champalimaud Foundation](http://fchampalimaud.org).
* Hugo Cachitas working - collaborator of the [Innate Behavior Lab](http://neuro.fchampalimaud.org/en/research/investigators/research-groups/group/Vasconcelos/) of the [Champalimaud Foundation](http://fchampalimaud.org).
* Carlos Mão de Ferro - collaborator of the [Scientific Software Platform](http://neuro.fchampalimaud.org/en/research/platforms/staff/Scientific%20Software/) of the [Champalimaud Foundation](http://fchampalimaud.org).


![Video annotator screenshot](/docs/screencapture.png?raw=true "Screen")

![Video annotator screenshot](/docs/screenshot.png?raw=true "Screen")

## Installation & Running

The application was developed and tested with Ubuntu 12.04 and 14, OSX El Capitan, Windows 7.

### Dependencies

* Python 2.7
* PyQt4: ```sudo apt-get install pyqt4-dev-tools python-qt4 python-qt4-gl```
* Numpy: ```sudo apt-get install python-numpy```
* PyOpenGL: ```sudo pip install pyopengl```
* Python OpenCV: ```sudo apt-get install python-opencv```
* Scipy: ```sudo apt-get install python-scipy```
* PyForms: ```sudo pip install git+git://github.com/UmSenhorQualquer/pyforms.git```

### Run

From the Terminal run:

```
python -m pythonvideoannotator
```


### Collaboration

This project was initially developed in collaboration with the [Innate Behavior Lab](http://neuro.fchampalimaud.org/en/research/investigators/research-groups/group/Vasconcelos/) to correct the result of a Computer Vision software to track flies in an arena
