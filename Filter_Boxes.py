import numpy as np


def filter_boxes(box_confidence, boxes_all, box_class_probs, score_threshold = 0.6):
    ''' Returns the scores, boxes and classes identified from
    the parameters given in arguments

    :param
    box_confidence -- (1, 7, 7), pc values
    boxes_all -- (4, 7, 7), coordinates of upper left and bottom right corners of the bounding box w.r.t. the 7x7 full grid
    box_class_probs -- (25, 7, 7), class probabilities
    score_threshold -- to get rid from unnecessary boxes

    :return
    scores -- containing class probability score for "selected" boxes
    boxes -- containing (b_x, b_y, b_h, b_w) coordinates of "selected" boxes
    classes -- containing the index of the class detected by the "selected" boxes'''

    box_scores = box_confidence * box_class_probs # 7x7x25
    print('box scores = \n', box_scores)

    # Step 1 - getting all maximum scores to a 2D array
    box_classes = np.zeros((7, 7))       # for index
    box_class_scores = np.zeros((7, 7))  # for maximums
    for row in range(7):
        for col in range(7):
            temp_max = 0
            temp_layer = 0
            for layer in range(25):
                if box_scores[layer, row, col] >= temp_max:
                    temp_max = box_scores[layer, row, col]
                    temp_layer = layer+1
            box_class_scores[row, col] = temp_max
            box_classes[row, col] = temp_layer

    print('box classes = \n', box_classes)
    print('shape of box classes: ', box_classes.shape)
    print('box class scores = \n', box_class_scores)
    print('shape of box class scores: ', box_class_scores.shape, '\n')

    # Step 2 - Filtering by threshold
    scores = []     # python list
    boxes = []      # going to make a 2D list
    classes = []    # python list
    for r in range(7):
        for c in range(7):
            if box_class_scores[r, c] >= score_threshold:
                scores.append(box_class_scores[r, c])
                classes.append(box_classes[r, c])
                boxes.append([boxes_all[0, r, c], boxes_all[1, r, c], boxes_all[2, r, c], boxes_all[3, r, c],])

    print('scores = \n', scores)
    print('shape of scores: ', len(scores), '\n')
    print('classes = \n', classes)
    print('shape of classes: ', len(classes), '\n')
    print('boxes = \n',)
    for R in boxes:
        for C in R:
            print(C, end="\t")
        print()
    print('shape of boxes: ', len(boxes))
    print(boxes)

    return scores, boxes, classes
