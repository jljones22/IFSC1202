ELInput = open("06.04 EmptyLinesInput.txt", "rt")
ELOutput = open("06.04 EmptyLinesOutput.txt", "wt")

line = ELInput.readline()

readCount = 0
writeCount = 0

while line != "":
    if line != '\n':
        ELOutput.write(line)
        writeCount += 1
    readCount += 1
    line = ELInput.readline()

ELInput.close()
ELOutput.close()

print("{} records read\n{} records written".format(readCount, writeCount))
    