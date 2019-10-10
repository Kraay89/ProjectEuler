def divisibleUpTo(n):
    prod = 1
    bases = []
    for i in range(2,n+1):
        if prod%i!=0:
            for x in bases[:]:
                if i%x==0:
                    bases.remove(x)
                    prod//=x
            prod*=i
            bases.append(i)

    return prod

def zooi(n):
    i = 1
    for k in (range(1, n+1)):
        if i % k > 0:
            for j in range(1, n+1):
                if (i*j) % k == 0:
                    i *= j
                    break
    return i

if __name__ == "__main__":
    print(divisibleUpTo(10000))
    print(zooi(10000))