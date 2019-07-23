def scale_boxes(boxes, image_shape):
    '''
    Scales the bounding box coordinates given in boxes corresponding to the new image_shape.

    :param boxes: python list of a fixed length (v <= 49, depends on the score_threshold)
    :param image_shape: python tuple, shape of the image in pixels in the order of (breadth, length)
    :return: python list of same length (v) as input, scaled w.r.t. image shape
    '''

    n = len(boxes)
    b, l = image_shape[0], image_shape[1]
    for i in range(n):
        boxes[i][0] *= l
        boxes[i][1] *= b
        boxes[i][2] *= l
        boxes[i][3] *= b

    return boxes
