def solution(n, arr1, arr2):
    
    a1 = [[] for _ in range(n)]
    a2 = [[] for _ in range(n)]
    for i in range(n):
        nxt1 = str(bin(arr1[i]))[2:]
        nxt2 = str(bin(arr2[i]))[2:]
        if len(nxt1) < n :
            nxt1 = ("0"*(n-(len(nxt1))))+nxt1
        if len(nxt2) < n :
            nxt2 = ("0"*(n-(len(nxt2))))+nxt2
        for j in nxt1:
            if j == "1":
                a1[i].append("#")
            elif j == "0":
                a1[i].append(" ")
        for j in nxt2:
            if j == "1":
                a2[i].append("#")
            elif j == "0":
                a2[i].append(" ")
    answer = [[0 for _ in range(len(a1))] for _ in range(len(a1))]

    for i in range(len(a1)):
        for j in range(len(a1)):
            if a1[i][j] == "#" or a2[i][j] == "#" :
                answer[i][j] = "#"
            else :
                answer[i][j] = " "
    
                
    return answer

n = 5
dd = [9, 20, 28, 18, 11]
ddd = [30, 1, 21, 17, 28]
print(solution(n,dd,ddd))