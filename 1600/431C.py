MOD = 1000000007
n, k, d = map(int, input().split())
dp = [[0] * 2 for _ in range(n + 1)]
dp[0][0] = 1
for s in range(1, n + 1):
    for num in range(1, k + 1):
        if s >= num:
            if num < d:
                dp[s][0] = (dp[s][0] + dp[s - num][0]) % MOD
                dp[s][1] = (dp[s][1] + dp[s - num][1]) % MOD
            else:
                dp[s][1] = (dp[s][1] + dp[s - num][0] + dp[s - num][1]) % MOD
print(dp[n][1])