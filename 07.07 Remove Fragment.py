str = input("Enter a string: ")

for i in range(str.find('h'), str.rfind('h')):
    str = str.replace(str[i], ' ')

for char in str:
    if char == ' ':
        str = str.replace(char, '')

print("{}".format(str))