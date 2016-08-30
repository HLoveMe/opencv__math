# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt
import cv2,os
"""
   cap = cv2.VideoCapture(0)  得到设备  0 1 等代表摄像头 文件名这是视频文件
   cap.isOpened()               检查是否打开
   cap.open()                 打开设备
   cap.read()   -->bool,ndarray   表明是否读取到数据/读取到的数据
   cap.get(proid  0-18)  得到设备的某些信息
   cap.set(id,value)

cv2.cv.


0:CV_CAP_PROP_POS_MSEC 当前视频的position
1:CV_CAP_PROP_POS_FRAMES
2:CV_CAP_PROP_POS_AVI_RATIO  得到视频相对位置  0 : 相对头   1:相对结尾
3:CV_CAP_PROP_FRAME_WIDTH
4:CV_CAP_PROP_FRAME_HEIGHT
5:CV_CAP_PROP_FPS         FPS
6:CV_CAP_PROP_FRAME_COUNT   总帧数
7:CV_CAP_PROP_FORMAT   格式
8:CV_CAP_PROP_BRIGHTNESS 亮度 仅仅用于相机
.CV_CAP_PROP_CONTRAST  对比度 仅仅用于相机
.CV_CAP_PROP_SATURATION  饱和度 仅仅用于相机
.CV_CAP_PROP_HUE     色彩 仅仅用于相机
.CV_CAP_PROP_GAIN Gain of the image (only for cameras).
.CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
.CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
.CV_CAP_PROP_WHITE_BALANCE Currently unsupported
.CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend cur- rently)
"""


# flag = False
# if flag:
#     #摄像头捕捉
#     cap = cv2.VideoCapture(0)
#     cv2.namedWindow("video", cv2.cv.CV_WINDOW_AUTOSIZE)
#     while (True):
#         success, frame = cap.read()
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow('video', gray)
#     cap.release()
#     cv2.destroyAllWindows()
# else:
#     # 播放本地视频
#     file = "./video.mp4"
#     cap = cv2.VideoCapture(file)
#     fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
#     wait = int(1000/fps)
#     print cap.get(cv2.cv.CV_CAP_PROP_FORMAT)
#     while (cap.isOpened()):
#         ret, frame = cap.read()
#         cv2.imshow('frame', frame)
#         cv2.waitKey(1)
#
#     cap.release()
#     cv2.destroyAllWindows()


#视频录制


cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object

fourcc = cv2.cv.FOURCC(*'mp4v')
cap.set(3,640)
cap.set(4,480)
# w=cap.get(3)
# h=cap.get(4)
# out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (int(w),int(h)))
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        frame = cv2.flip(frame,1)

        out.write(frame)

        cv2.imshow('frame',frame)

        cv2.waitKey(25)

# Release everything if job is finished

cap.release()

out.release()

cv2.destroyAllWindows()



