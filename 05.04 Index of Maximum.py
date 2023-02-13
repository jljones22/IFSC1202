max = 0
index = 1
count = 1

while True:
    userNumber = int(input("Enter a Number (zero to quit): "))
    if max < userNumber:
        max = userNumber
        index = count

    if userNumber == 0:
        break
    count += 1

if max == 0:
    index = 0

print("Maximum: {}".format(max))
print("Index of Maximum: {}".format(index))