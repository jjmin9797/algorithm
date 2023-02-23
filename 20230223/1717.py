import sys

sys.setrecursionlimit(100_100)
input = sys.stdin.readline

n, m = map(int, input().split())
p = [i for i in range(n + 1)]


def find(a):
    if a == p[a]:
        return a
    p[a] = find(p[a])
    return p[a]


def union(a, b):
    pa = find(a)
    pb = find(b)
    p[pb] = pa


for _ in range(m):
    print(p)
    t, c, d = map(int, input().strip().split())
    if t == 0:
        union(c, d)
    else:
        if find(c) == find(d):
            print("YES")
        else:
            print("NO")
