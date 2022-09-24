import itertools
import numpy as np
def solution(users, emoticons):

    rp = len(emoticons)
    discount = [0.9,0.8,0.7,0.6]
    data = list(itertools.product(discount, repeat = rp))
    rs = []
    
    for d in data:
        nowPirce = list(map(float,np.multiply(d,emoticons)))
        nowSang = [0,0]
        for userMaxDiscount,userMaxMoney in users :
            
            nowTotalPrice = 0
            nowTotalJoin = 0
            userMaxDiscount = (100-userMaxDiscount)*0.01
            for i in range(len(emoticons)):
                if userMaxDiscount >= d[i]:
                    nowTotalPrice += nowPirce[i]
            if nowTotalPrice >= userMaxMoney :
                nowTotalPrice = 0
                nowTotalJoin  = 1
            nowSang[0] += nowTotalJoin
            nowSang[1] += nowTotalPrice
        
        rs.append(nowSang)

    
        
    
    

    rrr = max(rs)
    rrr[1] = round(rrr[1])
    return rrr

print(solution([[40,10000],[25,10000]],[7000,9000]))