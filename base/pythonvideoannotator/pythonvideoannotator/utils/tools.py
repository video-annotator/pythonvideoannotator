import os, math, numpy as np

def list_folders_in_path(path):
	if not os.path.exists(path): return []
	return sorted([os.path.join(path, d) for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])


def list_files_in_path(path):
	if not os.path.exists(path): return []
	return sorted([os.path.join(path, d) for d in os.listdir(path) if not os.path.isdir(os.path.join(path, d))])



def make_lambda_func(func, **kwargs):
    """ Auxiliar function for passing parameters to functions """
    return lambda: func(**kwargs)



