import numpy as np


def boxes_to_corners(box_xy, box_wh):
    ''' Converts the grid cell local coordinates to full grid world image coordinates.

    :param box_xy: x and y coordinates w.r.t. the 7x7 grid cells (always between 0 and 1)
    :param box_wh: width and height scales of the object (maybe >1)
    :return: (x1, y1, x2, y2), coordinates of upper left and bottom right corners of the bounding box w.r.t. the 7x7 full grid
    '''

    boxes = np.zeros((4, 7, 7))
    box_xy_midpoints = np.zeros((2, 7, 7))
    for r in range(7):
        for c in range(7):
            box_xy_midpoints[0, r, c] = (c + box_xy[0, r, c])/7
            box_xy_midpoints[1, r, c] = (r + box_xy[1, r, c])/7

            boxes[0, r, c] = box_xy_midpoints[0, r, c] - box_wh[0, r, c] / 2
            boxes[1, r, c] = box_xy_midpoints[1, r, c] + box_wh[1, r, c] / 2
            boxes[2, r, c] = box_xy_midpoints[0, r, c] + box_wh[0, r, c] / 2
            boxes[3, r, c] = box_xy_midpoints[1, r, c] - box_wh[1, r, c] / 2
    print('\nboxes = \n', boxes)

    return boxes
