from heapq import heappop, heappush

def dijkstra(board,routes):
    heap = []
    heappush(heap,[0,1])
    while heap:
        cost, node = heappop(heap)
        for c, n in routes[node]:
            if cost + c < board[n] :
                board[n] = cost + c
                heappush(heap,[cost+c, n])


def solution(N, road, K):
    board = [float('inf')] * (N+1)
    board[1] = 0
    routes = [[] for _ in range(N+1)]
    for start,end,cost in road:
        routes[start].append([cost,end])
        routes[end].append([cost,start])
    dijkstra(board,routes)
    return len([i for i in board if i <= K])