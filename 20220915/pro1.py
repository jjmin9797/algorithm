import collections
def solution(money):
    answer = 0
    length = len(money)
    ccc = money.index(min(money))
    money = collections.deque(money)
    for _ in range(ccc):
        money.append(money.popleft())
    money=list(money)
    dp = [[] for _ in range(length+1)]
    dp2 = [0 for _ in range(length+1)]
    dp[0] = [0,0]
    dp[1] = [money[0],0]
    dp[2] = [money[1],money[0]]
    dp[3] = [money[0]+money[2],money[1]]
    money = [0]+money
    for i in range(4,length+1):
        a = max(dp[i-4][1]+money[i-3]+money[i],max(dp[i-4])+money[i-2]+money[i])
        b = max(dp[i-1])
        dp[i] = [a,b]

    return max(dp[-1])

money = [20,2,3,50]

solution(money)