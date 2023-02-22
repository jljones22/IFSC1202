from math import pi

def diameter(radius):
    return 2.0 * float(radius)

def circumference(radius):
    return 2.0 * pi * float(radius)

def area(radius):
    return pi * float(radius) ** 2.0

radii = open("06.01 Radius.txt", "rt")
radius = radii.readline()

print("{:>15}{:>15}{:>15}{:>15}".format("Radius", "Diameter", "Circumference", "Area"))

while radius != "":
    print("{:>15.5f}{:>15.5f}{:>15.5f}{:>15.5f}".format(float(radius), diameter(radius), circumference(radius), area(radius)))
    radius = radii.readline()