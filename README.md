# Low-level-YOLO-Implementation
A low-level implementation of functionalities needed in YOLO object detection from scratch in Python.

YOLO network architecture starts from an input image of size (h=448,w=448,c=3) and it uses a series of convolution (CONV) and pooling (MAX POOL) layers and converge to a final output block of size (7,7,30).
 
As per the key characteristic of YOLO, if the midpoint of an object falls into a grid cell, that grid cell is responsible for detecting the object. So, each pixel in this output’s each layer is responsible for image detection criteria. It is a list of bounding boxes along with the recognized classes. Each bounding box is provided by 6 information namely box probability, box coordinates/dimensions and the class probability/box confidence (pc, bx, by, bh, bw and c). 

Each layer in this output could be identified as. The following procedure is done in order to obtain the scores, boxes and classified class labels.
1.	First, the corresponding outputs are retrieved from the output block given.
2.	Computing the box scores by elementwise multiplication of the box probability and class probability.
3.	There can be more number of boxes which corresponds to a single image. This happens at nearby grid cells producing multiple bounding boxes. To get rid of these duplicate boxes, we perform filtering at two stages. First, we need to get rid of boxes with low scores (score thresholding – means that the box is not much confident in detecting a class). Then, we select only one box when several boxes overlap with each other and detect the same object (Non-Max Suppression). We have to scale up the box coordinates to the image size before performing NMS operation.
4.	After Non-Max Suppression (NMS), it then outputs the recognized objects together with the bounding boxes scaled up to the image size.

Above functions can be written using the libraries such as Keras. Here, I have written all those functionalities from scratch in Python. YOLO is a very efficient algorithm as it uses only one forward propagation pass to make the predictions as its name says ‘You Only Look Once’. People tend to use YOLO to achieve this higher efficiency. So, The above low level implementation will further contribute in speeding up getting predictions. Also, platforms such as Raspberry Pi’s may find difficult to run such libraries. This will avoid that issue.

References:
Convolutional Neural Networks by deeplearning.ai by Prof. Andrew Ng. on Coursera: https://www.coursera.org/learn/convolutional-neural-networks
