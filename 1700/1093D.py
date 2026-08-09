from collections import deque
import sys
input = sys.stdin.buffer.readline
MOD = 998244353
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    color = [-1] * (n + 1)
    ans = 1

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        q = deque()
        q.append(start)
        color[start] = 0
        x = []

        while q:
            node = q.popleft()
            x.append(node)
            for nei in adj[node]:
                if color[nei] == -1:
                    color[nei] = 1 - color[node]
                    q.append(nei)
                elif color[nei] == color[node]:
                    ans = 0

        if ans == 0:
            break

        a = 0
        b = 0
        for node in x:
            if color[node] == 0:
                a += 1
            else:
                b += 1

        ways = (pow(2, a, MOD) + pow(2, b, MOD)) % MOD
        ans = (ans * ways) % MOD
    print(ans)
    
