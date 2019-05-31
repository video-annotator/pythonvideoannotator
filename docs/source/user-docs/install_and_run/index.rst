.. _installing-label:

****************
Install and Run
****************

|

Quickest installation
______________________


Installing
-----------


1. Install Python 3.6 from  [python.org](https://www.python.org/)

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


| 1. Download & install [Anaconda](https://www.anaconda.com/download/) or [Miniconda](https://conda.io/miniconda.html).
|
| 2. Download & install the environment configuration file:

**for ubuntu:**

.. code-block:: bash

	conda install wget
	wget https://raw.githubusercontent.com/UmSenhorQualquer/pythonVideoAnnotator/master/utils/environment-ubuntu17.yml --no-check-certificate
	conda env create -f environment-ubuntu17.yml
	source activate videoannotator

**for mac:**

.. code-block:: bash

	conda install wget
	wget https://raw.githubusercontent.com/UmSenhorQualquer/pythonVideoAnnotator/master/utils/environment-macosx.yml --no-check-certificate
	conda env create -f environment-macosx.yml
	source activate videoannotator


**for windows:**

.. note :: 

	Make sure you are using the Anaconda prompt to execute the next commands.

.. code-block:: bash

	conda install -c menpo wget
	wget https://raw.githubusercontent.com/UmSenhorQualquer/pythonVideoAnnotator/master/utils/environment-windows.yml --no-check-certificate
	conda env create -f environment-windows.yml
	conda activate videoannotator

|
| 3. Activate the environment, download the source code and install it:

**for ubuntu, mac and windows:**

.. code-block:: bash
	
	git clone --recursive https://github.com/UmSenhorQualquer/pythonVideoAnnotator.git
	cd pythonVideoAnnotator/utils
	python install.py

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





*******************
Install DeepLabCut
*******************

**for windows and mac:**

Run the following commands:

.. code-block:: bash

	pip install deeplabcut
	pip install -U wxPython
	pip install --ignore-installed tensorflow==1.10

**for linux:**

| Go to this link: https://extras.wxpython.org/wxPython4/extras/linux/gtk3/.
| There you will have to choose your linux distribution and the wheel for Python 3.6.
| Then run the commands under, but replace the middle command with whatever fits your linux distribution.
|
| For example, if you have ubuntu 18.04, you will have to run the following commands:

.. code-block:: bash

	pip install deeplabcut
	pip install https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-18.04/wxPython-4.0.4-cp36-cp36m-linux_x86_64.whl
	pip install --ignore-installed tensorflow==1.10