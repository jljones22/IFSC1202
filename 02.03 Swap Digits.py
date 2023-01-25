userNumber = int(input("Enter a Number: "))
swapNumber = (userNumber % 10) * 10 + (userNumber // 10)

print("Swapped Number: {}".format(swapNumber))