
a = int(input())
b = int(input())
c = int(input())
abc = str(a*b*c)

key = {str(i):0 for i in range(10)}

for i in abc:
    key[i] += 1
for i in range(10):
    print(key[str(i)])