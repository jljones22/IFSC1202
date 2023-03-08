def properCase(s):
    return s.title()

def removeNewLine(s):
    return s.replace('\n', '')

def trim(s):
    return s.strip()

def firstName(s):
    return properCase(s[:s.find(' ')])

def lastName(s):
    return properCase(s[s.rfind(' '):])

def middleName(s):
    str = s[s.find(' '):s.rfind(' ') + 1]
    return properCase(trim(str)) if len(str) != 3 else properCase(trim(str[::-1].replace(' ', '.', 1)[::-1]))

print("{:10} {:10} {:10}\n{:10} {:10} {:10}".format("First", "Middle", "Last", "----------", "----------", "----------"))

names = open("07.11 Names.txt", "rt")
name = names.readline()

while name != "":
    name = trim(removeNewLine(name))
    print("{:10} {:10} {:10}".format(firstName(name), middleName(name), lastName(name)))
    name = names.readline()

names.close()