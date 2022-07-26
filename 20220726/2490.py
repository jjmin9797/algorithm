#배 0
#등 1
#도 배 1 등 3 // 개 배 2 등 2 // 걸 배 3 등 1 // 윹 배 4 // 모 등 4
for _ in range(3):
    a = list(map(int,input().split()))

    bae = a.count(0)
    deong = a.count(1)

    if bae == 1 and deong == 3 :
        print("A")
    elif bae == 2 and deong == 2 :
        print("B")
    elif bae == 3 and deong == 1 :
        print("C")
    elif bae == 4 and deong == 0 :
        print("D")
    elif bae == 0 and deong == 4 :
        print("E")