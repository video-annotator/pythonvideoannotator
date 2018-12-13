
Export data
===============================

This module allow the user to export data to custom csv files.

------------------------
How to use
------------------------

| 1. Open the **"Modules"** tab and choose the **"Export Data"** module.
| 
| 2. For every value you want to export, navigate through the project tree, select that value and click the **"Add"** button on the top left. In the resulting csv file, a column will be generated for each value you add. To remove a value, simply select it on the right side and click the **"Remove"** button on the top.
| 
| 3. If the **"Split files by events"** checkbox is selected, then the values will only be exported for the frames during those events.
| If no events are selected, the values during the whole video will be exported. If one or more events are selected, only the values during those events will be exported.
| The output file will also be split in multiple files, where each file will correspond to one of the selected events.
|
| 4. Choose the directory you want to save the csv file in by clicking the **"Open"** button on the bottom right side and then write the name you want the file to have in the **"Output file name"** textbox.
|
| 5. Click the **"Apply"** button to export the data to the output file.

.. note:: The first column of the csv file will always be the index of the frame the other columns correspond to

|

------------------------
Result
------------------------

The module will create a csv file in the chosen directory.

|

------------------------
Example
------------------------

.. image:: /_static/modules/exportdata-module.png

