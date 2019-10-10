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

if __name__ == "__main__":
    print(divisibleUpTo(10000))