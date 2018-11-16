
Export data
===============================

This module allow the user to export data to custom csv files.

| To use the module, first open the **"Modules"** tab and choose the **"Export Data"** module. Then, for every value you want to export, navigate through the project tree, select that value and click the **"Add"** button on the top left.
| In the resulting csv file, a column will be generated for each value you add.
| To remove a value, simply select it on the right side and click the **"Remove"** button on the top.
| 

| If the **"Split files by events"** checkbox is selected, then the values will only be exported for the frames during those events.
| If no events are selected, the values during the whole video will be exported.
| If one or more events are selected, only the values during those events will be exported.
| The output file will also be split in multiple files, where each file will correspond to one of the selected events.
|

.. note:: The first column of the csv file will always be the index of the frame the other columns correspond to

.. image:: /_static/modules/exportdata-module.png

