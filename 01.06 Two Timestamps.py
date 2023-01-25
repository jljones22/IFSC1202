print("First Timestamp")

hoursA = int(input("Enter Hours: "))
minutesA = int(input("Enter Minutes: "))
secondsA = int(input("Enter Seconds: "))

print("Second Timestamp")

hoursB = int(input("Enter Hours: "))
minutesB = int(input("Enter Minutes: "))
secondsB = int(input("Enter Seconds: "))

print(str((hoursB * 3600 + minutesB * 60 + secondsB) - (hoursA * 3600 + minutesA * 60 + secondsA)))