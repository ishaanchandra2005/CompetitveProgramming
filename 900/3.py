t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    m = k * (k + 1) // 2
    M = k * (2 * n - k + 1) // 2

    if m <= x <= M:
        print("YES")
    else:
        print("NO")
        