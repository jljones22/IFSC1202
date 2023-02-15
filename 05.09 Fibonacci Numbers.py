n = int(input("Enter Fibonnaci Sequence Number: "))

prevOne = 1
prevTwo = 0

while n - 1 > 0:
    sum = prevOne + prevTwo
    prevTwo = prevOne
    prevOne = sum
    n -= 1

print("Fibonacci Number: {}".format(sum))