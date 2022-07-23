#가장 큰 점수, 몇번째 사람
for i in range(1,6):
    a = list(map(int,input().split()))
    print(i,":",sum(a))