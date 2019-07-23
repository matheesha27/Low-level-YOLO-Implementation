import numpy as np
from Boxes_to_Corners import boxes_to_corners
from Filter_Boxes import filter_boxes
from Scale_Boxes import scale_boxes
from IOU_NMS import iou, non_max_suppression


# Retrieve outputs from CONV3D model
def retrieve_outputs(conv3d):
    ''' Retrieving the parameters from the conv3d model.

    :param conv3d: 7x7x30 yolo output
    :return: box_confidence, (box_xy, box_hw), box_class_probs
    '''

    box_confidence = conv3d[0, :, :] # 7x7x1
    box_xy = conv3d[1:3, :, :] # 7x7x2
    box_wh = conv3d[3:5, :, :] # 7x7x2
    box_class_probabilities = conv3d[5:30, :, :] # 7x7x25 , all class probabilities for all grid cells

    print('box confidence = \n', box_confidence, '\n')
    print('box xy = \n', box_xy, '\n')
    print('box wh = \n', box_wh, '\n')
    print('box class probabilities = \n', box_class_probabilities, '\n')

    return box_confidence, box_xy, box_wh, box_class_probabilities


# A sample matrix with dimensions (30,7,7) to test the output
input3d = np.random.rand(30,7,7)
print('input = \n', input3d, '\n')

# Retrieve outputs of the model
Box_confidence, Box_xy, Box_wh, Box_class_probs = retrieve_outputs(input3d)

# convert boxes to be ready for filtering functions
Corner_Boxes = boxes_to_corners(Box_xy, Box_wh)

# Use filter_boxes() to perform Score-filtering with a threshold of score_threshold
Scores, Filtered_Boxes, Classes = filter_boxes(Box_confidence, Corner_Boxes, Box_class_probs, score_threshold=0.6)

# Scale boxes back to original image shape
Scaled_Boxes = scale_boxes(Filtered_Boxes, image_shape=(720.0, 1280.0))

# Use Non-Max Suppression with a threshold of iou_threshold
Scores, Boxes, Classes = non_max_suppression(Scores, Scaled_Boxes, Classes, iou_threshold=0.5)
