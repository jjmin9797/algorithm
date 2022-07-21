fi = [0,1]
n = int(input())
for i in range(45):
    fi.append(fi[i]+fi[i+1])
print(fi[n])