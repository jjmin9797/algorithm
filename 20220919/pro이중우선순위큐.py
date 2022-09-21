import heapq
def solution(operations):
    result = []
    for i in operations:
        a, b = i.split()
        if a == 'I':
            heapq.heappush(result, int(b))
        else:
            if len(result) > 0:
                if b == '1':
                    result.pop(result.index(heapq.nlargest(1, result)[0]))
                else:
                    heapq.heappop(result)
    if len(result) == 0:
        return [0, 0]
    else:
        return [heapq.nlargest(1, result)[0], result[0]]