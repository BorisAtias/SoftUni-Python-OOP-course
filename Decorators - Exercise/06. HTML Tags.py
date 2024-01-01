def tags(curr_tag):
    def decorator(func):
        def wrapper(*args):
            return f"<{curr_tag}>{func(*args)}</{curr_tag}>"

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
