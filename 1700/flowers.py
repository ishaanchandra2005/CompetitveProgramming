mod = 1000000007
t, k = map(int, input().split())
dp = [0] * 100001
dp[0] = 1
for i in range(1, 100001):
    dp[i] = dp[i - 1]
    if i - k >= 0:
        dp[i] += dp[i - k]
    dp[i] %= mod
pref = [0] * 100001
for i in range(1, 100001):
    pref[i] = (pref[i - 1] + dp[i]) % mod
for _ in range(t):
    a, b = map(int, input().split())
    print((pref[b] - pref[a - 1]) % mod)