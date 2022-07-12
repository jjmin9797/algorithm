import sys
n = 9 #난장이 수
a = [int(input()) for _ in range(n)] #입력받기
a.sort() #오름차순 정렬
total = sum(a) #140
for i in range(0, n):
    for j in range(i+1, n):
        if total - a[i] - a[j] == 100:
            for k in range(0, n):
                if i == k or j == k:
                    continue
                print(a[k])
            sys.exit(0)