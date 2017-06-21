import math as m
with open("PE42_input.txt") as file:
    words = file.read().strip().split('\",\"')
    words[-1] = words[-1][:-1]
    words[0] = words[0][1:]


alphabet = {'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8, 
        'K': 11, 'J': 10, 'M': 13, 'L': 12, 'O': 15, 'N': 14, 'Q': 17, 'P': 16, 'S': 19, 
        'R': 18, 'U': 21, 'T': 20, 'W': 23, 'V': 22, 'Y': 25, 'X': 24, 'Z': 26}

def nameValue(name):
    global alphabet    
    sum = 0
    for i in name:
        sum += alphabet[i]
    
    return  sum

trianglenum = lambda n: 0.5 * n * (n + 1)

trianglewords = 0

def isTriangular(n):
    a = (m.sqrt(8.0 * n + 1) - 1) / 2
    return a.is_integer()
    
for word in words:
    if isTriangular(nameValue(word) ):
        trianglewords +=1

print trianglewords