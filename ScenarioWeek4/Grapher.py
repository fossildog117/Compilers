import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import ScenarioWeek4
import itertools

polygonArray = ScenarioWeek4.polygon()

# Get a list of all the edges of every polygon
# edges = [polygon1, polygon2, polygon3]
# polygon = [[coordinate1, coordinate2], [coordinate2, coordinate3], [coordinate3, coordinate4], [coordinate4, coordinate1]]
def polygonEdges():
    polygonEdgeArray = []
    for shape in polygonArray:
        edges = []
        for i in range(-1, len(shape) - 1):
            edges.append([ScenarioWeek4.Coordinate(False, shape[i][0], shape[i][1]), ScenarioWeek4.Coordinate(False, shape[i + 1][0], shape[i + 1][1])])

        polygonEdgeArray.append(edges)
    return polygonEdgeArray


edges = polygonEdges()

# plot the robots
def plotRobots(plt):
    x, y = [], []
    coordinates = []
    points = ScenarioWeek4.robots()
    # create array of x coordinates, y coordinates and Coordinates
    for robot in points:
        x.append(robot[0])
        y.append(robot[1])
        coordinates.append(ScenarioWeek4.Coordinate(True, x, y))

    # plot x,y coordinates
    plt.scatter(x[1:], y[1:])
    plt.scatter(x[0:1], y[0:1], color="r")
    
    # generate all possible lines
    lines = zip(*itertools.chain.from_iterable(itertools.combinations(points, 2)))

    # plot the lines
    plt.plot(*lines)

# print cornors of each polygon 
def printLines(polygons, plt):
    # for each polygon
    for p in polygons:
        x = []
        y = []
        # for each coordinate in a polygon
        for coordinate in p:
            x.append(coordinate[0]) # get x coordinate
            y.append(coordinate[1]) # get y coordinate
        
        # plot x,y values for each cornor
        plt.scatter(x, y, color="orange")


fig, ax = plt.subplots()
patches = []

plotRobots(ax)
printLines(polygonArray, ax)

# print the shape of the polygon
for i in ScenarioWeek4.polygon():
    polygon = Polygon(np.array(i), True)
    patches.append(polygon)

p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)

colors = 100 * np.random.rand(len(patches))
p.set_array(np.array(colors))

ax.add_collection(p)

plt.show()
