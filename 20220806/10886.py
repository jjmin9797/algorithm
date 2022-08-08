n = int(input())
cute = 0
noCute = 0
for i in range(n):
    a = int(input())
    if a == 1 :
        cute += 1
    else :
        noCute += 1

if cute > noCute :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")