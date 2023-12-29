class Vehicle:
    def __init__(self, mileage: int, max_speed: int = 150):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []

    def add_gadget(self, gadget: str):
        self.gadgets.append(gadget)

car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
