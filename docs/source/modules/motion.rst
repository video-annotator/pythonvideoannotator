
Motion
===============================

| This module calculates the motion of an object, which means,the number of pixels that change from frame to frame for a path or contours.

------------------------
How to use
------------------------


| 1. Open the **"Modules"** tab and choose the **"Motion"** module.
| 
| 2. On the top part select the video, the object and finally the object's **path or contour** to determine the object you will calculate the motion for.

.. note:: You can preview the motion calculation by clicking on the name of thevideo you selected and then clicking on the *'Play'* button under the video player

| 3. Use the blue slider or the left and right textboxes to **select a start and an end frame** for the calculation. The motion will then only be calculated for the specified interval.

.. note :: 

	To change the start and end frame you also have to click on the name of the video, **not just the checkbox**

| 4. Use the **"Compare with"** selection box to choose how the motion is calculated:
|		- **First frame** -> compares the current frame with the first frame
|		- **Previous frame** -> compares the current frame with the previous frame (current frame - 1)
| 		- **Background image** -> compares the current frame with a background image
|
| To create a Background image you can either :ref:`capture a frame <captureframe-label>` or use the :ref:`"Calculate the video background" <backgroundfinder-label>` module.
|
| 6. Use the **"Threshold"** slider to set the treshold for the motion
|
| 7. Use the **"Radius"** slider to select the radius the motion calculation
|
| 8. Check the **"Show diffs boxes"** if you want the preview to show the pixels that changed in the current frame
|
| 9. Press the **"Apply"** button to calculate the motion.
| 

------------------------
Result
------------------------

| The calculated motion will be added to the contours or path dataset as a new value called **"motion"**.
|

------------------------
Example
------------------------

.. image:: /_static/modules/motion.gif