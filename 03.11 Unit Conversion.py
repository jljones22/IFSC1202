fromValue = float(input("Enter From Value: "))
fromUnit = str(input("Enter From Unit (in, ft, yd, mi): "))

if fromUnit != "in" and fromUnit != "ft" and fromUnit != "yd" and fromUnit != "mi":
    print("{} is not valid".format(fromUnit))
    exit()

toUnit = str(input("Enter To Unit (in, ft, yd, mi): "))

if toUnit != "in" and toUnit != "ft" and toUnit != "yd" and toUnit != "mi":
    print("{} is not valid".format(toUnit))
    exit()

# in => in || ft || yd || mi

if fromUnit == "in" and toUnit == "in":
    print("{} in => {} in".format(fromValue, round(fromValue * 1.0, 7)))
elif fromUnit == "in" and toUnit == "ft":
    print("{} in => {} ft".format(fromValue, round(fromValue * 0.0833333333, 7)))
elif fromUnit == "in" and toUnit == "yd":
    print("{} in => {} yd".format(fromValue, round(fromValue * 0.0277777778, 7)))
elif fromUnit == "in" and toUnit == "mi":
    print("{} in => {} mi".format(fromValue, round(fromValue * 0.0000157828, 7)))

# ft => in || ft || yd || mi

elif fromUnit == "ft" and toUnit == "in":
    print("{} ft => {} in".format(fromValue, round(fromValue * 12.0, 7)))
elif fromUnit == "ft" and toUnit == "ft":
    print("{} ft => {} ft".format(fromValue, round(fromValue * 1.0, 7)))
elif fromUnit == "ft" and toUnit == "yd":
    print("{} ft => {} yd".format(fromValue, round(fromValue * 0.3333333333, 7)))
elif fromUnit == "ft" and toUnit == "mi":
    print("{} ft => {} mi".format(fromValue, round(fromValue * 0.0001893939, 7)))

# yd => in || ft || yd || mi

elif fromUnit == "yd" and toUnit == "in":
    print("{} yd => {} in".format(fromValue, round(fromValue * 36.0, 7)))
elif fromUnit == "yd" and toUnit == "ft":
    print("{} yd => {} ft".format(fromValue, round(fromValue * 3.0, 7)))
elif fromUnit == "yd" and toUnit == "yd":
    print("{} yd => {} yd".format(fromValue, round(fromValue * 1.0, 7)))
elif fromUnit == "yd" and toUnit == "mi":
    print("{} yd => {} mi".format(fromValue, round(fromValue * 0.0005681818, 7)))

# mi => in || ft || yd || mi

elif fromUnit == "mi" and toUnit == "in":
    print("{} mi => {} in".format(fromValue, round(fromValue * 63360.0, 7)))
elif fromUnit == "mi" and toUnit == "ft":
    print("{} mi => {} ft".format(fromValue, round(fromValue * 5280.0, 7)))
elif fromUnit == "mi" and toUnit == "yd":
    print("{} mi => {} yd".format(fromValue, round(fromValue * 1760.0, 7)))
elif fromUnit == "mi" and toUnit == "mi":
    print("{} mi => {} mi".format(fromValue, round(fromValue * 1.0, 7)))