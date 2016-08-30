# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt
import cv2
"""
    状态
EVENT_FLAG_ALTKEY
EVENT_FLAG_CTRLKEY
EVENT_FLAG_LBUTTON
EVENT_FLAG_MBUTTON
EVENT_FLAG_RBUTTON
EVENT_FLAG_SHIFTKEY
EVENT_LBUTTONDBLCLK

EVENT_LBUTTONDOWN  1 左按下
EVENT_LBUTTONUP    4 左抬起
EVENT_MBUTTONDBLCLK
EVENT_MBUTTONDOWN  3 滑轮按下
EVENT_MBUTTONUP    6:滑轮抬起
EVENT_MOUSEMOVE   0 移动
EVENT_RBUTTONDBLCLK
EVENT_RBUTTONDOWN  2:又按下
EVENT_RBUTTONUP    5:右抬起
"""

def mouseCallback(event,cols,rows,*args):
    if event==cv2.EVENT_LBUTTONUP:
        #cv2.circle(img,(250,250),100, (0,0,255), thickness=-1,lineType=5)
        cv2.circle(img,(cols,rows),25,(255,255,255),thickness=1)

img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow("image")
cv2.setMouseCallback("image",mouseCallback)


while True:
    cv2.imshow("image",img)
    if cv2.waitKey(20)&0xFF==27:
        print "----"
        break
cv2.destroyAllWindows()
