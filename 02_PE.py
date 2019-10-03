def fibGen():
    n = 0
    m = 1
    while True:
        newNum = n+m
        yield newNum
        n, m = m, newNum

total = 0
for fibNum in fibGen():
    if fibNum>4000000:
        break
    elif fibNum%2==0:
        total+=fibNum

print(total)