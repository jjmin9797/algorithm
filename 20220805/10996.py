n = int(input())
if n == 1 :
    print("*")
else :
    for i in range(n):
        if n % 2 == 1 :
            str = ""
            for x in range(n):
                if x % 2 == 1 :
                    str += " "
                else :
                    str += "*"
            print(str)
            str = ""
            for x in range(n-1):
                if x % 2 == 1 :
                    str += "*"
                else :
                    str += " "
            print(str)
        else :
            str = ""
            for x in range(n-1):
                if x % 2 == 1 :
                    str += " "
                else :
                    str += "*"
            print(str)
            str = ""
            for x in range(n):
                if x % 2 == 1 :
                    str += "*"
                else :
                    str += " "
            print(str)


