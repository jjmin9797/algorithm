a = int(input())

for i in range(a):
    n,m = map(int,input().split())
    q = list(map(int,input().split()))
    key = [i for i in range(n)]
    count = 0
    while len(q) != 0 :
        if q[0] < max(q) :
            q.append(q[0])
            del q[0]
            key.append(key[0])
            del key[0]
        else :
            del q[0]
            if key[0] == m :
                print(count+1)
                break
            del key[0]
            count += 1
