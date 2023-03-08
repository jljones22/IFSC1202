str = input("Enter a string: ")
countF = 0

for char in str:
    if char == 'f':
        countF += 1

if countF == 1:
    print("{}".format(str.find('f')))
elif countF == 2:
    print("{} {}".format(str.find('f'), str.rfind('f')))
else:
    print(0)