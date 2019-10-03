multiples_3_and_5 = set(range(0,1000,3))
multiples_3_and_5.update(set(range(0,1000,5)))
print(sum(multiples_3_and_5))
