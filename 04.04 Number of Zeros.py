n = int(input("Enter N: "))
countZero = 0

for i in range(n):
    if int(input("Enter Number: ")) == 0:
        countZero += 1

print("Number of Zeros: {}".format(countZero))