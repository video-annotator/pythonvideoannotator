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


- Download & install [Anaconda](https://www.anaconda.com/download/) or [Miniconda](https://conda.io/miniconda.html).
- Download & install the environment configuration file.

|

**for ubuntu:**

.. code-block:: bash

	conda install wget
	wget https://raw.githubusercontent.com/UmSenhorQualquer/pythonVideoAnnotator/master/environment-ubuntu17.yml --no-check-certificate
	conda env create -f environment-ubuntu17.yml
	source activate videoannotator

**for mac:**

.. code-block:: bash

	conda install wget
	wget https://raw.githubusercontent.com/UmSenhorQualquer/pythonVideoAnnotator/master/environment-macosx.yml --no-check-certificate
	conda env create -f environment-macosx.yml
	source activate videoannotator


**for windows:**

.. note :: 

	Make sure you are using the Anaconda prompt to execute the next commands.

.. code-block:: bash

	conda install -c menpo wget
	wget https://raw.githubusercontent.com/UmSenhorQualquer/pythonVideoAnnotator/master/environment-windows.yml --no-check-certificate
	conda env create -f environment-windows.yml
	conda activate videoannotator

|

- Activate the environment, download the source code and install it:

**for ubuntu, mac and windows:**

.. code-block:: bash
	
	git clone --recursive https://github.com/UmSenhorQualquer/pythonVideoAnnotator.git
	cd pythonVideoAnnotator
	python install.py

|


Running
-----------

**for ubuntu, mac and windows:**

.. code-block:: bash

	source activate videoannotator
	python -m pythonvideoannotator
