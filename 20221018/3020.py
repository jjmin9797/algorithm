import sys
from collections import Counter

N, H = map(int, sys.stdin.readline().strip().split()) # N: 장애물 갯수(동굴길이), H: 동굴 높이
X, Y = [ 0 for _ in range(H+1)], [ 0 for _ in range(H+1)] # X: 석순, Y: 종유석

for r in range(N): # num 길이의 석순/종유석이 몇개 있는지 X,Y배열에 cnt
    num = int(sys.stdin.readline())
    if r % 2 == 0: # 짝수 ==> 석순
        X[num] += 1
    else: # 홀수 ==> 종유석
        Y[num] += 1

Px, Py = [ 0 for _ in range(H+1)], [ 0 for _ in range(H+1)] # 석순, 종유석의 prefix sum
Px[H], Py[1] = X[H], Y[H]

# prefix sum
for r in range(1, H):
    Px[H-r] = Px[H-r+1] + X[H-r] # R-1경로 석순 갯수 = R경로 석순 갯수 + (R-1)높이 석순 갯수
    Py[r+1] = Py[r] + Y[H-r] # R+1경로 종유석 갯수 = R경로 종유석 갯수 + (H-R)높이 종유석 갯수

# 석순 + 종유석
P = [ 0 for _ in range(H)]
for r in range(H):
    P[r] = Px[r+1] + Py[r+1]

#Counter
c = Counter(P) # {Key: x경로로 갔을 때의 장애물 갯수, Value: 그런 경로의 갯수}
minXY = list(sorted(c.keys()))[0] # Key 오름차순으로 정렬
print(minXY, c[minXY]) # 최소 장애물 갯수, 경로 갯수