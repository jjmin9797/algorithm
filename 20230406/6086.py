import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
routes = defaultdict(list)
for _ in range(n):
    start, end, cost = input().strip().split()
    routes[start].append([int(cost), end])
    routes[end].append([int(cost), start])
print(routes)
# https://roamingman.tistory.com/39
