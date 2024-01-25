class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        rented_dvds = [x.name for x in self.rented_dvds]
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join(rented_dvds)})"


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def convert_month(cls, month):
        months = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        return months.get(month, "Unknown Month")

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split(".")
        month = cls.convert_month(int(month))
        return cls(name, id, int(year), month, age_restriction)

    def __repr__(self):
        rented = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {rented}"


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = [x for x in self.dvds if x.id == dvd_id][0]
        customer = [x for x in self.customers if x.id == customer_id][0]
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return "DVD is already rented"
        elif customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        else:
            dvd.is_rented = True
            customer.rented_dvds.append(dvd)
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd = [x for x in self.dvds if x.id == dvd_id][0]
        customer = [x for x in self.customers if x.id == customer_id][0]
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += f"{customer.__repr__()}\n"
        for dvd in self.dvds:
            result += f"{dvd.__repr__()}\n"
        return result


c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)
