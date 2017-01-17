|

PROJECT's TREE
===============

|

| A project may have multiple videos, and each video may contain several 2D objects associate to it. 
| This organization of the data was created so that the user will not get confused when analysing and comparing multiple videos outputs.
| The structure has an hierarchy and is composed by what I call Models or Entities (ex: a project is a model, a video is a model, and so on ...).

.. image:: /_static/index/project.png
	:align: left
	:class: left-image

|

Hierarchy
___________

.. container:: left-text

	A project is organized in the next hierarchy:

	- Project
		- Video
			- Image
			- Object
				- Path
				- Contour
				- Value
		

.. container:: clear-line
	
	.

|

Entities definition
_______________________

|

+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Model    | Description                                                                                                                                                                                      |
+==========+==================================================================================================================================================================================================+
| Project  | A project contains videos, and is the entity responsible to agregate all the data in the application, including the graphs and annotations that are in the timeline.                             |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Video    | A video may can contains serveral objects on it or images.                                                                                                                                       |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Image    | The image is just an entity to associate images to a video. For example if you use the module "Calculate the video background" you will create a background image under the corresponding video. |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Object   | An object is a 2D artefact present in the video. I can be used to annotate paths, motions or contours.                                                                                           |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Path     | Entity representing the path of an object.                                                                                                                                                       |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Contours | Entity representing the contours of an object overtime. A contour contains a path also, but the diference between the Contour entity and the Path entity is that a contour path can't be smooth. |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Value    | A value is entity that associates a generic value to an object. For example, you can create a value from a contour area and smooth this value to remove jittering.                               |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


|

Path and Contours properties
_____________________________________________________

|

`Datasets description. <datasets.html>`_

|

Project files
____________________


.. image:: /_static/user-docs/project-tree/project-files-tree.png
	:align: left
	:class: left-image

|
| The structured of the project files is similar to the project tree. The user can move the files around a define a new project organization

|
|
