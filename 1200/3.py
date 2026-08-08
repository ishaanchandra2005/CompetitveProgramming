from math import gcd
t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    X = n // x
    Y = n // y
    l = x * y // gcd(x, y)
    L = n // l
    X -= L
    Y -= L
    ans = 0 
    # print(X)
    # print(Y)
    ans = X * (2 * n - X + 1) // 2
    ans -= Y * (Y + 1) // 2
    print(ans)

    