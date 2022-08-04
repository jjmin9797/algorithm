import collections

a = collections.deque([(0,0,2)])

x,y,v = a.popleft()


print(x,y,v)