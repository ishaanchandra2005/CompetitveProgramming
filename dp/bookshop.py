# n, x = map(int, input().split())
# wt = list(map(int, input().split()))
# pages = list(map(int, input().split()))
# dp = [[0] * (x + 1) for _ in range(n)]
# for j in range(x + 1):
#     if j >= wt[0]:
#         dp[0][j] = pages[0]
# for i in range(1, n):
#     for j in range(1, x + 1):
#         not_take = dp[i - 1][j]
#         take = 0
#         if j >= wt[i]:
#             take = pages[i] + dp[i - 1][j - wt[i]]
#         dp[i][j] = max(not_take, take)
# ans = dp[n - 1][x]
# print(ans)

n, x = map(int, input().split())
wt = list(map(int, input().split()))
pages = list(map(int, input().split()))
prev = [0] * (x + 1)
for j in range(x + 1):
    if j >= wt[0]:
        prev[j] = pages[0]
for i in range(1, n):
    curr = [0] * (x + 1)
    for j in range(1, x + 1):
        not_take = prev[j]
        take = 0
        if j >= wt[i]:
            take = pages[i] + prev[j - wt[i]]
        curr[j] = max(not_take, take)
    prev = curr
print(prev[x])