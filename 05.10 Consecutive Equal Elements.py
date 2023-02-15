maximum = 0
previous = 0

while True:
    userNumber = int(input("Enter a Number (zero to quit): "))

    if previous == userNumber:
        consec = userNumber
        amount = count + 1

    if maximum < userNumber:
        maximum = userNumber
        count = 1

    previous = userNumber

    if userNumber == 0:
        break

print("{} repeated {} times".format(consec, amount))