import collections

a = collections.deque([5,3,1,2])
a = list(a)
a.sort()
a = collections.deque(a)
print(a)
