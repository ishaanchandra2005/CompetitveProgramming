t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    k = 0
    s = 0
    mini = float('inf')
    for i in range(n):
        for j in range(m):
            s += abs(grid[i][j])
            if grid[i][j] < 0:
                k += 1
            mini = min(mini, abs(grid[i][j]))
    if k % 2 == 0:
        print(s)
    else:
        print(s - 2 * mini)
        

