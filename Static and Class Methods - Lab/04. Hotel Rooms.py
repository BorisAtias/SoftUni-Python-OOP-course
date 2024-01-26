class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        if not self.is_taken and people <= self.capacity:
            self.guests = people
            self.is_taken = True
        else:
            return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
        else:
            return f"Room number {self.number} is not taken"


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0


    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                res = room.take_room(people)
                if res is None:
                    self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()

    def status(self):
        free_rooms = []
        taken_rooms = []
        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(str(room.number))
            else:
                free_rooms.append(str(room.number))

        status = f"Hotel {self.name} has {self.guests} total guests\n"
        status += f"Free rooms: {', '.join(free_rooms)}\n"
        status += f"Taken rooms: {', '.join(taken_rooms)}"

        return status


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())
