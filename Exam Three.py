import math

class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = float(s1)
        self.s2 = float(s2)
        self.s3 = float(s3)
    
    def type(self):
        if self.s1 == self.s2 and self.s1 == self.s3: return "Equailateral"
        elif self.s1 == self.s2 or self.s1 == self.s3: return "Isocelese"
        else: return "Scalene"

    def perimeter(self): return self.s1 + self.s2 + self.s3
    def area(self):
        semiP = self.perimeter() / 2
        return math.sqrt((semiP * (semiP - self.s1) * (semiP - self.s2) * (semiP - self.s3)))
    
    def angles(self):
        ls = []
        ls.append(math.degrees(math.acos((self.s2 ** 2 + self.s3 ** 2 - self.s1 ** 2) / (2 * self.s2 * self.s3))))
        ls.append(math.degrees(math.acos((self.s1 ** 2 + self.s3 ** 2 - self.s2 ** 2) / (2 * self.s3 * self.s1))))
        ls.append(math.degrees(math.acos((self.s1 ** 2 + self.s2 ** 2 - self.s3 ** 2) / (2 * self.s1 * self.s2))))
        return ls

triangle = open("Exam Three Triangles.txt", "rt")
line = triangle.readline()

TriangleList = []

while line != "":
    ls = line.strip().split(',')

    TriangleList.append(Triangle(ls[0], ls[1], ls[2]))
    line = triangle.readline()

print(f"{'Type':>12}{'Side 1':>11}{'Side 2':>11}{'Side 3':>11}{'Perimeter':>11}{'Area':>11}{'Angle 1':>11}{'Angle 2':>11}{'Angle 3':>11}")

for i in range(len(TriangleList)):
    angles = TriangleList[i].angles()
    print(f"{TriangleList[i].type():>12}{TriangleList[i].s1:>11.3f}{TriangleList[i].s2:>11.3f}{TriangleList[i].s3:>11.3f}{TriangleList[i].perimeter():>11.3f}{TriangleList[i].area():>11.3f}{angles[0]:>11.3f}{angles[1]:>11.3f}{angles[2]:>11.3f}")