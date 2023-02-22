p, m = map(int, input().split())
players = [input().split() for _ in range(p)]


rooms = [[players[0]]]


for level, name in players[1:]:
    check = True
    for i in range(len(rooms)):
        if abs(int(rooms[i][0][0]) - int(level)) <= 10 and len(rooms[i]) < m:
            rooms[i].append([level, name])
            check = False
            break
    if check:
        rooms.append([[level, name]])
for r in rooms:
    r.sort(key=lambda x: x[1])
    if len(r) == m:
        print("Started!")
    else:
        print("Waiting!")
    for i in r:
        print(" ".join(i))
