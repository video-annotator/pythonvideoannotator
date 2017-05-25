.. trackingmodule-label:

************************
Track objects
************************

This module allows the use of simple tracking algorithms to track objects in a video.

.. image:: /_static/modules/tracking-module.png

To use the module the user has to go over 4 steps:

1. Choose the :ref:`datasets <datasets-label>`.
2. Configure the image filters.
3. Configure the filters that should be applied to blobs resulted from the image filter.
4. Press the apply button.


------------------------
1. Choose the datasets
------------------------

You should first define in which datasets the results should be saved.
You should choose one dataset for each object you want to track, so if you have one object, you should choose one single dataset, if you have 2 objects to track you should choose 2 datasets.

.. image:: /_static/modules/tracking-module-datasets.png

a. First check the video you wish to analyse.
b. After check the objects you want to search for.
c. Check the datasets you want to use to store the result.

.. note:: 
	* If you check a path dataset, only the positions overtime will be stored. If you check the contours you will save all the blobs information overtime.
	* The analysis of multiple videos in one single execution is not working yet, please choose datasets of one single video.
	* You can hide the datasets field by pressing the top button "Hide datasets list".
	* To pre-visualize the video in player, you can right click in the video and select the option "Select video".

Restrict the analysis to a period
--------------------------------------

The blue bar at the bottom of datasets field, allow you you to choose the period of time you want to analyse.

------------------------------
2. Configure the image filters
------------------------------

On this step the user configures the image filters that are going to be used to split the objects from the background image.

1. The user should start by choosing the workflow of filters that wish to use.

The current filters are:

+-----------------------------------------+-----------------------------------------------------------+
| Available filters                       | Description                                               |
+=========================================+===========================================================+
| Background subtract                     | An image is subtracted to the current frame.              |
+-----------------------------------------+-----------------------------------------------------------+
| Background subtract + mask              | After the subtraction, a image mask defining a ROI is     |
|                                         | applied to the image.                                     |
+-----------------------------------------+-----------------------------------------------------------+
| Background subtract + path mask         | After the subtraction, a circular mask around the current |
|                                         | position of a path is applied to the image. Usually this  |
|                                         | filter is used to improve detail of contours found in     |
|                                         | previous analysis.                                        |
+-----------------------------------------+-----------------------------------------------------------+
| Background subtract + mask + path mask  | It is a combination of the previous 2 filters.            |
+-----------------------------------------+-----------------------------------------------------------+
| Adaptative threshold                    | Applies a adaptative threshold to the image               |
+-----------------------------------------+-----------------------------------------------------------+
| Adaptative threshold + mask             | After the threshold, a image mask defining a ROI is       |
|                                         | applied to the image.                                     |
+-----------------------------------------+-----------------------------------------------------------+
| Adaptative threshold + path mask        | After the threshold, a circular mask around the current   |
|                                         | position of a path is applied to the image. Usually this  |
|                                         | filter is used to improve detail of contours found in     |
|                                         | previous analysis.                                        |
+-----------------------------------------+-----------------------------------------------------------+
| Adaptative threshold + mask + path mask | It is a combination of the previous 2 filters.            |
+-----------------------------------------+-----------------------------------------------------------+

.. note:: 
	
	For the **Background subtract** workflows you need to have an image in the project to use as background. You can add one manually or use the module :ref:`Calculate the background image <backgroundfinder-label>` to create one.

After selecting the workflow, the list of options available bellow will change. The options are parameters of the fitlers.
The user can adjust these parameters and previsualise its result on the right side of the player as it is shown in image (white blob).


.. image:: /_static/modules/tracking-module-imagefilters.png


------------------------------
3. Configure the blobs filters
------------------------------

On this step the user configures the filters that are applied after step 2 workflow.

As it is shown in the image the user, can filter blobs by their size, and define how many blobs he wish to track. 

.. note:: 
	The number of blobs to track should be the same of datasets selected in the first step.

.. image:: /_static/modules/tracking-module-blobsfilters.png


Schematic of the workflow of filters:

.. image:: /_static/modules/tracking-module-blobsfilter-workflow.png
	:scale: 40% 


------------------------------
4. Apply and process
------------------------------

After you configure all the workflows just press the Apply button, wait for the processing to finish, and check the results on the main window.


.. image:: /_static/modules/tracking-module-result.png