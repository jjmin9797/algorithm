al = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for u in al :  
    for i in u:  
        for x in word :  
            if i == x :  
                time += al.index(u) +3 
print(time)