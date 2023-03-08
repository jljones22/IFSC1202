str = input("Enter a string: ")
firstHalf = ""
secondHalf = ""

if len(str) % 2 != 0:
    firstHalf = str[:((len(str) // 2 + 1))]
    secondHalf = str[((len(str) // 2) + 1):]
else:
    firstHalf = str[:(len(str) // 2)]
    secondHalf = str[(len(str) // 2):]

print("{}{}".format(secondHalf, firstHalf))