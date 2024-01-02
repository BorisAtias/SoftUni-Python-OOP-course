def number_increment(numbers):
    def decorator(func):
        def wrapper():
            result = func()
            return [num + 1 for num in result]
        return wrapper()
    @decorator
    def increase():
        return numbers

    return increase

print(number_increment([1, 2, 3]))
