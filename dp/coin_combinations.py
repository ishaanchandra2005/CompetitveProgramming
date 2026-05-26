# n, x = map(int, input().split())
# coins = list(map(int, input().split()))
# MOD = 10**9 + 7
# dp = [0] * (x + 1)
# dp[0] = 1
# for s in range(1, x + 1):
#     for coin in coins:
#         if s - coin >= 0:
#             dp[s] = dp[s] + dp[s - coin]
#             dp[s] %= MOD
# print(dp[x])
import sys
input = sys.stdin.readline
n, x = map(int, input().split())
coins = list(map(int, input().split()))
MOD = 10**9 + 7
dp = [0] * (x + 1)
dp[0] = 1
for s in range(1, x + 1):
    total = 0
    for coin in coins:
        if s >= coin:
            total += dp[s - coin]
    dp[s] = total % MOD
print(dp[x])