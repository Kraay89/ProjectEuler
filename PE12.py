import math

def triangular(n):
    return reduce(lambda x, y: x + y, xrange(n+1))

plist = [2]
with open('primesfrom3to1000000.txt') as file:
    for line in file.readlines():
        plist.append(int(line.strip()))

def numberOfDivisors(n):
    m = n
    global plist
    if m in plist:
        return 1
    primefactors = {}
    i = 0
    for i in plist:
        while n%i == 0:
            try:
                primefactors[i] += 1
            except KeyError:
                primefactors[i] = 1
            
            n /= i
        
        if i > math.sqrt(m):
            return reduce(lambda x, y : x * y , map(lambda x:x+1, primefactors.values()))

# print numberOfDivisors(triangular(12375))     
#   
# i = 8
# 
# while numberOfDivisors(triangular(i)) <= 500:
#     i+=1
# 
# print i, "has:", numberOfDivisors(triangular(i)), "divisors"
print triangular(12375)