n = int(input())
for i in range(n):
    strs = input()
    result = 0
    addScore = 1
    for string in strs:
        if string == "O" :
            result += addScore
            addScore += 1
        elif string == "X" :
            addScore = 1
    print(result)