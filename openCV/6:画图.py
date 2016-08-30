# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt
import cv2

# def line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None):
# 图片  起点 结束点 颜色(0,0,0)
#  thickness:线条的粗细  -1 表示闭合图形 会填充  default:1
# lintype 线的样式

img = np.zeros((500,500,3),dtype=np.uint8)
#划线
# cv2.line(img,(0,0),(99,99),(255,255,255),thickness=1,lineType=8)

#矩形  对角线
cv2.rectangle(img,(2,2),(20,20),(100,0,0))

# 画圆
# cv2.circle(img,(250,250),100, (0,0,255), thickness=-1,lineType=5)

#椭圆             中点   (长/短轴) 旋转    起始       终点
# ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness=None, lineType=None, shift=None):
# cv2.ellipse(img,(255,255),(100,50),45,0,360,(0,100,0),thickness=1)

#文字
# putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"OpenCV",(250,100),font,1,(100,0,0),thickness=2)

plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()
