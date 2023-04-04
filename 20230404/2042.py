import sys

input = sys.stdin.readline
n, m, k = map(int, input().strip().split())
numbers = [0 for _ in range(n + 1)]
originalNumbers = [0]
commands = []
for i in range(1, n + 1):
    nxt = int(input())
    originalNumbers.append(nxt)
    numbers[i] = numbers[i - 1] + nxt

for _ in range(m + k):
    commandType, beforeNumber, afterNumber = map(int, input().strip().split())
    if commandType == 2:
        print(numbers[afterNumber] - numbers[beforeNumber - 1])

    else:
        diffValue = afterNumber - (originalNumbers[beforeNumber])
        originalNumbers[beforeNumber] = afterNumber
        for j in range(beforeNumber, n + 1):
            numbers[j] += diffValue


"""
1 2 3  4  5
1 3 6 10 15


"""
