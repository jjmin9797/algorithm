n,m = map(int,input().split())
d = []
b = []
result = []
for ss in range(n):
    d.append(input())
for ss in range(m):
    bb = input()
    if bb in d :
        result.append(bb)

result.sort()
print(len(result))
for r in result :
    print(r)

