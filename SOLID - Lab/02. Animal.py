from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self) -> str:
        return "woof-woof!"


class Cat(Animal):
    def make_sound(self) -> str:
        return "meow"


class Turtle(Animal):
    def make_sound(self) -> str:
        return "turtle sound"


class Chicken(Animal):
    def make_sound(self) -> str:
        return "chicken sound"


class Pig(Animal):
    def make_sound(self) -> str:
        return "pig sound"
def animal_sound(animals: List[Animal]) -> None:
    for animal in animals:
        print(animal.make_sound())



animals = [Dog(), Cat(), Turtle(), Chicken(), Pig()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
