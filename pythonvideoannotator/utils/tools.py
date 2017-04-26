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



def points_angle(p1, p2): 
	x1, y1 = p1
	x2, y2 = p2
	rads = math.atan2(y2-y1,x2-x1)
	return rads

def min_dist_angles(ang1, ang2):
    tmp  = max(ang1, ang2)
    ang2 = min(ang1, ang2)
    ang1 = tmp
    angle1 = abs(ang1-ang2)
    angle2 = abs(ang1-(np.pi*2)-ang2)
    angle3 = abs(ang1+(np.pi*2)-ang2)
    return min(angle1, angle2, angle3)