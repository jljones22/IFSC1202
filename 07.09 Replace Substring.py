str = input("Enter a string: ")

for char in str:
    if char == '1':
        str = str.replace('1', "one")

print("{}".format(str))