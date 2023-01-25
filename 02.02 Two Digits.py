userNumber = int(input("Enter a Number: "))

print("Ones Digit: {}".format(userNumber % 10))
print("Tens Digit: {}".format(userNumber // 10))