sum = 0

while True:
    userNumber = int(input("Enter a Number (zero to quit): "))
    sum += userNumber
    if userNumber == 0:
        break
print("Sum: {}".format(sum))