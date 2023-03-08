str = input("Enter a string: ")
sep = str.find(" ") + 1

print("{} {}".format(str[sep:], str[:sep - 1]))