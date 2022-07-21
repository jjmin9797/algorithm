n = int(input())
numbers = []
for _ in range(n):
    a = int(input())
    if a != 0 :
        numbers.append(a)
    else :
        del numbers[-1]
print(sum(numbers))