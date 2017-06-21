sum = 2

with open('primesfrom3to2000000.txt') as file:
    for line in file.readlines():
        sum += int(line.strip())

print sum
        