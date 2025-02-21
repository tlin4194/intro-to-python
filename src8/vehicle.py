class Vehicle:
    def __init__(self, price, color):
        self.color = color
        self.price = price
        self.gas = 0

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas

    def beep(self):
        print("Boop")


class Truck(Vehicle):
    def __init__(self, price, color, tires):
        super().__init__(price, color)
        self.tires = tires

    def beep(self):
        print("Honk honk")


class Car(Vehicle):
    def __init__(self, price, color, speed):
        super().__init__(price, color)
        self.speed = speed

    def beep(self):
        print("Beep Beep")


c = Car(1000, "red", 50)
print(c.gasLeft())
c.fillUpTank()
print(c.gasLeft())
c.beep()

t = Truck(2000, "blue", 8)
print(t.tires)
t.beep()
