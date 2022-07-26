n = int(input())
numbers = []
#리스트.append(추가할값) - 추가
#del 리스트[삭제할출석번호] - 삭제
for i in range(n):
    a = int(input())
    if a == 0 :
        del numbers[-1]
    else :
        numbers.append(a)
print(sum(numbers))