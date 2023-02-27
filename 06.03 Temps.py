def FahrToCel(F):
    return round(((float(F) - 32.0) * (5 / 9)), 1)

Ftemp = open("06.03 FTemps.txt", "rt")
Ctemp = open("06.03 CTemps.txt", "wt")

line = Ftemp.readline()
count = 0

while line != "":
    Ctemp.write(str(FahrToCel(line)) + '\n')
    line = Ftemp.readline()
    count += 1

Ftemp.close()
Ctemp.close()

print("{} records written".format(count))