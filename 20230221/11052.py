n = int(input())
cards = list(map(int, input().split()))
if n == 1:
    print(cards[0])

else:
    cards = [0] + cards
    dp = [cards[1] * i for i in range(1, n + 1)]
    dp = [0] + dp

    for i in range(2, len(cards)):
        now = dp.copy()
        for j in range(i, n + 1):
            now[j] = max(dp[j], ((j // i) * cards[i]) + now[j % i])
        dp = now.copy()

    print(dp[-1])
