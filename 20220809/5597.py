scores = []
for i in range(28):
    scores.append(int(input()))
scores.sort()
for i in range(1,31):
    if i in scores :
        pass
    else :
        print(i)