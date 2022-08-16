n = int(input())
scores = list(map(int,input().split()))
maxValue = max(scores)
result = []
for s in scores :
    result.append(s/maxValue*100)

print(sum(result)/n)