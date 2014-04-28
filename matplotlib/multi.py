# coding:utf8

import numpy as np
import matplotlib.pylab as plt
# from xkcd import XKCDify

'''将图形画在一个矩阵制定的表中，利用subplot，plot()中放有多个自变量和函数,画多坐标图'''
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0.0, 5.0, 0.05)
t2 = np.arange(0.0, 5.0, 0.05)
plt.figure(1)
plt.subplot(211)  #subplot(numRows, numCols, plotNum),如：subplot(221)
lines = plt.plot(t1, f(t1),'bo', t2, f(t2), 'r--')
plt.setp(lines[0], marker = '*')

plt.title('pylab first example',fontsize = 16)
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.title('pylab second example',fontsize = 16)

# ax = plt.axes()
# XKCDify(ax)

plt.show()