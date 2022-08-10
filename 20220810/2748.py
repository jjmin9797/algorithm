d = [0,1]
n = int(input())
count = 0
while len(d) != n+1 :
    d.append(d[count] + d[count+1])
    count += 1
print(d[n])