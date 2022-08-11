rs = []
for i in range(10):
    rs.append(int(input()) % 42)

rs = set(rs)
rs = list(rs)
print(len(rs))