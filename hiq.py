import matplotlib.pyplot as plt
from coreprogram import *

test1 = orders()

data = test1.tracepath
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111, frameon=False)
ax.grid(True)
ax.plot(*zip(*data),marker='o')
plt.show()