board = ["A"+input() for _ in range(8)]
count = 1
result = 0
for b in board :
    if count % 2 == 1 :
        for c in range(1,8,2):
            if b[c] == "F":
                result += 1
    else :
        for c in range(2,9,2):
            if b[c] == "F" :
                result += 1
    count += 1
print(result)
