from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

a = list(map(int, input().split()))

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

dist = [-1] * (n + 1)

q = deque([1])

dist[1] = 0

while q:
    node = q.popleft()

    for nei in adj[node]:
        if dist[nei] == -1:
            dist[nei] = dist[node] + 1
            q.append(nei)

ans = [0] * (k + 1)

for city in range(1, n + 1):
    typ = a[city - 1]
    ans[typ] = max(ans[typ], dist[city])

print(*ans[1:])