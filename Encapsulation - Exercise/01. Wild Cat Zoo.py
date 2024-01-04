class Animal:
    def __init__(self, name: str, gender: str, age: int, money_for_care: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Lion(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, 50)


class Tiger(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, 45)


class Cheetah(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, 60)


class Worker:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Keeper(Worker):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age, salary)


class Caretaker(Worker):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age, salary)


class Vet(Worker):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age, salary)


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget:
            if len(self.animals) < self.__animal_capacity:
                self.animals.append(animal)
                self.__budget -= price
                animal_type = animal.__class__.__name__
                return f"{animal.name} the {animal_type} added to the zoo"
            else:
                return "Not enough space for animal"
        return "Not enough budget"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            worker_type = worker.__class__.__name__
            self.workers.append(worker  )
            return f"{worker.name} the {worker_type} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for name in self.workers:
            if worker_name in name.name:
                self.workers.remove(name)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = sum(worker.salary for worker in self.workers)
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_animal_tend = sum(animal.money_for_care for animal in self.animals)
        if self.__budget >= total_animal_tend:
            self.__budget -= total_animal_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        total_animals_count = len(self.animals)
        lions_count = sum(1 for animal in self.animals if animal.__class__.__name__ == "Lion")
        tigers_count = sum(1 for animal in self.animals if animal.__class__.__name__ == "Tiger")
        cheetah_count = sum(1 for animal in self.animals if animal.__class__.__name__ == "Cheetah")
        lion_string = "\n".join(str(animal) for animal in self.animals if animal.__class__.__name__ == "Lion")
        tiger_string = "\n".join(str(animal) for animal in self.animals if animal.__class__.__name__ == "Tiger")
        cheetah_string = "\n".join(str(animal) for animal in self.animals if animal.__class__.__name__ == "Cheetah")

        final_string = f"You have {total_animals_count} animals\n"
        final_string += f"----- {lions_count} Lions:\n{lion_string}\n"
        final_string += f"----- {tigers_count} Tigers:\n{tiger_string}\n"
        final_string += f"----- {cheetah_count} Cheetahs:\n{cheetah_string}\n"

        return final_string.rstrip()

    def workers_status(self):
        total_workers_count = len(self.workers)
        caretakers_count = sum(1 for worker in self.workers if worker.__class__.__name__ == "Caretaker")
        keepers_count = sum(1 for worker in self.workers if worker.__class__.__name__ == "Keeper")
        vets_count = sum(1 for worker in self.workers if worker.__class__.__name__ == "Vet")
        caretaker_string = "\n".join(str(worker) for worker in self.workers if worker.__class__.__name__ == "Caretaker")
        keepers_string = "\n".join(str(worker) for worker in self.workers if worker.__class__.__name__ == "Keeper")
        vets_string = "\n".join(str(worker) for worker in self.workers if worker.__class__.__name__ == "Vet")

        final_string = f"You have {total_workers_count} workers\n"
        final_string += f"----- {keepers_count} Keepers:\n{keepers_string}\n"
        final_string += f"----- {caretakers_count} Caretakers:\n{caretaker_string}\n"
        final_string += f"----- {vets_count} Vets:\n{vets_string}\n"

        return final_string.rstrip()



zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
