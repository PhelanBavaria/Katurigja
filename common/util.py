

import math


def rect(r, d):
    return r*math.cos(d), r*math.sin(d)

def polar(x, y):
    return math.atan2(x, y)+math.pi
