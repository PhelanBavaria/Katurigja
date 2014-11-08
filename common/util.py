

import math


def rect(r, d, use_degrees=True):
    if use_degrees:
        d = math.radians(d)
    d -= math.pi
    return round(r*math.sin(d), 2), round(r*math.cos(d), 2)

def polar(x, y, return_degrees=True):
    result = math.atan2(x, y)+math.pi
    if return_degrees:
        result = math.degrees(result)
    return result


if __name__ == '__main__':
    print(polar(-1, -1))
    print(rect(1, 45), 45)
    print(rect(1, 90), 90)
    print(rect(1, 135), 135)
    print(rect(1, 180), 180)
    print(rect(1, 225), 225)
    print(rect(1, 270), 270)
    print(rect(1, 315), 315)
    print(rect(1, 360), 360)
