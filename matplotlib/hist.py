# coding:utf8

import numpy as np
import matplotlib.pyplot as plt
from xkcd import XKCDify

x = np.arange(0,10,0.5)
y = np.random.rand(20)
plt.bar(x, y)

plt.title('Hist of Y')
plt.xlabel('Smarts')
plt.ylabel('NormProbability')
plt.text(2,0.12,'mu=10,sigma=20')
plt.grid(True)

ax = plt.axes()
XKCDify(ax)

plt.show()