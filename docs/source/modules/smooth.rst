.. smoothpaths-label:

Smooth
===============================

This module smoothens the data of a value or path using the Savitzky–Golay filter.

------------------------
How to use
------------------------

| 1. Open the **"Modules"** tab and choose the **"Smooth"** module.
| 
| 2. If you want to smoothen the data of a value, first you have to create a value. See how you can create a value :ref:`here <add_dataset-label>`.
|
| 3. **Check** the corresponding checkboxes to select the **video**, the **object** and the **path or value** for which you want to smoothen the data.
|
| 4. Use the **blue slider or the left and right textboxes** to **set a start and an end frame** for the calculation. The data will only be smoothed for the interval you choose.

.. note :: 

	To change the start and end frame you also have to click on the name of the video, **not just the checkbox**

| 5. Use the **"Window size"** slider to set the Windows size parameter for the Savitzky–Golay filter.
|
| 6. Use the **"Order"** slider to set the Order parameter for the Savitzky–Golay filter.
|
| 7. Use the **"Derivative"** slider to set the Derivative parameter for the Savitzky–Golay filter.
|
| 8. Use the **"Rate"** slider to set the Rate parameter for the Savitzky–Golay filter.

.. note :: 

	To obtain good results, the Window size parameter should be significantly bigger than the Order. You can read more about the Savitky-Golay filter `here <https://scipy-cookbook.readthedocs.io/items/SavitzkyGolay.html>`_.

| 9. Press the **"Apply"** button and you're done.
|

------------------------
Result
------------------------

| The value or the path used in the module will have its data automatically smoothed after running the module. To see the results you can :ref:`display the value/path on the timeline <show_dataset_timeline-label>`.
|

------------------------
Example
------------------------

.. image:: /_static/modules/smooth.gif
