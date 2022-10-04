import collections
import math
def is_prime_number(n):
    array = [True for i in range(n+1)]

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): 
        if array[i] == True: 
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return array
pn = is_prime_number(100001)

n = int(input())
for _ in range(n) :
    s,e = map(int,input().split())
    dp = [-1 for _ in range(10001)]
    dp[s] = 0
    q = collections.deque()
    q.append((s))
    while q:
        number = str(q.popleft())
        if number == str(e) :
            print(dp[int(number)])
            break
        for i in range(4):
            for j in range(0,10):
                num = list(number)
                num[i] = str(j)
                nextNum = int("".join(num))
                if nextNum >= 1000 and dp[nextNum] == -1 and pn[nextNum]:
                    q.append((nextNum))
                    dp[nextNum] = dp[int(number)]+1
    if dp[e] == -1 :
        print(-1)
