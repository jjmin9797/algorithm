from collections import deque
from itertools import islice

chars = deque(list(input()))
boom = input()
checkSize = len(boom)
passChars = deque()


def check(strings):
    return True


while chars:
    passChars.appendleft(chars.popleft())
    if "".join(list(islice(passChars, 0, checkSize)))[::-1] == boom:
        for _ in range(checkSize):
            passChars.popleft()
if passChars:
    print("".join(passChars)[::-1])
else:
    print("FRULA")
# ABCC44DDDA
# A BCC44DDDA
# AB CC44DDDA
# ABC C44DDDA
# ABCC 44DDDA
# ABCC4 4DDDA
# ABC 4DDDA
# ABC4 DDDA
# AB DDDA
# ABD DDA
# ABDD DA
# ABDDD A
# ABDDDA
