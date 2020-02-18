import cv2
import numpy as np


COLOR_BLUE = (255, 0, 0)
COLOR_RED = (0, 0, 255)


def bb_draw(file, bounding_boxes, ext, border_color=COLOR_BLUE):
    """
    Draw Bounding Boxes

    :param file: file descriptor
    :param bounding_boxes: Bounding boxes as a list of matrix of integers, e.g.
           [[[1066, 25], [1437, 492]], ..., [[153, 167], [491, 666]]]
    :param ext: File extension that defines the output format.
    :param border_color: Borders color, as a tuple: (B, G, R)
    :return: An image as a memory buffer.
    """

    image = np.fromfile(file, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    for bb in bounding_boxes:
        pt1, pt2 = tuple(bb[0]), tuple(bb[1])
        image = cv2.rectangle(image, pt1, pt2, border_color, 2)
    _, image = cv2.imencode(ext, image)
    return image
