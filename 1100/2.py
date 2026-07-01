t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    f = 0
    a = 0
    t = k
    for i in range(n):
        if t == 0:
            break
        a += A[i]
        f = max(f, B[i])
        if t >= 0:
            b = f * (k - (i + 1))
        else:
            b = 0
        ans = max(a + b, ans)
        t -= 1
    print(ans)
