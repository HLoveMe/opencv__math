# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt

import cv2
print "opencv 加载的图片为BGR,matplotlib为RGB"
"http://stackoverflow.com/questions/15072736/extracting-a-region-from-an-image-using-slicing-in-python-opencv/15074748#15074748"

img = cv2.imread('./c.jpg')
cv2.imshow("cv2",img)
cv2.waitKey(0)

ax = plt.subplot(121)
ax.imshow(img)

ax2 = plt.subplot(122)
# b,g,r=cv2.split(img)
# img2 = cv2.merge([r,g,b])
img2=img[:,:,::-1]
ax2.imshow(img2)


plt.xticks([])
plt.yticks([])

plt.show()

