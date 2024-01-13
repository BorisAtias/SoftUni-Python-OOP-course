class vowels:
    def __init__(self, my_string):
        self.my_string = my_string
        self.vowels = ["a","e","i","o","u"]
        self.start_index = -1
        self.end_index = len(self.my_string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start_index += 1

        if self.start_index > self.end_index:
            raise StopIteration
        curr_char = self.my_string[self.start_index]
        if curr_char.lower() in self.vowels:
            return curr_char

        return self.__next__()





my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
