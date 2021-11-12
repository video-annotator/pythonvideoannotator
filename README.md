# Python Video Annotator

[Documentation on ReadTheDocs](https://pythonvideoannotator.readthedocs.io)


The software is an application written in python, which provides a GUI for users to analyse and to take notes of events occurred in the videos.

Features:
* Timeline for video navigation.
* Multiple events edition in the timeline.
* Graphs visualization over time.
* Objects tracking path edition.
* Plugins based app.

[![Video](docs/youtube.png)](https://www.youtube.com/watch?v=9C4Zr8fhqFo&t=63s)

![Video annotator screenshot](docs/screenshot.png "Screen")

## Installation & Running

How to install:

1. Create a Virtual Environment (highly recommended) on your preferred Python distribution with Python 3.6:
   * example with Anaconda in Anaconda Prompt

    ```bash
    conda create -n videoannotator python=3.6

    ...

    conda activate videoannotator
    ```

2. Make sure you are in the just created virtual environment and install PythonVideoAnnotator with pip:

    ```bash
    pip install python-video-annotator
    ```

## Intel Mac installation
### MacOS Catalina

1. Start with a fresh Virtual Environment (highly recommended) on your preferred Python distribution with Python 3.6:
   * example with Anaconda in Anaconda Prompt

    ```bash
    conda create -n videoannotator python=3.6

    ...

    conta activate videoannotator
    ```

2. Install some of the dependencies that might present issues as:

    ```bash
    pip install opencv-python-headless pyqt5==5.14.1 pyqtwebengine==5.14.0
    ```

3. Install Python Video Annotator

    ```bash
    pip install python-video-annotator
    ```

### MacOS Mojave

1. Start with a fresh Virtual Environment (highly recommended) on your preferred Python distribution with Python 3.8:
   * example with Anaconda in Anaconda Prompt

    ```bash
    conda create -n videoannotator python=3.8

    ...

    conta activate videoannotator
    ```

2. Install PyFormsGUI 5 first

    ```bash
    pip install pyforms-gui==5
    ```

3. Downgrade PyQt5 and QScintilla:

    ```bash
    pip install --upgrade qscintilla==2.11.4 pyqt5==5.14.1 pyqtwebengine==5.14.0
    ```

4. Install missing packages

    ```bash 
    pip install opencv-python-headless PyOpenGL_accelerate
    ```

5. Install Python Video Annotator, ignoring dependencies (will be installed afterwards since it has a conflict with opencv version)

    ```bash
    pip install python-video-annotator==3.306 --no-deps
    ```

6. Install python-video-annotator dependencies except the one that created conflicts (older version of opencv-python)

    ```bash
    pip install geometry-designer modular-computer-vision-api modular-computer-vision-api-gui pypi-xmlrpc python-video-annotator-models python-video-annotator-models-gui python-video-annotator-module-background-finder python-video-annotator-module-contours-images python-video-annotator-module-create-paths python-video-annotator-module-deeplab python-video-annotator-module-distances python-video-annotator-module-eventstats python-video-annotator-module-find-orientation python-video-annotator-module-import-export python-video-annotator-module-motion-counter python-video-annotator-module-path-editor python-video-annotator-module-path-map python-video-annotator-module-regions-filter python-video-annotator-module-smooth-paths python-video-annotator-module-timeline python-video-annotator-module-tracking python-video-annotator-module-virtual-object-generator scipy send2trash simplejson sklearn
    ```

How to run:

1. After the installation completes, you can start Python Video Annotator with:

    ```bash
    start-video-annotator
    ```

### For developers

[Follow the steps described here](https://pythonvideoannotator.readthedocs.io/en/master/user-docs/install_and_run/index.html#for-developers)


## Developers

* Ricardo Ribeiro - collaborator of the [Scientific Software Platform](http://neuro.fchampalimaud.org/en/research/platforms/staff/Scientific%20Software/) of the [Champalimaud Foundation](http://fchampalimaud.org).
* Hugo Cachitas working - collaborator of the [Innate Behavior Lab](http://neuro.fchampalimaud.org/en/research/investigators/research-groups/group/Vasconcelos/) of the [Champalimaud Foundation](http://fchampalimaud.org).
* Carlos Mão de Ferro - collaborator of the [Scientific Software Platform](http://neuro.fchampalimaud.org/en/research/platforms/staff/Scientific%20Software/) of the [Champalimaud Foundation](http://fchampalimaud.org).
* Luís Teixeira - collaborator of the [Scientific Software Platform](http://neuro.fchampalimaud.org/en/research/platforms/staff/Scientific%20Software/) of the [Champalimaud Foundation](http://fchampalimaud.org).

## Collaboration

This project was initially developed in collaboration with the [Innate Behavior Lab](http://neuro.fchampalimaud.org/en/research/investigators/research-groups/group/Vasconcelos/) to correct the result of a Computer Vision software to track flies in an arena
