n = int(input())
strings = [input() for _ in range(n)]
result =0
for s in strings:
    check = s[0]
    count = 0
    checkList = []
    for one in s :
        if count == 0 and one == check :
            checkList.append(one)
            count += 1

        elif count > 0 and one == check :
            count += 1

        elif one != check :

            if one in checkList:
                result += 1
                break
            else :
                count = 0
                check = one
                checkList.append(one)
        
print(n-result)