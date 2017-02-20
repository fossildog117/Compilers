import math
import re

import numpy as np

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def polygon():
    output = []
    with open('input.txt') as f:
        for line in f:
            inputLine = line.split(' ')[1].split('#')
            for poly in inputLine[1].split(';'):
                values = []
                for item in re.split('\),\(|\)|\(', poly)[1:-1]:
                    pair = item.split(',')
                    values.append([float(pair[0]), float(pair[1])])
                output.append(values)
    return output


def robots():
    output = []

    with open('input.txt') as f:
        for line in f:
            inputLine = line.split(' ')[1].split('#')
            for item in re.split('\),\(|\)|\(', inputLine[0])[1:-1]:
                pair = item.split(',')
                output.append([float(pair[0]), float(pair[1])])

    return output


def distance(x1, y1, x2, y2):
    x3 = x1 - x2
    y3 = y1 - y2
    return math.sqrt((x3 * x3) + (y3 * y3))



