from __future__ import division
from pyvisgraph.graph import Point, Edge, Graph
from pyvisgraph.vis_graph import VisGraph
from ScenarioWeek4 import GreedyDynamicSchedule as gd

import pyvisgraph as vg

polys = [[vg.Point(0.0,1.0), vg.Point(3.0,1.0), vg.Point(1.5,4.0)],
         [vg.Point(4.0,4.0), vg.Point(7.0,4.0), vg.Point(5.5,8.0)]]


pointArray = []

bigValue = 100000000000000000000

id = 0
for polygon in gd.polygons:
    p = []
    for point in polygon:
        p.append(Point(point[0] * bigValue * 1.001, point[1] * bigValue * 1.001, id))
        id += 1
    pointArray.append(p)




g = vg.VisGraph()
g.build(pointArray)
shortest = g.shortest_path(Point(-29.0939934671409 * bigValue,-26.282070505327646 * bigValue), Point(27.277154257681794 * bigValue,29.286506198923735 * bigValue))

# (-29.0939934671409, -26.282070505327646), (27.277154257681794, 29.286506198923735)

# (-84.2787860814455, -111.42966972146854), (70.69506359346656, 78.41810448767427)


print(shortest)

outputString = ""

for p in shortest:
    outputString += "({x},{y}),".format(x=(p.x/bigValue), y=(p.y/bigValue))

print(outputString)



