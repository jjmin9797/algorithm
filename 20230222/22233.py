n, m = map(int, input().split())
keywords = [input() for _ in range(n)]
answer = len(keywords)
articles = [input().split(",") for _ in range(m)]
keywords = set(keywords)

for i in articles:
    for j in i:
        if j in keywords:
            answer -= 1
            keywords.remove(j)
    print(answer)
