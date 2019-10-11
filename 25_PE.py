
def fibGen(): # Recycled from exercise 02_PE.py
    n = 0
    m = 1
    while True:
        newNum = n+m
        yield newNum
        n, m = m, newNum

for index, num in enumerate(fibGen()):
    if len(str(num)) >= 1000:
        print(index+2, '\n\n\n', num)
        break