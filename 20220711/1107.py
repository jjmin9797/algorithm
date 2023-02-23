n = int(input()) #이동해야할 채널
m = int(input()) #고장난 리모컨 버튼

#고장버튼 리스트 초기값은 아무것도 고장나있지 않다
broken = [False] * 10
print(broken)

if m > 0 : #만약에 고장난 버튼이 1개 이상이라면
    #숫자형태로 리스트에 담아준다.
    a = list(map(int,input().split()))
else :
    a = [] #고장난 리스트에는 아무것도 없을 것 !


#8 5 4
