#지구,태양,달
#지구 1~15 태양 1 ~ 28 달 1 ~ 19
#우리 1년 -> 1 1 1
#1년이 지날 때 마다 세 수는 모두 1씩 증가
#15년 15 15 15 여기서 1년이 지나면 1 16 16
#E S M 이 주어지고 1년이 준규가 사는 나라에서 1 1 1일 때 준규가 사는 나라에서 ESM이 우리가 알고 있는 연도로 몇년인지 구하는 프로그램

inputESM = list(map(int,input().split()))
startESM = [1,1,1]
count = 1
while inputESM != startESM :
    for x in range(3) :
        startESM[x] += 1
    if startESM[0] > 15 :
        startESM[0] = 1
    if startESM[1] > 28 :
        startESM[1] = 1
    if startESM[2] > 19 :
        startESM[2] = 1
    count += 1
print(count)

