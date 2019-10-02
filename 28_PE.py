sides = 5
steps = sides - 2


def X(n):
    while n > 0:
        yield X(n - 1) + 2
    yield 1


print[i for i in X(3)]
