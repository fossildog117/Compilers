import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import ScenarioWeek4
import itertools

def plotRobots(plt):
    x, y = [], []
    points = ScenarioWeek4.robots()
    for robot in points:
        x.append(robot[0])
        y.append(robot[1])

    plt.scatter(x[1:], y[1:])
    plt.scatter(x[0:1], y[0:1], color="r")
    print(*zip(*itertools.chain.from_iterable(itertools.combinations(points, 2))))
    plt.plot(*zip(*itertools.chain.from_iterable(itertools.combinations(points, 2))))

def printLines(polygons, plt):

    for p in polygons:
        x = []
        y = []
        for coordinate in p:
            x.append(coordinate[0])
            y.append(coordinate[1])

        plt.scatter(x, y, color="orange")




polygonArray = ScenarioWeek4.polygon()

fig, ax = plt.subplots()
patches = []
N = 5

plotRobots(ax)
printLines(polygonArray, ax)

for i in ScenarioWeek4.polygon():
    polygon = Polygon(np.array(i), True)
    patches.append(polygon)

p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)

colors = 100*np.random.rand(len(patches))
p.set_array(np.array(colors))

ax.add_collection(p)

plt.show()


