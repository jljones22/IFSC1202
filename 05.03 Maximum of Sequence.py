max = 0

while True:
    userNumber = int(input("Enter a Number (zero to quit): "))
    if max < userNumber:
        max = userNumber

    if userNumber == 0:
        break
print("Maximum: {}".format(max))