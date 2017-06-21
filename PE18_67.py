pyramid = []
with open('PE67_input.txt') as file:
    for line in file.readlines():
        pyramid.append(map(int,line.strip().split()))




while len(pyramid) > 1:
    last_row = pyramid.pop()
    for i in range(len(pyramid[-1])):
#         print last_row[i]
#         print last_row[i+1]
#         print pyramid[-1][i]
#         print "+++++++++++++"
        if last_row[i]>=last_row[i+1]:
            pyramid[-1][i] += last_row[i]
        else:
            pyramid[-1][i] += last_row[i+1]

print pyramid