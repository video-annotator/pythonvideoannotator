.. _installing-label:

****************
Install and Run
****************

|

Quickest installation
______________________


Installing
-----------


1. Install Python 3.6 from [python.org](https://www.python.org/) or use the Anaconda [Anaconda](https://www.anaconda.com/) Python version.

2. Install pypi from [pypi.org](https://pypi.org/)

3. Install PythonVideoAnnotator from Pypi:

.. code-block:: bash

	pip install python-video-annotator


Running
-----------

1. Execute pythonvideoannotator:

.. code-block:: bash

	start-video-annotator

|

For developers
______________


Installing
-----------

Download the source code and install it:

**for ubuntu, mac and windows:**

.. code-block:: bash
	
	git clone --recursive https://github.com/UmSenhorQualquer/pythonVideoAnnotator.git
	cd pythonVideoAnnotator
	python utils/install.py

|


Running
-----------

Run this command:

.. code-block:: bash

	start-video-annotator

Or these commands:


.. code-block:: bash

	source activate videoannotator
	python -m pythonvideoannotator
