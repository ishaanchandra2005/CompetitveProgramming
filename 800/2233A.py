t = int(input())
for _ in range(t):
    n, x, y, z = map(int, input().split())
    # ai unte
    # ans = n // (x + y)
    ans1 = (n + x + y - 1) // (x + y)
    # ai lekapothe
    ans2 = z
    n -= x * z
    # ans += n // (x + 10 * y)
    ans2 += (n + x + 10 * y - 1) // (x + 10 * y)
    print(min(ans1, ans2))
