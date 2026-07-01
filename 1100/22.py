MOD = 1000000007
t = int(input())
for _ in range(t):
    n = int(input())
    ans = 2 * n * (n + 1) * (2 * n + 1) // 6 - n * (n + 1) // 2
    ans = (ans * 2022) % MOD
    print(ans)
