.. regionsfilter-label:

****************************
Filter by regions
****************************

This module calculates the distance between a Path or Contours and a geometry closest border.
- When the distance is lower than 0 it means the object is outside the geometry.
- When the distance is 0 it means the position of the object is over the geometry border.
- When the distance is higher than 0 it means the object is inside the geometry.

.. figure:: /_static/modules/regionsfilter-module.png
	:scale: 100%

------------------------
Results
------------------------

After running the module, a value with the name "regions-filter" will appear under the object to which the path or contour belongs to.
If we plot this value into the timeline we can see the variation of the rat distance to the border of the selected geometry.

.. figure:: /_static/modules/regionsfilter-module-result.png
	:scale: 100%
