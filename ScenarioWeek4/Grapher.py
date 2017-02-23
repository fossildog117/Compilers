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
        coordinates.append(ScenarioWeek4.Coordinate(True, robot[0], robot[1]))

    plt.scatter(x[1:], y[1:])
    plt.scatter(x[0:1], y[0:1], color="r")
    # lines = zip(*itertools.chain.from_iterable(itertools.combinations(points, 2)))
    #
    # permutations = []
    #
    # for i in range(0, len(coordinates)):
    #     for j in range(i, len(coordinates)):
    #         permutations.append((coordinates[i], coordinates[j]))
    #
    # new = []
    # plotList = []
    # removeList = []
    # for coordinate in permutations:
    #     for edge in edges:
    #         for c in edge:
    #             if ScenarioWeek4.intersect(coordinate[0], coordinate[1], c[0], c[1]):
    #                 removeList.append((coordinate[0], coordinate[1]))
    #             else:
    #                 plotList.append((coordinate[0], coordinate[1]))
    #
    # for item in removeList:
    #     while item in plotList:
    #         plotList.remove(item)
    #
    # for plot in plotList:
    #     plt.plot([plot[0].x, plot[1].x], [plot[0].y, plot[1].y])


def plotOutcome(plt):
    arr = [[-40.57514036406533,3.8],[-40.107250530132994,4.1191949194803605],[4.175406496760833,-3.998734909058124],[5.121219735988028,-6.83652587991083],[9.273944427991669,-4.0688131781605605],[10.112241239798287,-0.1576421955372227],[35.617398615875445,3.19807223209778],[46.616643638540644,-11.085366042049392],[54.04098273274328,-5.998206813728088],[52.946466551349,-4.99644686618755]]
    for i in range(0, len(arr) - 1):
        print([[arr[i][0], arr[i][1]],[arr[i+1][0], arr[i+1][1]]])
        plt.plot([arr[i][0], arr[i][1]],[arr[i+1][0], arr[i+1][1]])


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
plotOutcome(ax)

for i in ScenarioWeek4.polygon():
    polygon = Polygon(np.array(i), True)
    patches.append(polygon)

p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)

colors = 100 * np.random.rand(len(patches))
p.set_array(np.array(colors))

ax.add_collection(p)
plt.show()
