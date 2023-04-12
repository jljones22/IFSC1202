class Student:
    def __init__(self, firstName, lastName, tNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.tNumber = tNumber
        self.grades = scores

    def runningAverage(self):
        sum = 0
        skip = 0
        for i in range(len(self.grades)):
            if self.grades[i] != 0.0:
                sum += int(self.grades[i])
            else: skip += 1
        return sum / (len(self.grades) - skip)

    def totalAverage(self):
        sum = 0
        for i in range(len(self.grades)):
            if self.grades[i] != "":
                sum += int(self.grades[i])
        return sum / len(self.grades)

    def letterGrade(self):
        totalAvg = self.totalAverage()
        if totalAvg >= 90: return 'A'
        elif totalAvg >= 80: return 'B'
        elif totalAvg >= 70: return 'C'
        elif totalAvg >= 60: return 'D'
        else: return 'F'

students = open("10.04 StudentScores.txt", "rt")
line = students.readline()

print(f"{'First':>12} {'Last':>12} {'ID':>12} {'Running':>12} {'Semester':>12} {'Letter':>12}")
print(f"{'Name':>12} {'Name':>12} {'Number':>12} {'Average':>12} {'Average':>12} {'Grade':>12}")
print(f"{'------------':>12} " * 6)

while line != "":
    ls = line.strip().split(',')
    grades = []
    for i in range(3, len(ls)):
        if ls[i] == "":
            grades.append(0.0)
        else:
            grades.append(float(ls[i]))
    student = Student(ls[0], ls[1], ls[2], grades)

    print(f"{student.firstName:>12} {student.lastName:>12} {student.tNumber:>12} {student.runningAverage():>12.2f} {student.totalAverage():>12.2f} {student.letterGrade():>12}")

    line = students.readline()