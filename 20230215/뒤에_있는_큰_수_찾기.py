

def solution(numbers):
    answer = [0 for _ in range(len(numbers))]
    stack = [] #index
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    while stack:
        answer[stack.pop()] = -1
    return answer