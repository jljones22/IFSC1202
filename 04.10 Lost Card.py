cards = int(input("Enter Number of Cards: "))
totalValue = 0
sum = 0

for i in range(1, cards + 1):
    totalValue += i

for i in range(cards - 1):
    sum += int(input("Enter Card: "))

print("Missing Card: {}".format(totalValue - sum))