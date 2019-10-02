from math import sqrt

def d(n):
    return sum((i  for i in xrange(1,n)if n%i==0))

def amicable(n):
    return True if d(d(n)) ==n and d(n)!=n else False

amicable_numbers = (i for i in xrange(1,10000) if amicable(i))

print sum(amicable_numbers)
