# -*- coding: utf-8 -*-


import numpy  as np
import cv2
import pickle

a = "A"

img1 = np.zeros((100,100,3),dtype=np.uint8)
img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
"""
putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None):
"""
cv2.putText(img,"A",(40,40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

cons,h =  cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img1,cons,0,(0,0,255),1)



img2 = cv2.imread("./AAAA.jpg",0)
ker = np.ones((5, 5), np.uint8)
img22 = cv2.morphologyEx(img2,cv2.MORPH_OPEN,ker)

ret , img22 = cv2.threshold(img22,175,255,cv2.THRESH_BINARY_INV)

cons2,h =  cv2.findContours(img22,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img2 = cv2.imread("./AAAA.jpg")
cv2.drawContours(img2,cons2,3,(0,0,255),1)


print cv2.matchShapes(cons[0], cons2[3], 3, 0.0)

cv2.imshow("A",img1)
cv2.imshow("AB",img2)
cv2.waitKey(0)

