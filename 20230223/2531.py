import sys

input = sys.stdin.readline
# 총 접시 수, 초밥의 가짓수 , 연속해서 먹는 접시 수, 쿠폰 번호
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
sushi = sushi + sushi[: k - 1]
# counter = [0 for _ in range(d+1)]
answer = -1

for i in range(n):
    now = set(sushi[i : i + k])
    a = len(now)
    if c not in now:
        a += 1
    answer = max(answer, a)
print(answer)
