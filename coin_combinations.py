MOD = 10 ** 9 + 7
n, amount = map(int, input().split())
coins = list(map(int, input().split()))
dp = [0] * amount+1
dp[0] = 1
for coin in coins:
    for s in range(coin, amount + 1):
        dp[s] = (dp[s] + dp[s - coin]) % MOD
print(dp[amount])

