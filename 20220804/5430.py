#r - 뒤집기
#d - 버리기
import sys
from collections import deque
t = int(input())
for _ in range(t):
    func = sys.stdin.readline().rstrip()
    n = int(input())
    if n >= 2 :
        board = list(map(int,sys.stdin.readline().rstrip()[1:-1].split(",")))
    elif n == 1 :
        board = [int(input()[1:-1])]
    elif n == 0 :
        input()
        board = []
    rvs = True
    if n < func.count("D"):
        print("error")
    else :
        func2 = func.split("D")
        check = func2[-1]
        del func2[-1]
        for i in func2 :
            if len(i) == 0 :
                del board[0]
            elif len(i) % 2 == 0 :
                del board[0]
                
            elif len(i) % 2 == 1 :
                board.reverse()
                del board[0]
        if len(check) % 2 == 1 :
            board.reverse()
                

        print(board)