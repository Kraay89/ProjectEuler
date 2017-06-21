import time


def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


t0 = time.time()
nums = {1:1}
max = 1
maxnum = 1
for i in range(2,10**6):
    sequence = [i]
    while i > 1:
        if i in nums:
            break
        i = collatz(i)
        sequence.append(i)
    sequence = sequence[::-1]
    for a, b in enumerate(sequence):
        nums[b] = a+nums[i]
        if nums[b] > max:
            max = nums[b]
            maxnum = b


print maxnum, "has a sequence with length: ", max

t1 = time.time()

nums = {1:1}
max = 1
maxnum = 1
for i in range(500001,10**6,2):
    sequence = [i]
    while i > 1:
        if i in nums:
            break
        i = collatz(i)
        sequence.append(i)
    sequence = sequence[::-1]
    for a, b in enumerate(sequence):
        nums[b] = a+nums[i]
        if nums[b] > max:
            max = nums[b]
            maxnum = b


print maxnum, "has a sequence with length: ", max

t2 = time.time()

print "1, 2, 3, ..., 999999 took: ", t1-t0
print "500001, 500003, ..., 999999 took: ", t2 - t1