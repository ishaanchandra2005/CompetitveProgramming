t = int(input())
for _ in range(t):
    n = int(input())
    x = 1
    while x * 2 <= n - 1:
        x *= 2
    ans = []
    for i in range(x - 1, -1, -1):
        ans.append(i)
    for i in range(x, n):
        ans.append(i)
    print(*ans)