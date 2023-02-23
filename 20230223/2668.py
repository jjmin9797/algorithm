import sys

input = sys.stdin.readline

n = int(input())
arr1 = [i for i in range(1, n + 1)]
arr2 = [int(input()) for _ in range(n)]

print(arr1, arr2)
answer = set()
for i in range(n):
    print()
    if arr1[arr2[i] - 1] == arr2[arr1[i] - 1]:
        answer.add(arr1[i])
        answer.add(arr2[i])
print(answer)
