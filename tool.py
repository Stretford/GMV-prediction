from __future__ import division
import math
__author__ = 'stretford'


def gaussian(center, width, x):
    y = (x - center) ** 2
    #print(y / (-2 * (width ** 2)))
    y = y / (-2 * (width ** 2))

    #print(y)
    return math.e ** y


