n = int(input("Enter N: "))

if n > 1:
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            print("COMPOSITE")
            break
        else:
            print("PRIME")
            break
else:
    exit()