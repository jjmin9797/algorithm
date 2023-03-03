import sys

sys.setrecursionlimit(100_100)


def check(num):
    num = str(num)
    count = 0
    for i in num:
        if int(i) % 2 == 1:
            count += 1
    return count


def go(now, total):
    if len(now) == 1:
        result.append(total)
        return
    elif len(now) == 2:
        nxt = int(now[0]) + int(now[1])
        go(str(nxt), total + check(nxt))
    else:
        for i in range(1, len(now)):
            for j in range(i + 1, len(now)):
                nxt1 = now[:i]
                nxt2 = now[i:j]
                nxt3 = now[j:]
                nxt = int(nxt1) + int(nxt2) + int(nxt3)
                go(str(nxt), total + check(nxt))
    pass


n = input()
result = []
go(n, check(n))

print(min(result), max(result))
