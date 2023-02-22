import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    answer = 0
    d = int(input())
    prices = list(map(int, input().split()))
    maxPrice = max(prices)
    prices = deque(prices)
    while prices:
        a = prices.popleft()
        if a == maxPrice:
            if prices:
                maxPrice = max(prices)
                continue
            else:
                break

        answer += maxPrice - a
    print(answer)


# 1 1 1 5 1 1 10 3 3 1 16
