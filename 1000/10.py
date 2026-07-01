# t = int(input())
# for _ in range(t):
#     n, c = input().split()
#     n = int(n)
#     s = input()
#     if c == 'g':
#         print(0)
#         continue
#     st = s + s
#     ans = 0
#     dp = {}
#     def dfs(i):
#         if st[i] == 'g':
#             return 0
#         if i in dp:
#             return dp[i]
#         dp[i] = 1 + dfs(i + 1)
#         return dp[i]
#     for i in range(n):
#         if s[i] == c:
#             ans = max(ans, dfs(i))
#     print(ans)
t = int(input())
for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()
    if c == 'g':
        print(0)
        continue
    st = s + s
    m = 2 * n
    dist = [0] * m
    lg = -1
    for i in range(m - 1, -1, -1):
        if st[i] == 'g':
            lg = i
        elif lg != -1:
            dist[i] = lg - i
    ans = 0
    for i in range(n):
        if st[i] == c:
            ans = max(ans, dist[i])
    print(ans)
        
            
        