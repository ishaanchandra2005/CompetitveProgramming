# import sys
# sys.setrecursionlimit(10**6)
# MOD = 10 ** 9 + 7
# n = int(input())
# dp = {}
# def rec(sump):
#     if sump == n:
#         return 1
#     if sump > n:
#         return 0
#     if sump in dp:
#         return dp[sump]
#     dp[sump] = 0
#     for i in range(1, 7):
#         dp[sump] += rec(sump + i)
#         dp[sump] %= MOD
#     return dp[sump]
# print(rec(0))
MOD = 10**9 + 7
n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
for sump in range(n + 1):
    for dice in range(1, 7):
        if sump + dice <= n:
            dp[sump + dice] += dp[sump]
            dp[sump + dice] %= MOD
print(dp[n])

