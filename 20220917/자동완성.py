def makeTrie(words):
    dic = {}
    for word in words:
        nowDic = dic
        for later in word:
            nowDic.setdefault(later, [0, {}])
            nowDic[later][0] +=1  
            nowDic = nowDic[later][1] 
    return dic

def solution(words):
    answer = 0
    trie = makeTrie(words)
    for word in words:
        tmp = trie
        for later in word:
            answer += 1
            tmp = tmp[later]
            if tmp[0] == 1:
                break
            else:
                tmp = tmp[1]
    
    return answer