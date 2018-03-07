# Python Video Annotator

[Documentation on ReadTheDocs](https://pythonvideoannotator.readthedocs.io)


The software is an application written in python, which provides a GUI for users to analyse and to take notes of events occurred in the videos.

Features:
* Timeline for video navigation.
* Multiple events edition in the timeline.
* Graphs visualization over time.
* Objects tracking path edition.
* Plugins based app.

[![Video](/docs/video.png)](https://www.youtube.com/watch?v=IE_mtCHc9bQ)


### Developers

* Ricardo Ribeiro - collaborator of the [Scientific Software Platform](http://neuro.fchampalimaud.org/en/research/platforms/staff/Scientific%20Software/) of the [Champalimaud Foundation](http://fchampalimaud.org).
* Hugo Cachitas working - collaborator of the [Innate Behavior Lab](http://neuro.fchampalimaud.org/en/research/investigators/research-groups/group/Vasconcelos/) of the [Champalimaud Foundation](http://fchampalimaud.org).
* Carlos Mão de Ferro - collaborator of the [Scientific Software Platform](http://neuro.fchampalimaud.org/en/research/platforms/staff/Scientific%20Software/) of the [Champalimaud Foundation](http://fchampalimaud.org).


![Video annotator screenshot](/docs/screenshot.png?raw=true "Screen")

## Installation & Running

- Download & install [Anaconda](https://www.anaconda.com/download/) or  [Miniconda](https://conda.io/miniconda.html).
- Download the environment configuration file [windows](https://raw.githubusercontent.com/UmSenhorQualquer/pythonVideoAnnotator/master/environment-windows.yml) / [mac](https://raw.githubusercontent.com/UmSenhorQualquer/pythonVideoAnnotator/master/environment-macosx.yml).
- Open an anaconda prompt, install and activate the environment by running the next commands in the terminal:

for windows:
```
conda env create -f environment-windows.yml
source activate videoannotator
python install.py
```

for mac:
```
conda env create -f environment-macosx.yml
source activate videoannotator
python install.py
```
- Clone the python video annotator repository by running the next command in the terminal: 

```
git clone https://github.com/UmSenhorQualquer/pythonVideoAnnotator.git
```

- Install the code:

```
cd pythonVideoAnnotator
python install.py
```

- Execute the code:

```
python -m pythonvideoannotator
```

### Run

In the Video Annotator folder in the Terminal run:

for mac:
```
source activate videoannotator
python -m pythonvideoannotator
```
for windows:
```
activate videoannotator
python -m pythonvideoannotator
```


### Collaboration

This project was initially developed in collaboration with the [Innate Behavior Lab](http://neuro.fchampalimaud.org/en/research/investigators/research-groups/group/Vasconcelos/) to correct the result of a Computer Vision software to track flies in an arena
