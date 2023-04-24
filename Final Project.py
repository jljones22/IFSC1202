class VendingItem:
    def __init__(self, name, initialCount, costPerItem):
        self.name = name
        self.initialCount = int(initialCount)
        self.costPerItem = float(costPerItem)
        self.soldCount = 0
        self.lostCount = 0

    def initialValue(self): return self.initialCount * self.costPerItem
    def soldValue(self): return self.soldCount * self.costPerItem
    def lostValue(self): return self.lostCount * self.costPerItem

class Vending:
    def __init__(self):
        self.vendingList = []
        self.vendingTotalInitialValue = 0
        self.vendingTotalInitialCount = 0
        self.vendingTotalSoldValue = 0
        self.vendingTotalSoldCount = 0
        self.vendingTotalLostValue = 0
        self.vendingTotalLostCount = 0

    def loadVendingItemsFromFile(self, filename):
        vendingMachine = open(filename)
        line = vendingMachine.readline()

        while line != "":
            ls = line.split()
            vendingItem = VendingItem(ls[0], ls[1], ls[2])

            self.vendingTotalInitialValue += vendingItem.initialValue()
            self.vendingTotalInitialCount += vendingItem.initialCount

            self.vendingList.append(vendingItem)
            line = vendingMachine.readline()
        
        vendingMachine.close()

    def printVending(self):
        print(f"{'':10}{'Initial':10}{'Price':10}{'Initial':10}{'Sold':10}{'Sold':10}{'Lost':10}{'Lost':10}")
        print(f"{'Product':10}{'Count':10}{'Per Item':10}{'Value':10}{'Count':10}{'Value':10}{'Count':10}{'Value':10}\n")

        for i in range(len(self.vendingList)):
            print(f"{self.vendingList[i].name:10}{self.vendingList[i].initialCount:<10}{self.vendingList[i].costPerItem:<10.2f}{self.vendingList[i].initialValue():<10.2f}{self.vendingList[i].soldCount:<10}{self.vendingList[i].soldValue():<10.2f}{self.vendingList[i].lostCount:<10}{self.vendingList[i].lostValue():<10.2f}")

        print(f"\n{'Total':10}{self.vendingTotalInitialCount:<10}{'':10}{self.vendingTotalInitialValue:<10.2f}{self.vendingTotalSoldCount:<10}{self.vendingTotalSoldValue:<10.2f}{self.vendingTotalLostCount:<10}{self.vendingTotalLostValue:<10.2f}")


    def findProduct(self, productToFind):
        for i in range(len(self.vendingList)):
            if self.vendingList[i].name == productToFind: return i
        else: return -1

    def updateVending(self, productName):
        index = self.findProduct(productName)
        assert index != -1, "Product Not Found"

        if self.vendingList[index].soldCount < self.vendingList[index].initialCount:
            self.vendingList[index].soldCount += 1
            self.vendingTotalSoldCount += 1
            self.vendingTotalSoldValue += self.vendingList[index].costPerItem
        else:
            self.vendingList[index].lostCount += 1
            self.vendingTotalLostCount += 1
            self.vendingTotalLostValue += self.vendingList[index].costPerItem

vending = Vending()
vending.loadVendingItemsFromFile("Final Project Vending.txt")

Sales = open("Final Project Sales.txt")
line = Sales.readline()

while line != "":
    vending.updateVending(line.replace('\n', ''))

    line = Sales.readline()

Sales.close()

vending.printVending()