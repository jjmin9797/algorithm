import sys

input = sys.stdin.readline
nxt = ["+", " ", "-"]


def go(numbers, idx, n, now):
    global answer
    if idx == n:
        if check(now.copy()):
            answer.append(now.copy())
        return
    for nx in nxt:
        now.append(nx)
        now.append(numbers[idx])
        go(numbers, idx + 1, n, now)
        now.pop(-1)
        now.pop(-1)


def check(case):
    nowInt = ""
    nowGiho = 1
    nowNumber = 0
    case = case + ["+"]
    for c in case:
        if str(c).isdigit():
            nowInt += c
        else:
            if c == " ":
                pass
            elif c == "+":
                nowNumber += int(nowInt) * nowGiho
                nowGiho = 1
                nowInt = ""
            elif c == "-":
                nowNumber += int(nowInt) * nowGiho
                nowGiho = -1
                nowInt = ""
    if nowNumber == 0:
        return True
    return False


t = int(input())
for _ in range(t):
    n = int(input())
    answer = []
    numbers = [str(i) for i in range(1, n + 1)]
    go(numbers, 1, n, ["1"])
    answer.sort()
    for a in answer:
        print("".join(a))
    print()
