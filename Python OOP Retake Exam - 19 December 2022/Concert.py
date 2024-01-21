from abc import ABC, abstractmethod


class Musician(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Musician name cannot be empty!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")
        self.__age = value

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.valid_skills:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."

    @property
    @abstractmethod
    def valid_skills(self):
        pass

    def __repr__(self):
        return f"Name: {self.name}\nAge: {self.age}\nSkills: {', '.join(self.skills)}"


class Singer(Musician):
    @property
    def valid_skills(self):
        return ["sing high pitch notes", "sing low pitch notes"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def learn_new_skill(self, new_skill: str):
        if new_skill not in ["sing high pitch notes", "sing low pitch notes"]:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."


class Drummer(Musician):
    @property
    def valid_skills(self):
        return ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def learn_new_skill(self, new_skill: str):
        if new_skill not in ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."


class Guitarist(Musician):
    @property
    def valid_skills(self):
        return ["play metal", "play rock", "play jazz"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def learn_new_skill(self, new_skill: str):
        if new_skill not in ["play metal", "play rock", "play jazz"]:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."


class Band:
    def __init__(self, name: str):
        self.name = name
        self.members = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Band name should contain at least one character!")
        self._name = value

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."



class Concert:
    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    def __str__(self):
        return f"{self.genre} concert at {self.place}."

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        if value not in ["Metal", "Rock", "Jazz"]:
            raise ValueError(f"Our group doesn't play {value}!")
        self.__genre = value

    @property
    def audience(self):
        return self.__audience

    @audience.setter
    def audience(self, value):
        if value < 1:
            raise ValueError("At least one person should attend the concert!")
        self.__audience = value

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        if value < 1.0:
            raise ValueError("Ticket price must be at least 1.00$!")
        self.__ticket_price = value

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0.00:
            raise ValueError("Expenses cannot be a negative number!")
        self.__expenses = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        if len(value) < 2 or not value.strip():
            raise ValueError("Place must contain at least 2 chars. It cannot be empty!")
        self.__place = value

    def get_profit(self):
        return self.audience * self.ticket_price - self.expenses


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Singer": Singer, "Drummer": Drummer, "Guitarist": Guitarist}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def find_musician_by_name(self, name):
        return next((m for m in self.musicians if m.name == name), None)

    def find_band_by_name(self, name):
        return next((b for b in self.bands if b.name == name), None)

    def find_concert_by_place(self, place):
        return next((c for c in self.concerts if c.place == place), None)

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        if self.find_musician_by_name(name):
            raise Exception(f"{name} is already a musician!")
        musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if self.find_band_by_name(name):
            raise Exception(f"{name} band is already created!")
        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if self.find_concert_by_place(place):
            raise Exception(f"{place} is already registered for {genre} concert!")
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.find_musician_by_name(musician_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        band = self.find_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.find_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        musician = self.find_musician_by_name(musician_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self.find_band_by_name(band_name)
        concert = self.find_concert_by_place(concert_place)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        if not concert:
            raise Exception(f"{concert_place} isn't a concert!")

        has_singer = any(isinstance(member, Singer) for member in band.members)
        has_drummer = any(isinstance(member, Drummer) for member in band.members)
        has_guitarist = any(isinstance(member, Guitarist) for member in band.members)

        if not (has_singer and has_drummer and has_guitarist):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        needed_skills = {"Rock": ["play the drums with drumsticks", "sing high pitch notes", "play rock"],
                         "Metal": ["play the drums with drumsticks", "sing low pitch notes", "play metal"],
                         "Jazz": ["play the drums with drum brushes", "sing high pitch notes", "sing low pitch notes",
                                  "play jazz"]}

        for skill in needed_skills[concert.genre]:
            if not any(skill in member.skills for member in band.members):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.get_profit()
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."


musician_types = ["Singer", "Drummer", "Guitarist"]

names = ["George", "Alex", "Lilly"]

app = ConcertTrackerApp()

for i in range(3):
    print(app.create_musician(musician_types[i], names[i], 20))

print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[2].learn_new_skill("play rock"))
print(app.create_band("RockName"))

for i in range(3):
    print(app.add_musician_to_band(names[i], "RockName"))

print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))
print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", "RockName"))
