idtracker.ai validator
======================

This plugin has been developed with the Polavieja Lab at the Champalimaud Foundation
and it is part of `idtracker.ai <https://www.idtracker.ai/>`_ project. If you are using
idtracker.ai to track your videos or this plugin to correct trajectories, please cite:

  `Romero-Ferrero, F., Bergomi, M.G., Hinz, R.C., Heras, F.J.H., de Polavieja, G.G., Nature Methods, 2019.
  idtracker.ai: tracking all individuals in small or large collectives of unmarked animals <https://drive.google.com/open?id=1fYBcmH6PPlwy0AQcr4D0iS2Qd-r7xU9n>`_

.. code-block:: bibtex

  @article{romero2019idtracker,
  title={idtracker.ai: tracking all individuals in small or large collectives of unmarked animals},
  author={Romero-Ferrero, Francisco and Bergomi, Mattia G and Hinz, Robert C and Heras, Francisco JH and de Polavieja, Gonzalo G},
  journal={Nature methods},
  volume={16},
  number={2},
  pages={179},
  year={2019},
  publisher={Nature Publishing Group}
  }

-------------------------------------
A plugin to correct idtracker.ai trajectories
-------------------------------------

Under good `video condtions <https://idtracker.ai/video_conditions.html>` idtracker.ai typically gives very high accuracte trajectories. However, due to not so good video conditions some animals might be badly identified for in some parts of the video. Also, the interpolation algorithm might place the centroid of the animal in a place different to the center of mass of the animal (during crossings).

This plugin allows to correct wrongly identified animals in the video and also
to modify the position of the centroids so that they are closer to the center of
mass of the the represent.

In the following sections we explain how to load a tracking session into the
video annotator, how to correct trajectories, and how to save the results to
get new and updated trajectories files.

--------------------------------------
Load an idtracker.ai tracking session
--------------------------------------

If you finished tracking a video using the GUI from `idtracker.ai <https://www.idtracker.ai/>`_, you can press the **Validate trajectories** button on the bottom left corner to open the validation GUI. The current tracking session will be automatically loaded into the video annotator. Note that depending on the length of the video and the number of animals the process of loading the data can take some time.

To load an idtracker.ai session from scratch you have two options. Both require
to open a terminal and run a command inside of the virtual environment where you
installed idtracker.ai.

1. Run the command

.. code-block::

    idtrackerai

Click the button "Open" and select the video for which you want to validate the trajectories. In the text box "Session", add the name of the session that you want to open. Remember that if the session folder is "session_test", the name of the tracking session will be "test". If the name is correct the button "Validate trajectories" in the bottom right corner will activate. Click that button and the validation GUI will open.

2. Run the video annotator (see :doc:`../_static/install_and_run/index`), press the button **Open** and open the session folder you want to load. This will automatically read the necessary files from the session folder and create an "Idtrackerai object".

Once the validator GUI is open, you can add as many videos and tracking sessions as you want as far as they fit in your memory

***********************
Add a tracking session to a video
***********************

In the "Videos list" right panel, right click on the name of the video and click the button add idtracker.ai object. Select the tracking session that you want to add and press "Open".

********************
Add a video
********************

In the "Videos list" right panel, click the button "Add video". Then select a video (not a tracking session folder) that you want to add and open it. Afterwards, you can add a tracking session following the steps above.

--------------------
Validate the trajectories
--------------------

To visualize the trajectories and start validating them, make sure that an "Idtrackerai object" is selected (highligthed in blue in the "Video list" panel).

.. image:: /_static/modules/idtrackerai_1_select_obj.png

*********************************
Change the identity of a centroid
*********************************

To change the identity of a centroid, double click on top of a centroid. A window "New identity" will pop up. You can type the new identity and press "Ok". The identity will be propagated to the previous and next frames until the next crossing or until the animal disappears.


*********************************
Move a centroid to a different position
*********************************



*********************************
Add a new centroid to a blob
*********************************


*********************************
Delete a centroid from a blob
*********************************


*********************************
Clear all user updates
*********************************


*********************************
Clear user updates for a given identity
*********************************


*********************************
Local interpolation
*********************************


*********************************
Global interpolation
*********************************



--------------------
Save the results
--------------------


-----------
Keys events
-----------

==========================================================================  =================================
EVENT                                                                       SHORT KEYS
==========================================================================  =================================
Go to the next crossing.                                                     Ctrl+M
Go to the previous crossing.                                                 Ctrl+N
==========================================================================  =================================
