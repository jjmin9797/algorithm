'''
n = int(input())
sangCard = list(map(int,input().split()))
m = int(input())
howManyCard = list(map(int,input().split()))

result = [0 for _ in range(m)]

for i in range(len(howManyCard)):
    result[i] += sangCard.count(howManyCard[i])
print(" ".join(map(str,result)))
'''
import collections
n = int(input())
sangCard = list(map(int,input().split()))
m = int(input())
howManyCard = list(map(int,input().split()))
a = collections.Counter(sangCard)
for h in howManyCard:
    print(a[h],end=" ")