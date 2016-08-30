# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt
import cv2
import  threading


print "练习"
a = cv2.imread("./a.jpg")
b = cv2.imread('./aa.jpg')
alp= 0
wname="name"


def jianbian():
    print alp
    global alp
    cv2.destroyWindow(wname)
    c = cv2.addWeighted(a,alp,b,(1-alp),0)
    cv2.imshow(wname,c)
    cv2.waitKey(1)
    print "AA"

import time
for i in range(1000):
    alp=alp+0.05
    if alp<1.0:
        jianbian()
    elif alp>=1.0:
        alp=1.0
        jianbian()
        cv2.waitKey(0)
        break
    time.sleep(0.2)



