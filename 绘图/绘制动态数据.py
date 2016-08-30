# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D


# print np.__version__
# fig = plt.figure()
# ax = fig.add_subplot()
# rand = np.random.rand(10)
# ax.plot(rand,'g--')
#
#
# animation.FuncAnimation(plt.gca(),)

fig = plt.figure()
axes1 = fig.add_subplot(111)

# 取第一条Line2D
line, = axes1.plot(np.random.rand(10))

# 更新显示对象 参数为数据
def update(data):
    line.set_ydata(data)
    return line
    # return Line2D(data,np.arange(0,10,1),transform=fig.transFigure, figure=fig)


# 每生成数据 无参数
def data_gen():
    while True:
        yield np.random.rand(10)

#   视图 更新
"""
def __init__(self, fig, func, frames=None, init_func=None, fargs=None,
                 save_count=None, **kwargs):
    fig:Figure
    func:更新显示数据  返回显示对象
        参数为:   frames的返回值  +  fargs
        return:绘画对象Line2D...
    frames : a generator, an iterable, or a number of frames. 显示的数据 获得者
            如果为空 默认return 0,1,2,3,4 .....N 次数 (也可以指定为一个数 表明 在0--X之间循环 0,1,2,3,4...X,0,1,2,3...X)
            如果指定 返回需要的需要显示的数据 object
    init_func:用于显示之前的绘画 返回显示对象
              会被调用一次  如果没指定 就使用第一帧计算结果进行显示
              如果第一帧一直显示设置该函数
    save_count:系统默认会保存100张绘画结果
    **kwargs:
        interval   间隔毫秒数
        repeat_delay  动画开始多少秒重复之前的动画
        blit=True:表明只需要绘制显示的更新的视图
        repeat:是否重复

"""


ani = animation.FuncAnimation(plt.gcf(), update, data_gen, interval=2 * 1000)
# 把动画图保存为视频
"""
def save(self, filename, writer=None, fps=None, dpi=None, codec=None,
             bitrate=None, extra_args=None, metadata=None, extra_anim=None,
             savefig_kwargs=None):
"""
#需要安装FFMPEG
# ani.save('animation.mp4',writer="ffmpeg",fps=30)
plt.show()