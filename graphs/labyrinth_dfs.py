import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
s = ''
length = float('inf')
arr1 = []
key = 0
mp = {}

def dfs(r, c):
    if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] == '#':
        return
    if grid[r][c] == 'B':
        arr2.append(s)
        mp[len(s)] = key
        key += 1
        arr1.append(len(s))
        s = ''
        return 
    grid[r][c] = '#'
    s += 'U'
    dfs(r - 1, c)
    s += 'L'
    dfs(r, c - 1)
    s += 'D'
    dfs(r + 1, c)
    s += 'R'
    dfs(r, c + 1)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'A':
            dfs(i, j)
if arr1:
    mini = min(arr1)
    ans = ''
    ans += arr2[mp[mini]]
    print("YES")
    print(mini)
    print(ans)

