.. regionsfilter-label:

Filter by regions
===============================

This module calculates the distance between an object and a geometry's closest border. 

------------------------
How to use
------------------------


| 1. Create a geometry, :ref:`here's how <addgeometry-label>`.
|
| 2. Open the **"Modules"** tab and choose the **"Filter by regions"** module.
|
| 3. On the top part select the video, then the object and finally the object's **path or contour** to determine the object used in the distance calculation. On the bottom part select the geometry you want to calculate the distance to.
| 
| 4. Use the **blue slider or the left and right textboxes** to **set a start and an end frame** for the calculation. The distance will only be calculated for the interval you choose.

.. note :: 

	To change the start and end frame you also have to click on the name of the video, **not just the checkbox**

| 5. Click the **"Apply"** button.
|

------------------------
Result
------------------------

| After running the module, a value with the name **"regions-filter"** will appear under the object to which the path or contour belongs to.
| If we plot this value into the timeline we can see the variation of the object's distance to the border of the selected geometry.

| For the value of the calculated distance we have that:
|
|	- When the distance is **lower than 0** it means the object is **outside the geometry**.
|
|	- When the distance is **0** it means the position of the object is **over the geometry border**.
|
|	- When the distance is **higher than 0** it means the object is **inside the geometry**.
|

------------------------
Example
------------------------

.. image:: /_static/modules/filter-by-regions.gif
