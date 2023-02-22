n, k = map(int, input().split())
board = list(map(int, input().split()))

left, right = 0, 0
counter = [0] * (max(board) + 1)
answer = 0
while right < n:
    if counter[board[right]] < k:
        counter[board[right]] += 1
        right += 1
    else:
        counter[board[left]] -= 1
        left += 1
    answer = max(answer, right - left)
print(answer)
