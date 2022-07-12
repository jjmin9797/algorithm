import sys
data = [int(input()) for _ in range(9)]

check = sum(data) - 100
data.sort()
for i in range(0,9) :
    for j in range(i+1,9):

        if data[i] + data[j] == check :
            for k in range(9) :
                if i == k or j == k :
                    continue
                print(data[k])

            sys.exit(0)