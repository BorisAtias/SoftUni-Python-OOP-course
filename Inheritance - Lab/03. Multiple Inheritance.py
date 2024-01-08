class Person:
    def __init__(self):
        pass

    def sleep(self):
        return "sleeping..."

class Employee:
    def __init__(self):
        pass

    def get_fired(self):
        return "fired..."

class Teacher(Person, Employee):
    def __init__(self):
        pass

    def teach(self):
        return 'teaching...'