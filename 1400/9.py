t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    bad = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        bad[b] = max(bad[b], a)
    left = [0] * (n + 1)
    dp = [0] * (n + 1)
    left[1] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        left[i] = max(left[i - 1], bad[i] + 1)
        dp[i] = i - left[i] + 1
    print(sum(dp))