def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0
    works.sort(reverse=True)

    while n != 0 :
        print(works)
        gigun = works[0]
        search = False
        for i in range(len(works)):
            if gigun != works[i] :
                gigun2 = works[i]
                idx = i
                search = True
                break
        if not search :
            works[-1] -= 1
            n -= 1
            continue
        cha = gigun - gigun2
        for i in range(idx):
            works[i] -= cha
            n -= cha
        if n < 0:
            gak = abs(n)//idx
            na = abs(n)%idx
            for i in range(idx):
                works[i] += gak
            for i in range(na):
                works[i] += 1
            n = 0

        
    

    for w in works :
        answer += w**2
    return answer



a = solution(4,[4,3,3])
print(a)