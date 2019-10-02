with open("PE22_input.txt") as file:
    names = file.read().strip().split('\",\"')
    names[-1] = names[-1][:-1]
    names[0] = names[0][1:]
    names.sort()


# alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alphabet = {}
# for i,j in enumerate(alpha, start = 1):
#     alphabet[j] = i 
alphabet = {'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8, 
        'K': 11, 'J': 10, 'M': 13, 'L': 12, 'O': 15, 'N': 14, 'Q': 17, 'P': 16, 'S': 19, 
        'R': 18, 'U': 21, 'T': 20, 'W': 23, 'V': 22, 'Y': 25, 'X': 24, 'Z': 26}

def nameValue(name):
    global alphabet    
    sum = 0
    for i in name:
        sum += alphabet[i]
    
    return  sum
    

# print nameValue('COLIN')

sum = 0
for i, j in enumerate(names, start = 1):
    sum += i * nameValue(j)
print sum