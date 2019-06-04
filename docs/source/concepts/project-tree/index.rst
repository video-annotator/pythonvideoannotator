.. _projecttree-label:


Project's tree
================================================

|

| A project may have multiple videos and each video may contain several 2D objects associated to it.
| 
| The data is organized this way so the user will not get confused when analysing and comparing the outputs of multiple videos.
|
| The structure has a hierarchy and is composed by Models (or Entities) (ex: a project is a model, a video is a model, and so on ...).

|

---------------
Hierarchy
---------------

.. image:: /_static/index/project.png
	:align: right

A project is organized in the following hierarchy:

- Project
	- Video
		- Image
		- Geometry
		- Object
			- Path
			- Contours
			- Value

|

------------------------------
Models definition
------------------------------

|

+----------+------------------------------------------------------------------------------------------+
| Model    | Description                                                                              |
+==========+==========================================================================================+
| Project  | A project contains videos, and is the entity responsible for aggregating all the data in |
|          | the application, including the graphs and annotations that are in the timeline.          |
+----------+------------------------------------------------------------------------------------------+
| Video    | A video may have several objects or images associated to it.                             |
+----------+------------------------------------------------------------------------------------------+
| Geometry | A geometry stores one or multiple polygons which define areas in the video.              |
+----------+------------------------------------------------------------------------------------------+
| Image    | An image is just an entity to associate images to a video. For example if you use the    |
|          | module "Calculate the video background", you will create a background image under the    |
|          | corresponding video.                                                                     |
+----------+------------------------------------------------------------------------------------------+
| Object   | An object is a 2D artifact present in the video. It can be used to annotate paths,       |
|          | motions or contours.                                                                     |
+----------+------------------------------------------------------------------------------------------+
| Path     | Entity representing the path of an object.                                               |
+----------+------------------------------------------------------------------------------------------+
| Contour  | Entity representing the contour of an object overtime. A contour contains a path also,   |
|          | but the diference between the Contour entity and the Path entity is that a contour path  |
|          | can't be smooth.                                                                         |
+----------+------------------------------------------------------------------------------------------+
| Value    | A value is an entity that associates a generic value to an object. For example, you can  |
|          | create a value from a contour's area and smoothen this value to remove jittering.        |
+----------+------------------------------------------------------------------------------------------+
