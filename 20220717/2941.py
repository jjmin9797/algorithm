cro = ["c=","c-","dz=","d-","lj","nj","s=","z="]
q = input()

for c in cro :
    if c in q :
        q = q.replace(c,'C')
print(len(q))


