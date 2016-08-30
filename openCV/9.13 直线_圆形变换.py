# -*- coding: utf-8 -*-


import numpy  as np
import cv2
import matplotlib.pyplot as plt

def A():
    img = cv2.imread('./sd.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ker = np.ones((3, 3), np.uint8)
    gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, ker)

    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    """
        1:
        np.pi/90:
        150:最短直线
        10: 最短间距

    """
    lines = cv2.HoughLinesP(edges, 1, np.pi / 90, 150, 10)
    for x1, y1, x2, y2 in lines[0]:
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

    cv2.imshow("A", img)
    cv2.waitKey(0)


def B():
    im = cv2.imread("./logo.png",0)
    circle = cv2.HoughCircles(im,cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=45,maxRadius=0)
    circle = np.uint16(np.around(circle))
    for x,y,r in circle[0]:
        print r
        cv2.circle(im,(x,y),r,(0,0,0))
    cv2.imshow("A",im)
    cv2.waitKey(0)


B()
