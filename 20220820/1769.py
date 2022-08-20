a = input()
a = list(a)
count = 0
while len(a) != 1 :
    b = list(map(int,a))
    a = list(str(sum(b)))
    count += 1

print(count)
if a[0] == "3" or a[0] == "6" or a[0] == "9" :
    print("YES")
else :
    print("NO")