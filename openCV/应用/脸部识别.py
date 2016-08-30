# -*- coding: utf-8 -*-
import numpy as np
import cv2

"""
    /usr/local/share/OpenCV/haarcascades
"""


face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')

img = cv2.imread('./aa.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#找到脸
"""
                gray 源
    scaleFactor:检测时 每次图片放大倍数
    minNeighbors:最小相邻
    minsize:检测特征的最小size
"""
faces =  face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5,5),
    # flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    #脸的gray图
    roi_gray = gray[y:y+h, x:x+w]

    #脸的范围 原图
    roi_color = img[y:y+h, x:x+w]

    #查找眼范围
    eyes = eye_cascade.detectMultiScale(
    roi_gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(10,10),
    # flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    print len(eyes)
    #画眼
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()