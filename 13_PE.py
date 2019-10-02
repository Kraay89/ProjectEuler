sum =0 
with open('PE13_input.txt') as file:
    for num in file.readlines():
        sum += int(num.strip())

print str(sum)[0:10]