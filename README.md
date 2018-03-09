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


### Developers

* Ricardo Ribeiro - collaborator of the [Scientific Software Platform](http://neuro.fchampalimaud.org/en/research/platforms/staff/Scientific%20Software/) of the [Champalimaud Foundation](http://fchampalimaud.org).
* Hugo Cachitas working - collaborator of the [Innate Behavior Lab](http://neuro.fchampalimaud.org/en/research/investigators/research-groups/group/Vasconcelos/) of the [Champalimaud Foundation](http://fchampalimaud.org).
* Carlos Mão de Ferro - collaborator of the [Scientific Software Platform](http://neuro.fchampalimaud.org/en/research/platforms/staff/Scientific%20Software/) of the [Champalimaud Foundation](http://fchampalimaud.org).


![Video annotator screenshot](docs/screenshot.png "Screen")

## Installation & Running

- Download & install [Anaconda](https://www.anaconda.com/download/) or  [Miniconda](https://conda.io/miniconda.html).
- Download & install the environment configuration file.

for windows:  
**Note:** make sure you are using the Anaconda prompt to execute the next commands.
```
conda install -c menpo wget
wget https://raw.githubusercontent.com/UmSenhorQualquer/pythonVideoAnnotator/master/environment-windows.yml --no-check-certificate
conda env create -f environment-windows.yml
conda activate videoannotator
```

for mac:
```
wget https://raw.githubusercontent.com/UmSenhorQualquer/pythonVideoAnnotator/master/environment-macosx.yml --no-check-certificate
conda env create -f environment-macosx.yml
source activate videoannotator
```

- Activate the environment, download the source code and install it:

```
git clone --recursive https://github.com/UmSenhorQualquer/pythonVideoAnnotator.git
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
