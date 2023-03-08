str = input("Enter a string: ")
countF = str.count('f')

if countF == 1:
    print("One f")
elif countF == 2:
    print("{}".format(str.rfind('f')))
else:
    print("Zero f")