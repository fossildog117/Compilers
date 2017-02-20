import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import ScenarioWeek4

def polygons():
    output = []
    with open('input.txt') as f:
        for line in f:
            inputLine = line.split(' ')[1].split('#')
            for poly in inputLine[1].split(';'):
                output.append(poly)

    return output

fig, ax = plt.subplots()
patches = []
N = 5

print(polygons())

for i in ScenarioWeek4.polygon():
    print(np.array(i))
    polygon = Polygon(np.array(i), True)
    patches.append(polygon)

p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)

colors = 100*np.random.rand(len(patches))
p.set_array(np.array(colors))

ax.add_collection(p)

plt.show()


