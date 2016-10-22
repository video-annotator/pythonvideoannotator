import numpy as np
from scipy.interpolate import interp1d


def interpolate_positions(values, begin, end, interpolation_mode=None):
    computed_time   = np.array(range(begin, end + 1))  # pylint: disable=no-member
    frames          = []
    measures_x      = []
    measures_y      = []

    for i, pos in values:
        x, y = pos
        frames.append(i)
        measures_x.append(x)
        measures_y.append(y)

    frames     = np.array(frames)       # pylint: disable=no-member
    measures_x = np.array(measures_x)   # pylint: disable=no-member
    measures_y = np.array(measures_y)   # pylint: disable=no-member

    if interpolation_mode == None:
        kind = 'slinear'
        if len(frames) == 3: kind = 'quadratic'
        if len(frames) >= 4: kind = 'cubic'
    else:
        kind = interpolation_mode
        if   len(measures_x)<3 and (kind=='quadratic' or kind=='cubic'):   kind = 'slinear'
        elif len(measures_x)<4 and kind=='cubic':                          kind = 'quadratic'

    cubic_interp    = interp1d(frames, measures_x, kind=kind)
    measures_x      = cubic_interp(computed_time)
    cubic_interp    = interp1d(frames, measures_y, kind=kind)
    measures_y      = cubic_interp(computed_time)

    results = []
    for frame, x, y in zip(range(begin, end + 1), measures_x, measures_y):
        results.append([frame, (x, y)])
    return results