class Vehicle():
    gas_tank_size = 100

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        self.gas_amount = self.gas_tank_size

    def fuel_up(self):
        self.gas_amount = self.gas_tank_size

    def use_fuel(self):
        if self.gas_amount > 10:
            self.gas_amount -= 10


class Car(Vehicle):
    gas_tank_size = 100

    def __init__(self, color, brand):
        super().__init__(color, brand)

    def __str__(self):
        return f"This car is {self.color} from {self.brand}. Gas left: {self.gas_amount}"


class Truck(Vehicle):
    gas_tank_size = 200

    def __init__(self, color, brand, boxes=0):
        super().__init__(color, brand)
        self.boxes = boxes

    def __str__(self):
        return f"This truck is {self.color} from {self.brand}. Gas left: {self.gas_amount}. Boxes: {self.boxes}"

    def load_box(self):
        self.boxes += 1

    def use_fuel(self):
        if self.gas_amount > 20:
            self.gas_amount -= 20


my_car = Car("pink", "Lexus")
print(my_car)
my_car.use_fuel()
my_car.use_fuel()
print(my_car)

t = Truck("red", "Toyota")
print(t)
t.load_box()
t.load_box()
t.use_fuel()
print(t)
