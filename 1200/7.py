t = int(input())
for _ in range(t):
    n, m  = map(int, input().split())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    # print(grid)
    gird = []
    for j in range(m):
        rowie = []
        for i in range(n):
            rowie.append(grid[i][j])
        gird.append(rowie)
    # print(gird)
    for row in gird:
        row.sort(reverse = True)
    # print(gird)
    ans = 0
    for i in range(len(gird)):
        for j in range(len(gird[0])):
            ans += gird[i][j] * (len(gird[0]) - j - 1)
    for i in range(len(gird)):
        for j in range(len(gird[0])):
            ans -= gird[i][j] * j
    print(ans)



