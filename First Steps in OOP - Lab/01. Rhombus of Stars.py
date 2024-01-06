# create a function that takes a number n and prints a rhombus with size n

def print_row(n):
    for row in range(n):
        print(' ' * (n - row - 1), end='')
        print('* ' * (row + 1))
    for row in range(n - 2, -1, -1):
        print(' ' * (n - row - 1), end='')
        print('* ' * (row + 1))

# create input
n = int(input())
print_row(n)