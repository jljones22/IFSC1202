n = int(input("Enter Number: "))
sumOfCubes = 0

for i in range(1, n + 1):
    sumOfCubes += (i ** 3)

print(sumOfCubes)