import sys

input = sys.stdin.readline


def solution(N, M, L, K, stars):
    MAX = 0
    # 5,5
    # 5,5 ~ 9,9
    # 5,4 ~ 9,8
    # 5,3 ~ 9,7
    # 5,2 ~ 9,6
    # 5,1 ~ 9,5

    # 1,1 5,5 9,9

    return 1


print(
    solution(12, 10, 4, 7, [[2, 4], [7, 3], [3, 1], [5, 6], [4, 7], [12, 10], [8, 6]])
)
