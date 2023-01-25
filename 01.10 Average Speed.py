lengthOfRace = int(input("Enter Length of Race in Kilometers: "))
numMinutes = int(input("Enter Minutes: "))
numSeconds = int(input("Enter Seconds: "))

print(str((lengthOfRace / 1.61) / ((numMinutes + (numSeconds / 60)) / 60)))