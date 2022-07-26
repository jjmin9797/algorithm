k,n,m = map(int,input().split())
price = k*n
plusMoney = price-m
print(plusMoney)
if plusMoney < 0 :
    print(0)