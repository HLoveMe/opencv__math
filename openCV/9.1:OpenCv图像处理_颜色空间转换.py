# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt
import cv2
"""
            根据 颜色 显示物体物体



    BGR---->GRAY  cv2.COLOR_BGR2GRAY
    BRG---->HSV   cv2.COLOR_BGR2HSV

    HSV模型:
        H:色调   0-180
        S;饱和度 0-255
        V:亮度   0-255
    不同的工具 取值范围可能有些不同

     黑   灰  白   红    橙    黄   绿   青   蓝    紫
hmin 0    0   0   0|156  11   26  35   78   100  125
hmax 180 180 180  10|180 25   34  77   99   124  155
smin 0    0   0   43     43   43   43  43   43   43
smax 255  43  30  255   255   255  255 255  255  255
vmin 0   46  221  46     46   46   46  46   46   46
vmax 46  220 255   255   255  255  255  255 255  255

    cv2.cvtColor()  颜色转换
    cv2.inRange()   查找图片中 范围颜色 的范围
"""

flag=False
if flag:
    im = cv2.imread("./pg.jpg")
    new = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)


    def mouseCallback(event, cols, rows, *args):
        if event == cv2.EVENT_MOUSEMOVE:
            print "行:", rows, "列:", cols
            print "BGR:", im[rows][cols]
            print "RGB:", im[rows][cols][::-1]
            print "HSV", new[rows][cols]
            print "===================================="


    cv2.namedWindow("image")
    # cv2.setMouseCallback("image",mouseCallback)
    cv2.imshow("AA", im)
    cv2.imshow("image", new)

    # HSV
    low = np.array([105, 50, 50])
    up = np.array([124, 255, 255])
    mask = cv2.inRange(new, low, up)
    print mask[90:100, 180:210]
    print new.shape
    print mask.shape

    new2 = cv2.bitwise_and(im, im, mask=mask)
    cv2.imshow("new2", new2)
    cv2.waitKey(0)


else:
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    cv2.namedWindow("video",cv2.cv.CV_WINDOW_AUTOSIZE)
    # 颜色
    low , up = np.array([0, 0, 211]), np.array([179,30,255])
    while(cap.isOpened()):
        ret,img = cap.read()
        if ret:
            new = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(new,low,up)
            new = cv2.bitwise_and(img,img,mask=mask)
            cv2.imshow('video',new)
    cv2.destroyAllWindows()


"""
    green=np.uint8([[[0,255,0]]])
    hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)

    [[[60 255 255]]]
"""