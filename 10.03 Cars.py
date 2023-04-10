class Cars:
    def __init__(self, year, make):
        self.year = year
        self.make = make
        self.speed = 0

    def accelerate(self, value):
        self.speed += value
        print(f"{value:>6} {self.speed:>8}", end='')

    def brake(self, value):
        self.speed += value
        print(f"{value:>6} {self.speed:>8}", end='')

car = open("10.03 Cars.txt", "rt")
line = car.readline()

ls = line.strip().split(',')
cars = Cars(ls[0], ls[1])

line = car.readline()
print(f"Make:{cars.make}\nYear: {cars.year}\n\nChange    Speed")

while line != "":
    cars.accelerate(int(line)) if (int(line) > 0) else cars.brake(int(line))
    print()

    line = car.readline()

car.close()