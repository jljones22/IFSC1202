firstNumber = int(input("Enter First Number: "))
secondNumber = int(input("Enter Second Number: "))
thirdNumber = int(input("Enter Third Number: "))

if firstNumber < secondNumber and firstNumber < thirdNumber:
    print(str(firstNumber), end=' ')
    if secondNumber < thirdNumber:
        print(str(secondNumber) + " " + str(thirdNumber))
    else:
        print(str(thirdNumber) + " " + str(secondNumber))
elif secondNumber < firstNumber and secondNumber < thirdNumber:
    print(str(secondNumber), end=' ')
    if firstNumber < thirdNumber:
        print(str(firstNumber) + " " + str(thirdNumber))
    else:
        print(str(thirdNumber) + " " + str(firstNumber))
else:
    print(str(thirdNumber), end=' ')
    if firstNumber < secondNumber:
        print(str(firstNumber) + " " + str(secondNumber))
    else:
        print(str(secondNumber) + " " + str(firstNumber))