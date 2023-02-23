import sys

sys.setrecursionlimit(100_000)
input = sys.stdin.readline

n = int(input())  # 도시 수
m = int(input())  # 여행 계획에 속한 도시들의 수
board = [list(map(int, input().split())) for _ in range(n)]
p = [i for i in range(n + 1)]
city = map(int, input().split())


def find(a):
    if p[a] == a:
        return a
    p[a] = find(p[a])
    return p[a]


def union(a, b):
    pa = find(a)
    pb = find(b)
    p[max(pa, pb)] = min(pa, pb)


for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and find(i + 1) != find(j + 1):
            union(i + 1, j + 1)
pl = []
for c in city:
    pl.append(find(c))
if len(set(pl)) == 1:
    print("YES")
else:
    print("NO")
