import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import ScenarioWeek4
import itertools

polygonArray = ScenarioWeek4.polygon()


def polygonEdges():
    polygonEdgeArray = []
    for shape in polygonArray:
        edges = []
        for i in range(-1, len(shape) - 1):
            edges.append([ScenarioWeek4.Coordinate(False, shape[i][0], shape[i][1]), ScenarioWeek4.Coordinate(False, shape[i + 1][0], shape[i + 1][1])])

        polygonEdgeArray.append(edges)
    return polygonEdgeArray


edges = polygonEdges()


def plotRobots(plt):
    x, y = [], []
    coordinates = []
    points = ScenarioWeek4.robots()
    for robot in points:
        x.append(robot[0])
        y.append(robot[1])
        coordinates.append(ScenarioWeek4.Coordinate(True, x, y))

    plt.scatter(x[1:], y[1:])
    plt.scatter(x[0:1], y[0:1], color="r")
    lines = zip(*itertools.chain.from_iterable(itertools.combinations(points, 2)))

    plt.plot(*lines)


def printLines(polygons, plt):
    for p in polygons:
        x = []
        y = []
        for coordinate in p:
            x.append(coordinate[0])
            y.append(coordinate[1])

        plt.scatter(x, y, color="orange")


fig, ax = plt.subplots()
patches = []
N = 5

plotRobots(ax)
printLines(polygonArray, ax)

for i in ScenarioWeek4.polygon():
    polygon = Polygon(np.array(i), True)
    patches.append(polygon)

p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)

colors = 100 * np.random.rand(len(patches))
p.set_array(np.array(colors))

ax.add_collection(p)

plt.show()
