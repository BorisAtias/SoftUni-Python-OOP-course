class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.curr_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        num = self.curr_count
        self.curr_count += self.step
        self.count -= 1
        return num

numbers = take_skip(2, 6)
for number in numbers:
    print(number)

