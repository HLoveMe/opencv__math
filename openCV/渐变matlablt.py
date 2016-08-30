# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.image import  AxesImage
from matplotlib.lines import Line2D

import cv2


print "练习"
a = cv2.imread("./a.jpg")[:,:,::-1]
b = cv2.imread('./aa.jpg')[:,:,::-1]
alp= 0
wname="name"


fig = plt.figure(figsize=(8,6))
ax = plt.subplot(111)
ax.set_title(u"渐变")
# plt.xticks([])
# plt.yticks([])
plt.axis("off")
"""
def __init__(self, fig, func, frames=None, init_func=None, fargs=None,
                 save_count=None, **kwargs):
"""
week=100
one = 1.0/week

im = ax.imshow(b,animated=True)
alp=0.5
im.set_array(cv2.addWeighted(a,alp,b,1-alp,0))

def init():
    im.set_array(np.zeros(a.shape,dtype=np.uint8))
    return im,

def func(i):
    print i
    alp=i*one
    im.set_array(cv2.addWeighted(a,alp,b,1-alp,0))
    return im,

anim = FuncAnimation(fig,func,week,init_func=init,blit=True,interval=50,repeat=False)
# anaim = FuncAnimation(fig, animate, init_func=init,
#                                frames=100, interval=20, blit=True)
plt.show()
