import sys

input = sys.stdin.readline
n = int(input())
testcases = [int(input()) for _ in range(n)]
dp = [1, 1, 2]
for i in range(3, 12):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])


for case in testcases:
    print(dp[case])


# 4분 30초
