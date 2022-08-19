
while True :
    a = input()
    if a == "." :
        break
    board = []
    check = True
    for b in a :
        print(board)
        if b == "(" and b == "[" :
            board.append(b)
        elif b == ")" :
            if len(board) != 0 and board[-1] == "(" :
                del board[-1]
                pass
            else :
                check = False
                break

        elif b == "]" :
            if len(board) != 0 and board[-1] == "[" :
                del board[-1]
                pass
            else :
                check = False
                break
        else :
            pass

    if check and len(board) == 0 :
        print("yes")
    else :
        print("no")
    
    
            