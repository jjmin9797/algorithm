import sys
from itertools import product as p


def twoTwo(lis, k):
    print(lis)
    if k == 0:
        return lis[::-1]
    return twoTwo(lis[-1 * 2**k :], k - 1) + lis[: -1 * 2**k]


n = int(input())
ori = [i for i in range(1, n + 1)]
tar = list(map(int, sys.stdin.readline().split()))
k = 1
while n > 1:
    k += 1
    n //= 2
for i in p([i for i in range(1, k)], repeat=2):
    if tar == twoTwo(twoTwo(ori[:], i[0]), i[1]):
        print(*i)
        break
