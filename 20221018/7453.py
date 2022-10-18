import sys
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(list(map(int,sys.stdin.readline().strip().split())))

print(numbers)