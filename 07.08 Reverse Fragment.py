str = input("Enter a string: ")
strR = "".join(reversed(str))

str = str.replace(str[str.find('h'):str.rfind('h')], strR[strR.find('h'):str.rfind('h')])

print("{}".format(str))