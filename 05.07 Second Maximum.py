maximum = 0
secMaximum = 0

userNumber = int(input("Enter First Number: "))
maximum = userNumber
userNumber = int(input("Enter Second Number: "))

if maximum < userNumber:
    secMaximum = maximum
    maximum = userNumber
else:
    secMaximum = userNumber

while True:
    userNumber = int(input("Enter a Number (zero to quit): "))

    if maximum < userNumber:
        secMaximum = maximum
        maximum = userNumber

    if secMaximum < userNumber and maximum != userNumber:
        secMaximum = userNumber

    if userNumber == 0:
        break


print("First Maximum: {}".format(maximum))
print("Second Maximum: {}".format(secMaximum))