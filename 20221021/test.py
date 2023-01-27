import time
a = 1
start_time = time.time()
while True :
    a += 1
    if a == 13000000 :
        break

end_time = time.time()
print(end_time-start_time)