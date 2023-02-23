import sys

input = sys.stdin.readline
sys.setrecursionlimit(100_000)

n, m = map(int, input().split())
p = [i for i in range(n)]


def find(a):
    if a == p[a]:
        return a
    p[a] = find(p[a])
    return p[a]


def union(a, b):
    pa = find(a)
    pb = find(b)
    p[max(pa, pb)] = min(pa, pb)


count = 1
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        break
    union(a, b)
    count += 1

if count == m + 1:
    print(0)
else:
    print(count)
