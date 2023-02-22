from itertools import combinations

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
b = []
for i in range(1, 13):
    b += list(combinations(a, i))
print(len(b))
