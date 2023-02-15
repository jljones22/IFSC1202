count = 0
previousNumber = 0

while True:
    userNumber = int(input("Enter a Number (zero to quit): "))

    if userNumber > previousNumber and previousNumber != 0:
        count += 1

    if userNumber == 0:
        break

    previousNumber = userNumber

print("Number of Values Greater Than the Previous: {}".format(count))