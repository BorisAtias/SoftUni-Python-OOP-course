class dictionary_iter:
    def __init__(self, my_dict):
        self.my_dict = list(my_dict.items())
        self.start_index = - 1
        self.end_index = len(my_dict) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start_index += 1
        if self.start_index > self.end_index:
            raise StopIteration
        key, value = self.my_dict[self.start_index]
        return key, value



result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

