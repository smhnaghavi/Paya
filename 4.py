def dfs(i: int, j: int, k: int) -> bool:
    if k == len(word):
        return True
    if i < 0 or i >= m or j < 0 or j >= n or brd[i][j] != word[k]:
        return False
    tmp = brd[i][j]
    brd[i][j] = None
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if dfs(i+dx, j+dy, k+1):
            return True
    brd[i][j] = tmp
    return False


m, n = map(int, input("Enter m and n: ").split())
print(f"Enter the {m}x{n} board row by row:")
board = [input().split() for _ in range(m)]
word = input("Enter a word: ")


cnt_brd = {}
for row in board:
    for ch in row:
        cnt_brd[ch] = cnt_brd.get(ch, 0) + 1

cnt_word = {}
for ch in word:
    cnt_word[ch] = cnt_word.get(ch, 0) + 1

for ch in cnt_word:
    if cnt_brd.get(ch, 0) < cnt_word[ch]:
        print("False")
        exit()

if cnt_brd.get(word[0], 0) > cnt_brd.get(word[-1], 0):
    word = word[::-1]

brd = [row[:] for row in board]

for i in range(m):
    for j in range(n):
        if brd[i][j] == word[0]:
            if dfs(i, j, 0):
                print("True")
                exit()

print("False")
