name = list(map(str,input().split("-")))
result = ""
for n in name :
    result += n[0]
print(result)