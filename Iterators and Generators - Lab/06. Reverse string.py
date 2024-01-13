def reverse_text(my_string):
    for char in reversed(my_string):
        yield char

for char in reverse_text("step"):
    print(char, end='')
