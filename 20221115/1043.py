n,m = map(int,input().split())
knowList = set(map(int,input().split()[1:]))
parties = []
for _ in range(m):
    parties.append(set(map(int,input().split()[1:])))

for _ in range(m):
    for party in parties :
        if party & knowList :
            knowList = knowList.union(party)

print(knowList)