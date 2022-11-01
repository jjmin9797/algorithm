import sys
import collections
n = int(input())
cards = [int(sys.stdin.readline().strip()) for _ in range(n)]


cardSt = collections.deque()