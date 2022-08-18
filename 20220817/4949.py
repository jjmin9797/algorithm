while True :
    a = input()
    if a == ".":
        break
    stack = []
    for n in a :
        if a == "[" or a == "(":
            stack.append(a)
        elif (a == "]" or a == ")") and 0 < len(stack):
            if stack[-1] == a :
                del stack[-1]
            else :
                stack = ["nnnnnnn"]
                break
    if len(stack) != 0 :
        print("no")
    else :
        print("yes")