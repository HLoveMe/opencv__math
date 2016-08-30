# -*- coding: utf-8 -*-

import  numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FuncFormatter


def pi_formatter(x, pos):
    # x 为设置的刻度 0*k,1*k....
    # pos 第n个

    m = np.round(x / (np.pi / 4))
    n = 4
    if m % 2 == 0: m, n = m / 2, n / 2
    if m % 2 == 0: m, n = m / 2, n / 2
    if m == 0:
        return "0"
    if m == 1 and n == 1:
        return "$\pi$"
    if n == 1:
        return r"$%d \pi$" % m
    if m == 1:
        return r"$\frac{\pi}{%d}$" % n
    return r"$\frac{%d \pi}{%d}$" % (m, n)

x = np.linspace(0,4*np.pi,100)
y = np.sin(x)

plt.figure(figsize=(8,6))
ax = plt.gca()
# plt.plot(x,y,'r--')
ax.plot(x,y,'g--')
# 设置y轴文本
plt.ylabel("Y")
ax.set_ylabel("YYY")
ax.yaxis.set_label_text("Y_Y")

# 设置x轴文本
plt.xlabel("->X")
ax.set_xlabel("->XX")
ax.xaxis.set_label_text("->X_X")
# 设置X轴主刻度

ax.xaxis.set_major_locator(MultipleLocator(np.pi/4))#刻度为pi/4

ax.xaxis.set_major_formatter( FuncFormatter( pi_formatter) )  # 设置函数来转换(n * pi/4)


# 设置刻度文本属性
labels = ax.xaxis.get_ticklabels()
for lab in labels:
    # matplotlib.text.Text:Artist
    from matplotlib.text import  Text
    lab.set_color('r')
    lab.set_rotation(45)
    lab.set_fontsize(14)

# 设置副刻度
ax.xaxis.set_minor_locator(MultipleLocator(np.pi/20))
#开启网格
plt.gca().grid()
# plt.grid()


plt.ylim((-1.5,1.5))
plt.xlim(0,4*np.pi)
plt.show()