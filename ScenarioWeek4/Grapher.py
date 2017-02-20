import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import ScenarioWeek4


def plotRobots(plt):
    x, y = [], []
    for robot in ScenarioWeek4.robots():
        x.append(robot[0])
        y.append(robot[1])

    plt.scatter(x[1:], y[1:])
    plt.scatter(x[0:1], y[0:1], color="r")

fig, ax = plt.subplots()
patches = []
N = 5

plotRobots(ax)

for i in ScenarioWeek4.polygon():
    polygon = Polygon(np.array(i), True)
    patches.append(polygon)

p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)

colors = 100*np.random.rand(len(patches))
p.set_array(np.array(colors))

ax.add_collection(p)

plt.show()


