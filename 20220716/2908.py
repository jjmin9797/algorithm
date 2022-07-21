a = input().split()

a[0] = a[0][2]+a[0][1]+a[0][0]
a[1] = a[1][2]+a[1][1]+a[1][0]

a = list(map(int,a))
print(max(a))
