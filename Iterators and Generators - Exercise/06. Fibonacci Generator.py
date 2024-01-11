def fibonacci():
    num_1, num_2 = 0, 1
    while True:
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


generator = fibonacci()
for i in range(5):
    print(next(generator))
