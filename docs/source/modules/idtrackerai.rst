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

1. Open idtracker.ai by running the command:

.. code-block:: bash

  idtrackerai

In the GUI, click the button "Open" and select the video for which you want to validate the trajectories. In the text box "Session", add the name of the session that you want to open. Remember that if the session folder is "session_test", the name of the tracking session will be "test". If the name is correct the button "Validate trajectories" in the bottom right corner will activate. Click that button and the validation GUI will open.

2. Run the video annotator (see :doc:`../_static/install_and_run/index`), press the button **Open** and open the session folder you want to load. This will automatically read the necessary files from the session folder and create an "Idtrackerai object".

Once the validator GUI is open, you can add as many videos and tracking sessions as you want as far as they fit in your memory

********************
Add a video
********************

In the "Videos list" right panel, click the button "Add video". Then select a video (not a tracking session folder) that you want to add and open it. Afterwards, you can add a tracking session following the steps above.


***********************
Add a tracking session to a video
***********************

In the "Videos list" right panel, right click on the name of the video and click the button add idtracker.ai object. Select the tracking session that you want to add and press "Open".

--------------------
Validate the trajectories
--------------------

To visualize the trajectories and start validating them, make sure that an "Idtrackerai object" is selected (highligthed in blue in the "Video list" panel).

.. image:: /_static/modules/idtrackerai_1_select_obj.png

In the video preview, the centroids of animals that belong to a blob classified by the algorithm as a single animal, will show a number. The centroids of animals that belong to a blob classified by the algorithm as a crossing, will show a number with the prefix 'c-'. The centroids of any animal for which the user modified its identity or the position of the centroid, will show a number with the prefix 'u-'.

*********************************
Change the identity of a centroid
*********************************

To change the identity of a centroid, double click on top of a centroid. A window "New identity" will pop up. You can type the new identity and press "Ok". The identity will be propagated to the previous and next frames until the next crossing or until the animal disappears.


*********************************
Move a centroid to a different position
*********************************

To move a centroid to a different position, click on it, drag it and drop it wherever you want its new position to be.

*********************************
Add a new centroid to a blob
*********************************

To add a new centroid to an existing blob. Click on a centroid of the giving blob. In the "Details" panel on the right, check the box "Add centroid". Then click again on the blob. This will open a windows in which you will need to introduce the identity of the centroid to be added.

*********************************
Delete a centroid from a blob
*********************************

To delete a centroid, click on it and press the button "Delete centroid" in the "Details" panel on the righ.

Only centroids of duplicated identities and centroids of blobs with multiple centroids can be deleted. To delete a centroid of a unique identity first create a new centroid for that identity.


*********************************
Clear all user updates
*********************************

If you want to recover the original identities assigned by the algorithm for a particular part of the video, click on the button "Clear user updates for all identities" in the "Details" panel on the right. This will show a window where you can indicate the starting and ending point to define the interval where the identities will be reseted.


*********************************
Clear user updates for a given identity
*********************************

To clear the user updates for a given identity select a centroid of the identity X you want to reset. Then, on the "Details" panel on the right, click the button "Clear user updates for X". This will show a window where you can indicate the starting and ending point to define the interval where the identities will be reseted.


*********************************
Local interpolation
*********************************

In some situations, you might want to modify the position of the centroid for a given identity for multiple frames in a row. This can be very time consuming. To facilitate the work, we implemented a "Local interpolation for X" button. This will interpolate the positions for a given identity between two user generated centroids. Note that this runs a linear interpolation, so we recommend to add user generated centroids where the animal changes orientation.

To interpolate the positions for a given identity follow these steps.

1.- Modify the centroid of a given identity for a set of frames. You do not need to modify it for all the frame, just when the animals is changing orientation.
2.- Make sure that the identity is unique for the interval where you want to interpolate the centroids.
3.- Click the button "Local interpolation for X".
4.- Add the initial and ending frames of the interval where you want the interplation to run. Note that the first and last frame must include a user generated centroid (i.e. a centroid with the prefix 'u-')


*********************************
Global interpolation
*********************************

Click the button "Global interpolation" to run the idtracker.ai interpolation algorithm that assigns the centroids to the blobs that correspond to multiple animals. This is particularly useful when you are only modifying identities before and after crosings. The algorithm might work if you have also modified the positions the centroids in the blobs corresponding to crossings. However, we haven't test it deeply, so we recommend to only used if you only modified identities and not centroids.

--------------------
Save the results
--------------------

To save the results of your validation, press the button "Save" on the top of the window. Select the tracking session folder where you want to store the results and click "Open". This will update the "blobs_collection_no_gaps.npy" file in the "preprocessing" folder insider of the session folder. Also it will generate two new "trajectories_TIMESTAMP.npy" and "trajectories_wo_gaps_TIMESTAMP.npy" files in the folders "trajectories" and "trajectories_wo_gaps" respectively.


-----------
Keys events
-----------

A part form the :doc:`../user-docs/shortcuts/index` of the video annotator, we added two new shortcuts to automatically advance to the next and previous crossings (or frames where an animal is missing). 

==========================================================================  =================================
EVENT                                                                       SHORT KEYS
==========================================================================  =================================
Go to the next crossing.                                                     Ctrl+M
Go to the previous crossing.                                                 Ctrl+N
==========================================================================  =================================
