def check(left, right, type):
    ret = type
    while left < right:
        if str[left] != str[right] and type == 0:
            a = check(left + 1, right, type + 1)
            b = check(left, right - 1, type + 1)
            ret = min(a, b)
            return ret
        elif str[left] != str[right] and type == 1:
            return 2
        else:
            left += 1
            right -= 1
    return ret


N = int(input())
for _ in range(N):
    str = input()
    print(check(0, len(str) - 1, 0))
