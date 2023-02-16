from itertools import permutations

def factorial(number):
    a = 1
    for i in range(1,number+1):
        a *= i
    return a

def solution(n, k):
    # 5일떄 k가 50
    # 4,5 / 2
    # [3,1,2]
    # 1로 시작 4! 24 (1~24)
    # 2로 시작 4! 24 (25~48)
    # 3로 시작 4! 24 (49~72)
    #   1로 시작 3! 6 (1~6)
    #       2로 시작 2! (1~2)
    #           4로 시작 1 1 1
    #           5로 시작 1 2 2
    #       4로 시작 2! (3~4)
    #       5로 시작 2! (5~6)
    #   2로 시작 3! 6
    #   4로 시작 3! 6
    #   5로 시작 3! 6
    #------------
    # 4로 시작 4! 24 
    # 5로 시작 4! 24
    
    # 1 2! 1 2
    # 2 2! 2 3
    # 3 2! 3 4
    answer = []
    nums = [i for i in range(1,n+1)]
    while True:
        size = len(nums)
        routes = factorial(size-1)
        start,end = 1, routes
        if end == 1:
            answer.append(nums.pop(k-1))
            answer += nums
            break
        for i in range(size):
            if start <= k <= end :
                answer.append(nums[i])
                nums.remove(nums[i])
                k -= (start-1)
                break
            start += routes
            end += routes
    return answer

            