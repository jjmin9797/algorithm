import sys

input = sys.stdin.readline

arr = list(input().rstrip())  # 문자열을 하나의 리스트로 받는것.(list)

result = [""] * len(arr)


def solution(now, arr):
    if not arr:
        return
    min_value = min(arr)
    min_idx = arr.index(min_value)
    result[now + min_idx] = min_value
    print("".join(result))
    solution(now + min_idx + 1, arr[min_idx + 1 :])
    solution(now, arr[:min_idx])


solution(0, arr)
