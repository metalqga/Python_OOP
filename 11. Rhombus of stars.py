n = int(input())


def print_stars(n, row):
    for space in range(n - row):
        print(" ", end="")
    for star in range(1, row):
        print("*", end=' ')
    print("*")


def print_upper(n):
    for row in range(1, n + 1):
        print_stars(n, row)


def print_lower(n):
    for row in range(n - 1, 0, -1):
        print_stars(n, row)


def print_rhombus(n):
    print_upper(n)
    print_lower(n)


print_rhombus(n)
