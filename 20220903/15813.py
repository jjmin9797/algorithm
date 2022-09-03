a = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
name = input()
ctn = 0
for na in name:
    ctn += a.index(na)
print(ctn)