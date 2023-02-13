sum = 0
count = 0

while True:
    userNumber = int(input("Enter a Number (zero to quit): "))
    sum += userNumber
    if userNumber == 0:
        break
    count += 1

if count != 0:
    print("Average: {}".format(sum / count))
else:
    print("Sequence Length is 0")