FileA = open("06.05 CompareFileA.txt", "rt")
FileB = open("06.05 CompareFileB.txt", "rt")

lineA = FileA.readline()
lineB = FileB.readline()
lineN = 1
diff = 0

while lineA != "" and lineB != "":
    if lineA != lineB:
        print("Line: {} - File A: {}\nLine: {} - File B: {}".format(lineN, lineA, lineN, lineB))
        diff += 1
    lineN += 1
    lineA = FileA.readline()
    lineB = FileB.readline()

FileA.close()
FileB.close()

print("{} differences".format(diff))
