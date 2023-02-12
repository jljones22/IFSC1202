A = int(input("Enter A: "))
B = int(input("Enter B: "))

for i in range(A, B + 1):
    flag = 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            flag = 0
            break
    if flag == 1:
        print(i)