def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False


n = 775146
divs = []
for i in primes_sieve2(n):
    if 600851475143 % i == 0:
        divs.append(i)

print(divs)
