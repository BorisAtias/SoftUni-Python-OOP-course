def logged(func):
    def wrapper(*args):
        result = func(*args)

        return (f"you called {func.__name__}{tuple(args)}\n"
                f"it returned {result}")

    return wrapper


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

