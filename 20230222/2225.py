# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 2개 더해서 20

mod = 1000000000
n, k = map(int, input().split())
d = [[0] * (n + 1) for _ in range(k + 1)]
d[0][0] = 1

for i in range(1, k + 1):
    for j in range(0, n + 1):
        for l in range(0, j + 1):
            d[i][j] += d[i - 1][j - l]
        d[i][j] %= mod
print(d[k][n])
