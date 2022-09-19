def solution(triangle):
    dp = []
    for i in range(1,len(triangle)+1):
        a = [-1 for _ in range(i)]
        dp.append(a)
    for i in range(len(triangle)-1,0,-1):
        for j in range(i):
            triangle[i-1][j] += max(triangle[i][j],triangle[i][j+1])
    
    answer = triangle[0][0]
    return answer
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))