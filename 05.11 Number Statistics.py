userNumber = float(input("Enter a Value (zero to quit): "))

count = 1
sum = userNumber
minimum = userNumber
maximum = userNumber

while True:
    
    if userNumber == 0:
        break

    userNumber = float(input("Enter a Value (zero to quit): "))

    if maximum < userNumber:
        maximum = userNumber

    if minimum > userNumber and userNumber != 0:
        minimum = userNumber
   
    if userNumber != 0:
        count += 1
        sum += userNumber

print("Count:   {}".format(count))
print("Sum:     {}".format(sum))
print("Average: {}".format(sum / count))
print("Minimum: {}".format(minimum))
print("Maximum: {}".format(maximum))
