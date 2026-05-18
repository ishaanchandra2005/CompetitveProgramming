import sys
sys.setrecursionlimit(10**6)
MOD = 10**9 + 7
n = int(input())
grid = [list(input()) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
if grid[0][0] == '.':
    dp[0][0] = 1 
for i in range(n):
    for j in range(n):
        if grid[i][j] == '*':
            dp[i][j] = 0
            continue
        if i == 0 and j == 0:
            continue
        if i > 0:
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]
        dp[i][j] %= MOD
print(dp[n - 1][n - 1])
        
# def rec(i, j):
#     if i < 0 or j < 0:
#         return 0
#     if grid[i][j] == '*':
#         return 0
#     if i == 0 and j == 0:
#         return 1
#     if dp[i][j] != -1:
#         return dp[i][j]
#     l = rec(i, j - 1)
#     u = rec(i - 1, j)
#     dp[i][j] = (l + u) % MOD
#     return dp[i][j]
# ans = rec(n - 1, n - 1)
# print(ans)


    
    
