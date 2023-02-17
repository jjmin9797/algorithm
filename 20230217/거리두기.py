# 오 왼 아 위
# 오 아 왼 위
mht_one = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 1)]
mht_two = [(0, 2), (2, 0), (0, -2), (-2, 0), (0, 2)]


# 오아, 왼아,  왼위 오위
mht = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def bfs(i, j, board):
    for m in range(4):
        dx, dy = i + mht_one[m][0], j + mht_one[m][1]
        if dx >= 0 and dx < 5 and dy >= 0 and dy < 5:
            if board[dx][dy] == "P":
                return False

    for m in range(4):
        dx, dy = i + mht_two[m][0], j + mht_two[m][1]
        cx, cy = i + mht_one[m][0], j + mht_one[m][1]
        if dx >= 0 and dx < 5 and dy >= 0 and dy < 5:
            if board[dx][dy] == "P" and board[cx][cy] == "O":
                return False

    for m in range(4):
        dx, dy = i + mht[m][0], j + mht[m][1]
        if dx >= 0 and dx < 5 and dy >= 0 and dy < 5:
            if board[dx][dy] == "P":
                cx1, cy1 = i + mht_one[m][0], j + mht_one[m][1]
                cx2, cy2 = i + mht_one[m + 1][0], j + mht_one[m + 1][1]
                print(cx1, cy1, cx2, cy2, dx, dy, i, j)
                if board[cx1][cy1] == "O" or board[cx2][cy2] == "O":
                    return False

    return True


def check(board):
    for i in range(5):
        for j in range(5):
            if board[i][j] == "P":
                if bfs(i, j, board):
                    continue
                return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer


solution(
    [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
    ]
)
