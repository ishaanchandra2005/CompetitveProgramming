# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     temp = []
#     for i in range(n):
#         temp.append([arr[i], i + 1])
#     temp.sort()
#     ind = []
#     for val, idx in temp:
#         ind.append(idx)
#     dp = [1] * n
#     for i in range(n):
#         for j in range(i):
#             if ind[i] % ind[j] == 0:
#                 dp[i] = max(dp[i], dp[j] + 1)
#     print(max(dp))
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    dp = [1] * (n + 1)
    for i in range(1, n + 1):
        for j in range(2 * i, n + 1, i):
            if arr[j] > arr[i]:
                dp[j] = max(dp[j], dp[i] + 1)
    print(max(dp))
