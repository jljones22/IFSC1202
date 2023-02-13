count = 0

while True:
    userNumber = int(input("Enter a Number (zero to quit): "))
    if userNumber % 2 == 0 and userNumber != 0:
        count += 1

    if userNumber == 0:
        break

print("Number of Even Values: {}".format(count))