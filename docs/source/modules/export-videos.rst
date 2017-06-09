|

Export videos
=======================================

This module allow the user to generate new videos with the annotations drawn directly in the image.

.. image:: /_static/modules/exportvideos-module.png


------------------------
Tabs
------------------------

PATH
--------------------------------------

In the tab PATH the user should select the video and path which the module should based on to generate a new video.
If the "Draw paths" checkbox is checked the path history of the object will be drawn in the video.

CIRCLE
--------------------------------------

If any dataset is selected or the checkbox "Use a fixed size" is selected, a circle will be drawn in the position of object for the correspondent frame.
In case you select the dataset and the checkbox "Use a fixed size" is unselected the area of the circle will be based on the are of the dataset for each frame (the dataset has to be of contours type) .

- The user can export paths, posititions, and events.
- It can also use a fixed image as background.

CIRCLE COLOR
--------------------------------------

If any dataset is selected the drawn circle will use the color of this dataset for each frame.
If the checkbox "Use a fixed color" is selected, then the drawn circle will assume the configured color.

BACKGROUND
--------------------------------------

If any image is selected the video will be generated with the image in background instead of the frames of the video.

DRAW EVENTS
--------------------------------------

Select the events to be drawn in the exported video.
If the "Draw titles" checkbox is select, the titles of the events will be also drawn.

SPIT FILES BY EVENTS
--------------------------------------

With this tab the user can export only the moments where the selected events occur.

------------------------
Results
------------------------

Screenshot of a video generated with this module.

.. image:: /_static/modules/exportvideos-module-result.png 