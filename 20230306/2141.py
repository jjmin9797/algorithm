import sys

input = sys.stdin.readline

n = int(input())
total_people = 0
village = []

for _ in range(n):
    v, p = map(int, input().strip().split())
    village.append([v, p])
    total_people += p

village.sort(key=lambda x: x[0])


now_people = 0
total_people /= 2
for v, p in village:
    now_people += p
    if now_people >= total_people:
        print(v)
        break
