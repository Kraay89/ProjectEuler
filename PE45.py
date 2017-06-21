import math as m

def isTriangular(n):
    a = (m.sqrt(8.0 * n + 1) - 1) / 2
    return a.is_integer()

def isPentagonal(n):
    a = (m.sqrt(24.0 * n + 1) + 1) / 6
    return a.is_integer()

def hexagonalnum(n):
    return n * (2 * n - 1)

i = 1
while True:
    if isTriangular(hexagonalnum(i)) and isPentagonal(hexagonalnum(i)):
        print hexagonalnum(i)
        stop = raw_input("stop?? y or n >>>")
        if stop == 'y':
            break
    i+=1