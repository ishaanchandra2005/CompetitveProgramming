n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(arr[0])
dp = [[0] * n for _ in range(n)]
dp[0][0] = arr[0]
dp[0][1] = max(arr[0], arr[1])
dp[1][1] = arr[1]
for i in range(1, n):
    for j in range(i, n):
        dp[i][j] = max(arr[i] + dp[i + 1][j], arr[j] + dp[i][j - 1])
print(dp[0][n - 1])