griddy = [[0] * 10 for _ in range(10)]
for i in range(10):
    griddy[0][i] = 1
    griddy[9][i] = 1
    griddy[i][0] = 1
    griddy[i][9] = 1
for i in range(1, 9):
    griddy[1][i] = 2
    griddy[8][i] = 2
    griddy[i][1] = 2
    griddy[i][8] = 2
for i in range(2, 8):
    griddy[2][i] = 3
    griddy[7][i] = 3
    griddy[i][2] = 3
    griddy[i][7] = 3
for i in range(3, 7):
    griddy[3][i] = 4
    griddy[6][i] = 4
    griddy[i][3] = 4
    griddy[i][6] = 4
for i in range(4, 6):
    griddy[4][i] = 5
    griddy[5][i] = 5
    griddy[i][4] = 5
    griddy[i][5] = 5

t = int(input())

for _ in range(t):
    grid = [input().strip() for _ in range(10)]
    ans = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'X':
                ans += griddy[i][j]
    print(ans)
            