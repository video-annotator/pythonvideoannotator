.. _howto-label:

************
How to
************

|

---------------
Project
---------------

By default the application opens with an empty project so you can start adding videos immediately.




Open a project
===============

To open a existing project select the option "Open" in the "File" menu of the main window.
A new window will appear asking for the project folder. You should select the folder and press open.

.. seealso:: Find information about the project folders structure in the :ref:`Project tree <projecttree-label>` section.

Save a project
===============

It is possible to save a project by using the options "Save" or "Save as" in the "File" menu of the main window.

Save
-------------

Update the current project files with the last changes.

.. note:: if you are saving the project for the first time, this option will behaves like the "Save as" option.

Save as
-------------

Save or export the current project into a folder.

.. note:: the user should choose an empty directory to avoid mixing the project files with pre existing files and directories.


Add a video
===============

.. image:: /_static/howto/add-video.png
|

Result

.. image:: /_static/howto/add-video-result.png



|
|
|
|


---------------
Video
---------------


Add & edit a geometry
==============================

A geometry is used to define a region or a static object in the video.


.. image:: /_static/howto/add-geometry.png

.. image:: /_static/howto/add-geometry-edit.png

Drawing geometries
------------------------

To draw geometries, you should first select the type of geometries you would like to draw (Square or Cicle). After drag the mouse over the video to draw the polygon.

The polygon **points can be moved**, by dragging and dropping the a selected point, or **deleted** by pressing the delete key on the keyboard.

.. image:: /_static/howto/add-geometry-edit-poly.png


Capture a frame
===============

The next step can be used to capture the current frame into an image.

.. image:: /_static/howto/add-capture.png
|

Result

.. image:: /_static/howto/add-capture-result.png


Add an object
===============

An object is something in the video which its properties change overtime.

.. image:: /_static/howto/add-object.png

Add a dataset
------------------------

Datasets are abjects properties that change overtime. There are 3 types of properties that you can add, Paths, Countours or Values.

.. seealso:: Find more information about the datasets in the :ref:`Objects’ datasets <datasets-label>` section.

To add a dataset right click over the object and select one of the available options.

.. image:: /_static/howto/add-datasets.png

Path
`````````````
A path dataset stores information about an object path.

Contours
`````````````
A contours dataset stores information about the object contours overtime, but it has also information about the object path.

Value
`````````````
This property stores any arbitrary number that change overtime. It can be used to store external data like for example hardware triggers.