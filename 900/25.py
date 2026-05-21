t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    if x - 1 >= n - x:
        x1 = 1
    else:
        x1 = n
    if y - 1 >= m - y:
        y1 = 1
    else:
        y1 = m
    if x1 == 1:
        x2 = n
    else:
        x2 = 1
    if y1 == 1:
        y2 = m
    else:
        y2 = 1
    print(x1, y1, x2, y2)