from collections import deque
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
def bfs(i, j):
    q = deque()
    q.append((i, j))
    grid[i][j] = '#'
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == '.':
                    grid[nr][nc] = '#'
                    q.append((nr, nc))
ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            ans += 1
            bfs(i, j)
print(ans)
