class RetailItem:
    def __init__(self, description = "", unitOnHand = 0, price = 0):
        self.description = description
        self.unitOnHand = unitOnHand
        self.price = price

    def inventoryValue(self):
        return float(self.unitOnHand) * self.price

def printInventory(ls):
    print("{:>11} {:>20} {:>20} {:>20}".format("Description", "Units On Hand", "Price", "Inventory Value"))

    for i in range(len(ls)):
        print(f"{ls[i].description:>11} {ls[i].unitOnHand:>20} {ls[i].price:>20} {ls[i].inventoryValue():>20.2f}")
    print('\n', end='')

def findInventory(ls, itemName):
    for i in range(len(ls)):
        if ls[i].description == itemName: return i
    else: return -1

inventory = open("11.01 Inventory.txt", "rt")
line = inventory.readline()

ril = []

while line != "":
    ls = line.strip().split(',')
    
    ri = RetailItem(ls[0], int(ls[1]), float(ls[2]))
    ril.append(ri)

    line = inventory.readline()

inventory.close()
printInventory(ril)

inventory = open("11.01 InventoryUpdate.txt", "rt")
line = inventory.readline()

while line != "":
    ls = line.strip().split(',')

    index = findInventory(ril, ls[0])
    if (not index < 0): ril[index].price = float(ls[1])

    line = inventory.readline()

inventory.close()
printInventory(ril)