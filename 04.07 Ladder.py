n = int(input("Enter N: "))

if n <= 9:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, sep="", end="")
        print("\n", end="")
else:
    exit()