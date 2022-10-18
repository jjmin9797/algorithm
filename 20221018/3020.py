'''
import sys
n,m = map(int,input().split())
stalagmite = [] #석영
stalactite = [] #종유석
result_number = 0
result_obstacle = n

for i in range(n):
    hei = sys.stdin.readline().strip()
    if i % 2 == 0 :
        stalagmite.append(hei)
    else :
        stalactite.append(hei)
stalactite.sort()
stalagmite.sort()
'''
def binary_search(hei,stone):
    start = 0
    end = len(stone)-1
    while start<=end :
        mid = (start+end) // 2
        if mid == 0 or hei == stone[mid] :
            return start
        elif stone[mid] > hei :
            end = mid
        elif stone[mid] < hei :
            start = mid
print(binary_search(4,[1,3,5]))