fivo = [0,1]
n = int(input())
for i in range(20):
    fivo.append(fivo[i]+fivo[i+1])
print(fivo[n])