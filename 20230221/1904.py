n = int(input())

n1 = 1
n2 = 2
answer = 0

for i in range(3, n + 1):
    answer = (n1 + n2) % 15746
    if i == n:
        print(answer)
        break
    n1 = n2
    n2 = answer


# 1 2
# 2 3
# 3 5
# 5 8
