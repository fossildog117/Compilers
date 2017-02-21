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

<<<<<<< HEAD
=======
# plot the robots
>>>>>>> origin/scenarioweek
def plotRobots(plt):
    x, y = [], []
    coordinates = []
    points = ScenarioWeek4.robots()
    # create array of x coordinates, y coordinates and Coordinates
    for robot in points:
        x.append(robot[0])
        y.append(robot[1])
        coordinates.append(ScenarioWeek4.Coordinate(True, robot[0], robot[1]))

    # plot x,y coordinates
    plt.scatter(x[1:], y[1:])
    plt.scatter(x[0:1], y[0:1], color="r")
    
    # generate all possible lines
    lines = zip(*itertools.chain.from_iterable(itertools.combinations(points, 2)))

<<<<<<< HEAD
    permutations = []

    for i in range(0, len(coordinates)):
        for j in range(i, len(coordinates)):
            permutations.append((coordinates[i], coordinates[j]))

    new = []
    plotList = []
    removeList = []
    for coordinate in permutations:
        for edge in edges:
            for c in edge:
                if ScenarioWeek4.intersect(coordinate[0], coordinate[1], c[0], c[1]) is True:
                    removeList.append((coordinate[0], coordinate[1]))
                else:
                    plotList.append((coordinate[0], coordinate[1]))

    for item in removeList:
        while item in plotList:
            plotList.remove(item)

    for plot in plotList:
        plt.plot([plot[0].x, plot[1].x], [plot[0].y, plot[1].y])
=======
    # plot the lines
    plt.plot(*lines)
>>>>>>> origin/scenarioweek

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
