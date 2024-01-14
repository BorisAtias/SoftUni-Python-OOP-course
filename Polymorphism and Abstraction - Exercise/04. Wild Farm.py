from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def __init__(self, quantity):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Meat(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Seed(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Animal(ABC):

    @abstractmethod
    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @property
    @abstractmethod
    def gained_weight(self):
        pass

    @property
    @abstractmethod
    def food_that_eats(self):
        pass

    def feed(self, food):
        if type(food) not in self.food_that_eats:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.gained_weight
        self.food_eaten += food.quantity


class Bird(Animal, ABC):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25


class Hen(Bird):

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def food_that_eats(self):
        return [Meat, Fruit, Vegetable, Seed]

    @property
    def gained_weight(self):
        return 0.35


class Mouse(Mammal):

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self):
        return 0.10


class Dog(Mammal):

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40


class Cat(Mammal):

    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def food_that_eats(self):
        return [Vegetable, Meat]

    @property
    def gained_weight(self):
        return 0.30


class Tiger(Mammal):

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1.00
owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)




