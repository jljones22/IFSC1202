n = int(input("Enter N: "))
flag = True

if n > 1:
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            flag = False
        
if flag == True:
    print("PRIME")
else:
    print("COMPOSITE")