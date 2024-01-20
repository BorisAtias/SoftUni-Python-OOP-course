from abc import ABC, abstractmethod


class User:
    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating = 0
        self.is_blocked = False

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if not value.strip():
            raise ValueError("First name cannot be empty")
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not value.strip():
            raise ValueError("Last name cannot be empty")
        self.__last_name = value

    @property
    def driving_license_number(self):
        return self.__driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        if not value.strip():
            raise ValueError("Driving license number is required!")
        self.__driving_license_number = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError("Users rating cannot be negative!")

        self.__rating = value

    def increase_rating(self):
        self.rating += 0.5
        if self.rating > 10:
            self.rating = 10

    def decrease_rating(self):
        if self.rating - 2 < 0:
            self.rating = 0
            self.is_blocked = True

        else:
            self.rating -= 2

    def __str__(self):
        return f"{self.first_name} {self.last_name} Driving license: {self.driving_license_number}  Rating: {self.rating}"


class BaseVehicle(ABC):
    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level = 100
        self.is_damaged = False

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if not value.strip():
            raise ValueError("Brand cannot be empty!")
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model cannot be empty!")
        self.__model = value

    @property
    def license_plate_number(self):
        return self.__license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value):
        if not value.strip():
            raise ValueError("License plate number is required!")
        self.__license_plate_number = value

    @abstractmethod
    def drive(self, mileage: float):
        pass

    def recharge(self):
        self.battery_level = 100

    def change_status(self):
        self.is_damaged = not self.is_damaged

    def __str__(self):
        status = "OK" if not self.is_damaged else "Damaged"
        return f"{self.brand} {self.model} License plate: {self.license_plate_number} Battery: {self.battery_level}% Status: {status}"


class PassengerCar(BaseVehicle):
    MAX_MILAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, PassengerCar.MAX_MILAGE)

    def drive(self, mileage: float):
        percentage = mileage / PassengerCar.MAX_MILAGE
        self.battery_level -= round(percentage * 100)


class CargoVan(BaseVehicle):
    MAX_MILAGE = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, CargoVan.MAX_MILAGE)

    def drive(self, mileage: float):
        percentage = mileage / CargoVan.MAX_MILAGE
        self.battery_level -= round(percentage * 100)
        self.battery_level -= 5


class Route:
    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        self.start_point = start_point
        self.end_point = end_point
        self.length = length
        self.route_id = route_id
        self.is_locked = False

    @property
    def start_point(self):
        return self.__start_point

    @start_point.setter
    def start_point(self, value):
        if not value.strip():
            raise ValueError("Start point cannot be empty!")
        self.__start_point = value

    @property
    def end_point(self):
        return self.__end_point

    @end_point.setter
    def end_point(self, value):
        if not value.strip():
            raise ValueError("End point cannot be empty!")
        self.__end_point = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value < 1.00:
            raise ValueError("Length cannot be less than 1.00 kilometer!")
        self.__length = value


class ManagingApp:
    VALID_VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def find_user(self, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return user
        return None

    def find_vehicle(self, license_plate_number: str):
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return vehicle

    def find_route(self, route_id: int):
        for route in self.routes:
            if route.route_id == route_id:
                return route

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self.find_user(driving_license_number)
        if user:
            return f"{driving_license_number} has already been registered to our platform."
        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        vehicle = self.find_vehicle(license_plate_number)
        if vehicle_type not in ManagingApp.VALID_VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = ManagingApp.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}"

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                elif route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                elif route.length > length:
                    route.is_locked = True

        route_id = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        user = self.find_user(driving_license_number)
        vehicle = self.find_vehicle(license_plate_number)
        route = self.find_route(route_id)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        return vehicle.__str__()

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        damaged_vehicles.sort(key=lambda v: (v.brand, v.model))
        repaired_vehicles = damaged_vehicles[:count]
        for v in repaired_vehicles:
            v.is_damaged = False
            v.recharge()
        return f"{len(repaired_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        users = sorted(self.users, key=lambda u: u.rating, reverse=True)
        return "*** E-Drive-Rent ***\n" + "\n".join([u.__str__() for u in users])


app = ManagingApp()

print(app.register_user( 'Tisha', 'Reenie', '7246506' ))

print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))

print(app.register_user( 'Mack', 'Cindi', '7246506'))

print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))

print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))

print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))

print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))

print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))

print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))

print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))

print(app.allow_route('SOF', 'PLD', 144))

print(app.allow_route('BUR', 'VAR', 87))

print(app.allow_route('BUR', 'VAR', 87))

print(app.allow_route('SOF', 'PLD', 184))

print(app.allow_route('BUR', 'VAR', 86.999))

print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))

print(app.make_trip('7246506', 'CWP8032', 1, True))

print(app.make_trip('7246506', 'COUN199728', 1, False))

print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))

print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))

print(app.repair_vehicles(2))

print(app.repair_vehicles(20))

print(app.users_report())