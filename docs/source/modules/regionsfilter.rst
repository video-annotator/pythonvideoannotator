.. regionsfilter-label:

****************************
Filter by regions
****************************

This module calculates the distance between an object and a geometry's closest border. 


To use the module, first you have to create a geometry, :ref:`here's how <addgeometry-label>`.
Then, open the **"Modules"** tab and choose the **"Filter by regions"** module.
On the top part you have to first select the video, then the object and finally the object's **path or contour**. On the bottom part you select the geometry you want to calculate the distance to. Then click **"Apply"**.


.. figure:: /_static/modules/regionsfilter-module.png
	:scale: 100%

|

**Result:**

After running the module, a value with the name **"regions-filter"** will appear under the object to which the path or contour belongs to.
If we plot this value into the timeline we can see the variation of the rat distance to the border of the selected geometry.

.. figure:: /_static/modules/regionsfilter-module-result.png
	:scale: 100%

| For the value of the distance we have that:
|
| - When the distance is **lower than 0** it means the object is **outside the geometry**.
|
| - When the distance is **0** it means the position of the object is **over the geometry border**.
|
| - When the distance is **higher than 0** it means the object is **inside the geometry**.
|