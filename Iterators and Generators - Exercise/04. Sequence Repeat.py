class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration

        current_element = self.sequence[self.index]
        self.index = (self.index + 1) % len(self.sequence)
        self.number -= 1

        return current_element

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

