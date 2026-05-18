import sys
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
ans = 0
def dfs(r, c):
    if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] == '#':
        return
    grid[r][c] = '#'
    dfs(r - 1, c)
    dfs(r, c - 1)
    dfs(r + 1, c)
    dfs(r, c + 1)
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            ans += 1
            dfs(i, j)
print(ans)