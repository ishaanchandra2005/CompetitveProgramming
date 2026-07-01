from collections import deque
t = int(input())
dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    bad = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                for dr, dc in dirs:
                    ni = i + dr
                    nj = j + dc
                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj] == 'G':
                            bad = True
                        elif grid[ni][nj] == '.':
                            grid[ni][nj] = '#'
    if bad:
        print("No")
        continue
    vis = [[False] * m for _ in range(n)]
    if grid[n - 1][m - 1] != '#':
        q = deque()
        q.append((n - 1, m - 1))
        vis[n - 1][m - 1] = True
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if not vis[nr][nc] and grid[nr][nc] != '#':
                        vis[nr][nc] = True
                        q.append((nr, nc))

    ok = True
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'G' and not vis[i][j]:
                ok = False
    if ok:
        print("Yes")
    else:
        print("No")
