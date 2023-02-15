count = 1
maximum = 0

while True:
    userNumber = int(input("Enter a Number (zero to quit): "))
    if maximum < userNumber:
        maximum = userNumber
        count = 1
    elif maximum == userNumber:
        count += 1

    if userNumber == 0:
        break

print("Maximum: {}".format(maximum))
print("Number of Occurrences: {}".format(count))