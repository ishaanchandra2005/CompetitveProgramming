n, x = map(int, input().split())
coins = list(map(int, input().split()))
dp = {}
def rec(sump):
    if sump == x:
        return 0
    if sump > x:
        return float('inf')
    if sump in dp:
        return dp[sump]
    dp[sump] = float('inf')
    for coin in coins:
        dp[sump] = min(dp[sump], 1 + rec(sump + coin))
    return dp[sump]
k = rec(0)
if k == float('inf'):
    print(-1)
else:
    print(k)  
        