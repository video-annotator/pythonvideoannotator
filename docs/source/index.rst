.. PythonVideoAnnotator documentation master file, created by
   sphinx-quickstart on Thu Jan 12 14:10:03 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
	:hidden:
	:maxdepth: 2
	:includehidden:
	:caption: Getting Started
   
	Introduction <self>
	user-docs/install_and_run/index
	user-docs/update/index

.. toctree::
	:hidden:
	:maxdepth: 2
	:includehidden:
	:caption: User guide

	user-docs/howto/index
	user-docs/timeline/index
	user-docs/shortcuts/index

.. toctree::
	:hidden:
	:maxdepth: 2
	:includehidden:
	:caption: Modules \ Plugins

    modules/idtrackerai
	modules/label-deeplabcut
	modules/path-map
	modules/tracking
	modules/regionsfilter	
	modules/extract-images
	modules/calc-background
	modules/smooth
	modules/distances
	modules/motion
	modules/estimate-contour-orientation
	modules/export-videos
	modules/export-data
	
.. toctree::
	:hidden:
	:maxdepth: 2
	:includehidden:
	:caption: Concepts

	concepts/project-tree/index
	concepts/project-tree/datasets
	concepts/project-tree/project-files

|
|

Python Video Annotator's Documentation
=====================================================

|

.. raw:: html

	<center>
	<iframe width="100%" height="315" src="https://www.youtube.com/embed/lQEy8kc-3w0?theme=light&modestbranding=1&autohide=1&showinfo=0&controls=1&rel=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
	</center>

|
|

What is the Python Video Annotator?
------------------------------------

| 
| The **PythonVideoAnnotator** is a graphical application written in python, to analyse videos and create notes for events in the video. It was developed with the aim of helping neuroscience and ethology researchers indentify animals' behaviours based on the information extracted from the video.
| 
| Paths, contours and outputs of external devices, like accelerometers, sound recorders, pokes, pressure devices and other sensors can be combined to find classes of events to identify behaviours.
|

|

.. image:: _static/index/project.png
	:align: left

|
|
| Organize your data and work on multiple videos at the same time with the project tree.
|
| Import the output of your scripts, third party applications or external devices, into your project and follow its changes over the time.
|
| On each video you may have associated objects that you can track and compare their properties.
|
|
| Navigate in the video, annotate and modify events with the timeline bar.
|
| Plot the data on the timeline to compare values over the time.
|

.. image:: _static/index/timeline_small.png
    

|

.. image:: _static/index/project-directories-tree.png
	:align: left

|
| Access and modify the data easily with the open formats.
| 
| The project data is organized in an intuitive structure, and files are saved with open formats like json and csv to garantee the portability of the data.
|
| Modify the project structure by moving the folders around with your filesystem manager.
|
|
| The python video annotator is plugins based which allow to toggle the activation of the ones that are already included or add new ones developed by you.
|
| Validate automatically tracking mistakes and correct them using the tracking modules or the manual correction.
|

.. image:: _static/index/background-calculator.gif

.. image:: _static/index/player.png
	:class: paddingleft18

|
| Visualize the tracking information directly on the video player, smooth paths, calculate the videos' backgrounds and much more ...
|


Funding
-------------------

.. image:: _static/index/funding.png

Thank you!!

|

Developers
-------------------

=================================   ============================================================================================================================================
Ricardo Ribeiro                     from the `Champalimaud Scientific Software Platform <http://neuro.fchampalimaud.org/en/research/platforms/staff/Scientific%20Software/>`_
									ricardo.ribeiro@research.fchampalimaud.org
Carlos Mão de Ferro                 from the `Champalimaud Scientific Software Platform <http://neuro.fchampalimaud.org/en/research/platforms/staff/Scientific%20Software/>`_
									carlos.maodeferro@research.fchampalimaud.org
Hugo Cachitas                       from the `Innate Behavior Lab <http://neuro.fchampalimaud.org/en/research/investigators/research-groups/group/Vasconcelos/>`_
									hugo.cachitas@research.fchampalimaud.org

Manuel Manso                        from the `Champalimaud Scientific Software Platform <http://neuro.fchampalimaud.org/en/research/platforms/staff/Scientific%20Software/>`_
									manel.manso@research.fchampalimaud.org
=================================   ============================================================================================================================================

|
|