def iou(box1, box2):
    ''' Implement the Intersection over union between box1 and box 2.
    Arguments:
    box1 -- (x1, y1, x2, y2), top left and bottom right coordinates of the first box
    box2 -- (x1, y1, x2, y2), top left and bottom right coordinates of the second box
    Returns:
    Intersection over Union (iou) of box1 and box2
    '''

    # Intersection area
    xi1 = max(box1[0], box2[0])
    yi1 = max(box1[1], box2[1])
    xi2 = min(box1[2], box2[2])
    yi2 = min(box1[3], box2[3])
    if box2[0] > box1[2] or box2[1] > box1[3]:
        return 0
    else:
        intersection_area = max(0, (yi2 - yi1) * (xi2 - xi1))
        #print(intersection_area)

        # Union area
        box1_area = (box1[3] - box1[1]) * (box1[2] - box1[0])
        box2_area = (box2[3] - box2[1]) * (box2[2] - box2[0])
        union_area = box1_area + box2_area - intersection_area

        # iou
        if union_area == 0:
            print('box 1=', box1, 'box 2=', box2)
        iou = float(intersection_area) / union_area

        return iou


def non_max_suppression(scores_input, boxes_input, classes_input, iou_threshold = 0.5):
    ''' Applies Non-max suppression (NMS) to set of boxes filtered out from
    filter_boxes() function.

    :param
    scores -- 1D python list, output from filter_boxes()
    boxes -- 2D python list, output from filter_boxes()
    classes -- 1D python list, output from filter_boxes()
    max_boxes -- integer, maximum no. of predicted boxes we would like to have
    iou_threshold -- float, Intersection over Union threshold used for NMS filtering

    :return
    scores -- 1D python list, predicted score of each box
    boxes -- 2D python list, predicted box coordinates
    classes -- 1D python list, predicted class for each box

    * The no. of elements in above lists depend on the threshold values used'''

    n = len(scores_input)
    for i in range(n):
        for j in range(1, n-i):
            if scores_input[j-1] < scores_input[j]:
                (scores_input[j-1], scores_input[j]) = (scores_input[j], scores_input[j-1])
                (classes_input[j - 1], classes_input[j]) = (classes_input[j], classes_input[j - 1])
                (boxes_input[j - 1], boxes_input[j]) = (boxes_input[j], boxes_input[j - 1])
    print('scores sorted = ', scores_input, '\n')
    print('classes sorted = ', classes_input, '\n')
    print('boxes = \n',)
    for R in boxes_input:
        for C in R:
            print(C, end="\t")
        print()

    n = len(scores_input)
    k = 0
    m = 0
    for i in range(n):
        for j in range(n):
            if (i != j) and (iou(boxes_input[i], boxes_input[j]) >= 0.5):
                scores_input.pop(j)
                boxes_input.pop(j)
                classes_input.pop(j)

                new_length_j = len(scores_input)
                if new_length_j - 1 >= j:
                    break
        new_length_i = len(scores_input)
        if new_length_i - 1 >= i:
            break

    return scores_input, boxes_input, classes_input
