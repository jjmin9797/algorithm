numbers = [31,28,31,30,31,30,31,31,30,31,30,31]
days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
#1월 1일 월요일
#1월 8일 월요일
y,d = map(int,input().split())
result = 0
for i in range(y-1):
    result += numbers[i]
result += d

print(days[result%7-1])
