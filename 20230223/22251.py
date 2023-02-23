board = [
    [],
    [0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1],
]

chageGraph = [[[]] for _ in range(10)]
for i in range(1, 10):
    chageGraph[i].append(-1)
    for j in range(i + 1, 10):
        ctn = 0
        for x in zip(board[i], board[j]):
            if x[0] != x[1]:
                ctn += 1
        chageGraph[i].append(ctn)
        chageGraph[j].append(ctn)


# N,K,P,X = map(int(input().split()))
# N : 1층부터 N층까지 이동 가능
# K : 최대 자릿수
# P : 최대 변경 LED
# X : 현재 층 수
print(chageGraph[3])
print(chageGraph[5])

# [2,3,2,3,1,3,3,4]
