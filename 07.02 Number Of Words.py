str = input("Enter a string: ")
spaceCount = 1

for char in str:
    if char == " ": spaceCount += 1

print("{} words".format(spaceCount))