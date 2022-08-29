a = int(input())


if a % 5 == 0 :
    if a % 3 == 0 :
        print(a,"는 5의 배수이면서 3의 배수입니다.")
    else :
        print(a,"는 5의 배수입니다.")
else :
    if a % 3 == 0 :
        print(a,"는 3의 배수입니다.")
    else :
        print(a,"는 3의 배수도 5의 배수도 아닙니다.")