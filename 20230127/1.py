import itertools

def check(user,banned):
    if len(user) != len(banned) :
        return False
    for i in range(len(user)):
        if banned[i] == "*":
            continue
        elif banned[i] != user[i]:
            return False
    return True
        

def solution(user_id, banned_id):
    result = []
    allCase = list(itertools.permutations(user_id,len(banned_id)))
    for case in allCase:
        count = 0
        for i in range(len(banned_id)):
            if check(case[i],banned_id[i]):
                count += 1
            else :
                break
        if count == len(banned_id):
            if set(case) not in result :
                result.append(set(case))

    return len(result)
