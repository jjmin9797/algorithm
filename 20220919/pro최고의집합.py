def solution(n, s):
    if n > s :
        return [-1]
    a = (s//n)
    b = (s % n)
    answer = [a for _ in range(n)]
    for i in range(b):
        answer[i] += 1
    answer.sort()
    return answer
print(solution(2,8))