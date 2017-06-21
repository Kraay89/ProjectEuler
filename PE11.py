import re

grid = []
with open('PE11_input.txt') as file:
    for a in file.readlines():
        grid.append(map(int, a.strip().split()))

def horizontalsearch(grid, n):
    listprod = lambda x,y : x * y # Multiply a list of numbers together
    largestProduct = 0 #keep track of the largest product untill now
    for i in grid:
        #go through all rows in the matrix
        for j in range(len(i)-n+1):
            #within each row, take each n entries and check if their product is bigger
            #than the previous largestProduct
            if reduce(listprod, i[j:j+n]) > largestProduct:
                # If the current product is bigger, update LargestProduct
                largestProduct = reduce(listprod, i[j:j+n])        
                
    return largestProduct

def verticalsearch(grid, n):
    return horizontalsearch(zip(*grid[::-1]), n)   

def diagonalsearch



print horizontalsearch(grid, 4)
print verticalsearch(grid, 4)

#print verticalsearch([[5,6,7,8],[1,2,3,4],[13,14,15,16],[9,10,11,12]], 2)


