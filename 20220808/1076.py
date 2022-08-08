colors = ['black','brown',
'red','orange','yellow','green',
'blue','violet','grey','white']
value = [i for i in range(10)]
gop = []
a = 1
for i in range(10):
    gop.append(a)
    a *= 10

result = [input(),input(),input()]
idx = []
for i in range(3):
    idx.append(colors.index(result[i]))

o = str(value[idx[0]])+str(value[idx[1]])
print(int(o)*gop[idx[2]])