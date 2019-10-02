import numpy as np

plist = []
with open("primesfrom3to1000000.txt") as file:
    for line in file.readlines():
        plist.append(int(line.strip()))

plist = np.array(plist)

