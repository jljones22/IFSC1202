n = int(input("Enter N: "))
factorialResult = 1
sumOfFactorial = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        factorialResult *= j
    sumOfFactorial += factorialResult
    factorialResult = 1

print("Sum of Factorials: {}".format(sumOfFactorial))