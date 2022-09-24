from datetime import date, datetime
def solution(today, terms, privacies):
    answer = []
    y,m,d = map(int,today.split("."))
    datetimeToday = datetime(y,m,d)
    termsDic = {}
    for t in terms:
        name,period  = t.split(" ")
        termsDic[name] = int(period)
    
    ctn = 1
    for privacie in privacies:
        contractDate,contractTerms = privacie.split(" ")
        cYear,cMonth,cDay = map(int,contractDate.split("."))
        cMonth += termsDic[contractTerms]
        cDay -= 1
        if cDay == 0 :
            cMonth -= 1
            cDay = 28

        if cMonth > 12 :
            cYear += cMonth//12
            cMonth = cMonth%12
            if cMonth == 0 :
                cMonth = 12
                cYear -= 1
        print(cYear,cMonth,cDay)
        endDate = datetime(cYear,cMonth,cDay)
        if endDate < datetimeToday:
            answer.append(ctn)
        ctn += 1
            


    
    return answer
print(solution("2022.05.19",["A 60","B 12","C 3"],["2000.05.02 A","2021.12.28 B","2022.12.28 C","2022.02.20 C"]))
#print(solution("2022.05.19",["A 6","B 12","C 3"],["2021.05.02 A","2021.07.01 B","2022.02.19 C","2022.02.20 C"]))