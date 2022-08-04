import sys
n = int(input())
myL = []
for i in range(n):
    a = sys.stdin.readline().rstrip()
    comm = list(map(str,a.split()))
    if comm[0] == "add" and int(comm[1]) not in myL:
        myL.append(int(comm[1]))
    elif comm[0] == "remove" and int(comm[1]) in myL:
        myL.remove(int(comm[1]))
    elif comm[0] == "check" :
        if int(comm[1]) in myL :
            print(1)
        else :
            print(0)
    elif comm[0] == "toggle":
        if int(comm[1]) in myL :
            myL.remove(int(comm[1]))
        else :
            myL.append(int(comm[1]))
    elif comm[0] == "all" :
        myL = [i for i in range(1,21)]
    elif comm[0] == "empty" :
        myL = []