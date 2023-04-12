from math import *

class Point:

    def __init__(self, Xvalue, Yvalue):
        self.x = Xvalue
        self.y = Yvalue

    def ToString(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
def distance(pointA, pointB):
    return sqrt((pointB.x - pointA.x) ** 2 + (pointB.y - pointA.y) ** 2)

def midPoint(pointA, pointB):
    return Point((pointB.x + pointA.x) / 2, (pointB.y + pointA.y) / 2)

def xAngle(pointA, pointB):
    slope = (pointB.y - pointA.y) / (pointB.x - pointA.x)
    return atan(slope) * (180 / pi)

Points = open("10.05 Points.txt", "rt")
line = Points.readline()

print(f"{'Point A':>20}{'Point B':>20}{'Distance':>20}{'Midpoint':>20}{'Angle':>20}")
print(f"{'---------------':>20}" * 5)

while line != "":
    ls = line.strip().split(',')
    a = Point(float(ls[0]), float(ls[1]))
    b = Point(float(ls[2]), float(ls[3]))

    print(f"{a.ToString():>20}{b.ToString():>20}{distance(a, b):>20.7f}{midPoint(a, b).ToString():>20}{xAngle(a, b):>20.7f}")
    line = Points.readline()
