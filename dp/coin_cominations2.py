# n, x = map(int, input().split())
# coins = list(map(int, input().split()))
# MOD = 10**9 + 7
# dp = [[-1] * (x + 1) for _ in range(n)]
# def rec(i, sump):
#     if sump == x:
#         return 1
#     if sump > x or i >= n:
#         return 0
#     if dp[i][sump] != -1:
#         return dp[i][sump]
#     dp[i][sump] = (rec(i, sump + coins[i]) + rec(i + 1, sump)) % MOD
#     return dp[i][sump]
# ans = rec(0, 0)
# print(ans)

n, x = map(int, input().split())
coins = list(map(int, input().split()))
MOD = 10**9 + 7
dp = [0] * (x + 1)
dp[0] = 1
for coin in coins:
    for s in range(coin, x + 1):
        dp[s] += dp[s - coin]
        dp[s] %= MOD
print(dp[x])

