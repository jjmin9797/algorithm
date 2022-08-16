a = list(map(int,list(input())))
a.sort(reverse=True)
a = list(map(str,a))
print("".join(a))