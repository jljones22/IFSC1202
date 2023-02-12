A = int(input("Enter A: "))
B = int(input("Enter B: "))

for i in range(A, B + 1):
    print("{}*{}={}".format(i, i, i * i))