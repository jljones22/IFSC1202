def percentChange(current, previous):
    return (current - previous) / previous * 100

stock = open("06.02 Stock.txt", "rt")
currentStock = stock.readline()
previousStock = 0

print("{:>9}{:>12}".format("Price", "Change"))
print("{:10}".format(float(currentStock)))

previousStock = currentStock
currentStock = stock.readline()

while currentStock != "":
    print("{:10.2f}{:10.2f}%".format(float(currentStock), float(percentChange(float(currentStock), float(previousStock)))))

    previousStock = currentStock
    currentStock = stock.readline()

stock.close()