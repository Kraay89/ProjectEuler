import math as m
import time

t0 = time.time()


def perfSquare(n):
    return m.sqrt(n).is_integer()


stop = False
for a in range(1000, 2, -1):
    if stop:
        break
    for b in range(1000, 3, -1):
        if stop:
            break
        c_squared = a**2+b**2
        if perfSquare(c_squared):
            c = int(m.sqrt(c_squared))
            if a+b+c == 1000:
                stop = True
                print(a, b, c, a+b+c, a*b*c)

print('Time passed: ', time.time()-t0)
