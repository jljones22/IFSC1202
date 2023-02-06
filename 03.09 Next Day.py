month = int(input("Enter Month: "))
day = int(input("Enter Day: "))

if month == 2:
    if day == 28:
        print("3/1")
    else:
        print(str(month) + "/" + str(day + 1))
elif (month == 4 or month == 6 or month == 9 or month == 11):
    if day == 30:
        print(str(month + 1) + "/1")
    else:
        print(str(month) + "/" + str(day + 1))
else:
    if day == 31:
        if month == 12:
          print("1/1")
        else:
            print(str(month + 1) + "/1")
    else:
        print(str(month) + "/" + str(day + 1))