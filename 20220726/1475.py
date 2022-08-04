strs = input()

import collections
num = '0123456789'
b = {}
for i in range(0,10):
    b[str(i)] = 0

a = collections.Counter(strs)

for nn in a :
    b[nn] += a[nn]

max = 0
if b['6'] != 0 or b['9'] != 0 :

    b['6'] += b['9']
    b['9'] = 0
    if b['6'] % 2 == 0:
        b['6'] = b['6'] // 2
    else :
        b['6'] = b['6'] // 2 + 1


for n in num :
    if b[n] > max :
        max = b[n]

print(max) 