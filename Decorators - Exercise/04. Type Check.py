def type_check(curr_type):
    def decorator(func):
        def wrapper(*args):
            for element in args:
                if not isinstance(element, curr_type):
                    return f"Bad Type"

            return func(*args)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
