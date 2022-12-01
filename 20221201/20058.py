import sys
import copy
input = sys.stdin.readline
n,q = map(int,input().strip().split())
print(2**n)
board = [list(map(int,input().strip().split())) for _ in range(2**n)]
magic = list(map(int,input().strip().split()))

def goMagic(mn,board):
    nBoard = [[-1 * 2**n] for _ in range(2**n)]
    
