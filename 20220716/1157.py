n = input()
alDic = {}
alphaList = [chr(c) for c in range(ord('A'), ord('Z')+1)]

result = [0]*len(alphaList)

for i in range(len(alphaList)):
    result[i] += n.count(alphaList[i])
    result[i] += n.count(alphaList[i].lower())
if result.count(max(result)) > 1 :
    print("?")
else :
    print(alphaList[result.index(max(result))])
