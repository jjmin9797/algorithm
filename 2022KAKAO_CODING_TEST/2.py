import collections


def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = collections.deque(deliveries)
    pickups = collections.deque(pickups)
    while deliveries and pickups:
        answer += max(len(deliveries),len(pickups))*2
        nowCap = cap
        while len(deliveries) > 0 and nowCap > 0 :
            nowCap -= deliveries.pop()
        if nowCap < 0 :
            deliveries.append(abs(nowCap))
        nowCap = cap
        while len(pickups) > 0 and nowCap > 0 :
            nowCap -= pickups.pop()
        if nowCap < 0 :
            pickups.append(abs(nowCap))
        while True :
            if len(deliveries) > 0 and 0 == deliveries.pop():
                pass
            else : break
        while True :
            if len(pickups) > 0 and 0 == pickups.pop():
                pass
            else : break

        print(deliveries,pickups)
        
        



    return answer

print(solution(2,7,[1,0,2,0,1,0,2],[0,2,0,1,0,2,0]))