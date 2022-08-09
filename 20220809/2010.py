import sys

n = int(input())
b = []
for i in range(n):
    b.append(int(sys.stdin.readline()))

print(sum(b)-n+1)
    
