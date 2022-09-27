c=0

while c <= 31:

    a=int(input("수를 입력하세요:"))

    import random

    b=random.randint(1,3)

    print("컴퓨터:",b)

    c=c+(a+b)

    print(c)

print("게임 끝")