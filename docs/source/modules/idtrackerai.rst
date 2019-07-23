idtracker.ai
============

This plugin adds functions to correct the trajetories from idtracker.ai sessions.
You can visit the project @ `idtracker.ai <https://www.idtracker.ai/>`_

Load an idtracker.ai tracking session
_____________________________________

If you finished tracking a video using the GUI from `idtracker.ai <https://www.idtracker.ai/>`_, you can press the **Validate trajectories** button on the bottom left corner to open the validation GUI. The current tracking session will be automatically loaded into the video annotator.

To load an idtracker.ai session from scratch, run the video annotator (see :doc:`../_static/install_and_run/index`), press the button **Open** and open the session folder you want to load. This will automatically read the necessary files from the session folder and create an "Idtrackerai object".

Correct the tracking
____________________

To visualize the trajectories and start validating them, make sure that an "Idtrackerai object" is selected (highligthed in blue in the "Video list" panel).

.. image:: /_static/modules/idtrackerai_1_select_obj.png

Select a centroid
____________________

Click over a centroid of a blob.

.. image:: /_static/modules/idtrackerai_2_select_centroid.png

Keys events
____________

==========================================================================  =================================
EVENT                                                                       SHORT KEYS
==========================================================================  =================================
Go to the next crossing.                                                     Ctrl+M
Go to the previous crossing.                                                 Ctrl+N
==========================================================================  =================================
