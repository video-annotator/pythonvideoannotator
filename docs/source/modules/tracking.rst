.. trackingmodule-label:

******************
Track objects
******************

This module allows the use of simple tracking algorithms to track objects in a video.

.. image:: /_static/modules/tracking-module.png


How to use
==================================

To use the module the user has to go over 4 steps:

| :ref:`1. <choosethedatasets-label>` Choose the :ref:`datasets <datasets-label>`.
| :ref:`2. <configureimagefilters-label>` Configure the image filters.
| :ref:`3. <configureblobsfilters-label>` Configure the filters that should be applied to blobs resulted from the image filter.
| :ref:`4. <applyandprocess-label>` Press the apply button.


|

.. _choosethedatasets-label:

1. Choose the datasets
________________________________


.. note:: You can preview the motion calculation by clicking on the name of thevideo you selected and then clicking on the *'Play'* button under the video player

1. Add an **object** to the video, :ref:`here's how <add_objects-label>`.

2. Add a **path or contour** to the created objects, :ref:`here's how <add_dataset-label>`.

3. Open the **"Modules"** tab and choose the **"Track objects"** module.

Now you need to define in which datasets the results should be saved. You should choose one dataset for each object you want to track, so if you have one object, you should choose one single dataset, if you have 2 objects to track you should choose 2 datasets.

.. image:: /_static/modules/tracking-module-datasets.png

4. On the top part select the video, the object and finally the object's **path or contour** to determine the object you will track.

.. note:: 
	* If the dataset is a path only the position's over time will be stored. If it is a contour you will save all the objects information over time.
	* The analysis of multiple videos in one single execution is not working yet, please choose datasets of one single video.
	* You can hide the datasets field by pressing the top button "Hide datasets list".
	* To preview the video in the player, right click the name of the video and click **"Select video"**

5. Use the **blue slider or the left and right textboxes** to **set a start and an end frame** for the tracking. The tracking algorithm will only run for the interval you choose and the object's values will only be stored for this interval.

|

.. _configureimagefilters-label:

2. Configure the image filters
________________________________


On this step the user configures the image filters that are going to be used to split the objects from the background image.

1. From the **"Image workflows"** dropdown list, choose the one you wish to use. You can read each workflows' description in the following table.

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
| Background subtract + mask + path mask  | It's a combination of the 2 previous filters.             |
+-----------------------------------------+-----------------------------------------------------------+
| Adaptative threshold                    | Applies an adaptative threshold to the image              |
+-----------------------------------------+-----------------------------------------------------------+
| Adaptative threshold + mask             | After the threshold, a image mask defining a ROI is       |
|                                         | applied to the image.                                     |
+-----------------------------------------+-----------------------------------------------------------+
| Adaptative threshold + path mask        | After the threshold, a circular mask around the current   |
|                                         | position of a path is applied to the image. Usually this  |
|                                         | filter is used to improve detail of contours found in     |
|                                         | previous analysis.                                        |
+-----------------------------------------+-----------------------------------------------------------+
| Adaptative threshold + mask + path mask | It's a combination of the 2 previous filters.             |
+-----------------------------------------+-----------------------------------------------------------+

.. note:: 
	
	For the **Background subtract** workflows you need to have an image in the project to use as background. You can :ref:`add one manually <captureframe-label>`, or use the module :ref:`Calculate the background image <backgroundfinder-label>` to create one.

.. note:: 
	
	For the **mask** workflows you need to have a geometry in the project to use as a mask. :ref:`Here's how to add a geometry to the project <addgeometry-label>`.

After selecting the workflow, the list of options available bellow will change. The options are parameters of the filters.The user can adjust these parameters and preview the result on the right side of the player as it is shown in image (white blob).


.. image:: /_static/modules/tracking-module-imagefilters.png

|

.. _configureblobsfilters-label:

3. Configure the blobs filters
________________________________


On this step the user configures the filters that are applied after step 2 workflow.


1. Click the **"Blobs filter"** button, on the left bottom part of the window
2. Choose as many blobs as the number of datasets you selected. 

.. image:: /_static/modules/tracking-module-blobsfilters.png


Schematic of the workflow of filters:

.. image:: /_static/modules/tracking-module-blobsfilter-workflow.png
	:scale: 40% 

|

.. _applyandprocess-label:

4. Apply and process
________________________________

After you have configured all the workflows and you are happy with the preview, simply click the **"Apply"** button on the bottom of the window. The processing might take a while to finish.

| 

Result
==================================

The results of the module will be the stored information in the datasets. In case you chose a path as the object's dataset, the path's properties such as position and velocity will now have information. If you chose a contour as the object's dataset, the contour's properties such as position, velocity, area and extreme points will now have information.

You will also be able to see the outline of an object's contour if select the name of the video and play the video in the main window video player.

|

Example
==================================

.. image:: /_static/modules/tracking-objects.gif