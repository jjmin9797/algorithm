import copy
firstWard = list(input())
secondWard = list(input())



while secondWard :
    if secondWard[-1] == "A":
        secondWard.pop()
    elif secondWard[-1] == "B":
        secondWard.pop()
        secondWard.reverse()
    elif len(secondWard) == len(firstWard) :
        if secondWard == firstWard :
            print(1)
            break
        else:
            print(0)
            break