def isEven(num):
    return int(num) % 2 == 0

def isOdd(num):
    return not isEven(num)

def isPrime(num):
    flag = True
    
    if int(num) > 1:
        for i in range(2, (int(num) // 2) + 1):
            if int(num) % i == 0:
                flag = False
    else: return False
    return flag

numbers = open("06.06 Numbers.txt", "rt")
evenNums = open("06.06 Evennumbers.txt", "wt")
oddNums = open("06.06 Oddnumbers.txt", "wt")
primeNums = open("06.06 Primenumbers.txt", "wt")

numC = 0
numE = 0
numO = 0
numP = 0

line = numbers.readline()

while line != "":
    if isEven(line):
        evenNums.write(line)
        numE += 1
    if isOdd(line):
        oddNums.write(line)
        numO += 1
    if isPrime(line):
        primeNums.write(line)
        numP += 1
    line = numbers.readline()
    numC += 1
    
numbers.close()
evenNums.close()
oddNums.close()
primeNums.close()

print("{} even numbers\n{} odd numbers\n{} prime numbers\n{} numbers read".format(numE, numO, numP, numC))