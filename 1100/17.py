t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    # print(grid)
    f = 0
    for i in range(n // 2):
        for j in range(n):
            if grid[i][j] != grid[n - 1 - i][n - 1 - j]:
                f += 1
    if n % 2 == 1:
        for j in range(n // 2):
            if grid[n // 2][j] != grid[n // 2][n - 1 - j]:
                f += 1
    # print(f)
    if f > k:
        print("NO")
    else:
        if n % 2 == 0:      
            if f % 2 == k % 2:
                print("YES")
            else:
                print("NO")
        else:
            print("YES")


