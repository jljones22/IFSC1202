class RetailItem:
    def __init__(self, description = "", unitOnHand = 0, price = 0):
        self.description = description
        self.unitOnHand = unitOnHand
        self.price = price

    def inventoryValue(self):
        return float(self.unitOnHand) * self.price

def printInventory(ls):
    print("{:>11} {:>20} {:>20} {:>20}".format("Description", "Units On Hand", "Price", "Inventory Value"))
    for item in range(len(ls)):
        print(f"{item.description:>11} {item.unitOnHand:>20} {item.price:>20} {item.inventoryValue():>20.2f}")


inventory = open("10.02 Inventory.txt", "rt")
line = inventory.readline()

p = []

while line != "":
    ls = line.strip().split(',')
    p.append(ls)

    line = inventory.readline()

for i in range(len(p)):
    match p[i][0]:
        case 'Jacket':
            jacket.description = p[i][0]
            jacket.unitOnHand = p[i][1]
            jacket.price = float(p[i][2])
        case 'Jeans':
            jeans.description = p[i][0]
            jeans.unitOnHand = p[i][1]
            jeans.price = float(p[i][2])
        case 'Shirt':
            shirt.description = p[i][0]
            shirt.unitOnHand = p[i][1]
            shirt.price = float(p[i][2])

print("{:>11} {:>20} {:>20} {:>20}".format("Description", "Units On Hand", "Price", "Inventory Value"))
print(f"{jacket.description:>11} {jacket.unitOnHand:>20} {jacket.price:>20} {jacket.inventoryValue():>20.2f}")
print(f"{jeans.description:>11} {jeans.unitOnHand:>20} {jeans.price:>20} {jeans.inventoryValue():>20.2f}")
print(f"{shirt.description:>11} {shirt.unitOnHand:>20} {shirt.price:>20} {shirt.inventoryValue():>20.2f}")