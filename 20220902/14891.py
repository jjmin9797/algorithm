import collections

t1 = collections.deque()
t2 = collections.deque()
t3 = collections.deque()
t4 = collections.deque()
ts = [t1,t2,t3,t4]

for i in range(4):
    ts[i].extend(list(map(int,(list(input())))))



def bing(start,where):
    global ts
    if 0 <= start-1 < 4 and check[start-1]:
        if ts[start-1][2] != ts[start][6] :
            check[start-1] = False
            bing(start-1,where*-1)
    if 0<= start + 1 < 4 and check[start+1]:
        if ts[start+1][6] != ts[start][2] :
            check[start+1] = False
            bing(start+1,where*-1)
    
    if where == 1 :
        ts[start].appendleft(ts[start].pop())
    elif where == -1 :
        ts[start].append(ts[start].popleft())
    

k = int(input())
for _ in range(k):
    check = [True] * 4
    n,w = map(int,input().split())
    check[n-1] = False
    bing(n-1,w)

o = 1
result = 0
for i in ts:
    if i[0] == 1 :
        result += o
    o *= 2
print(result)
