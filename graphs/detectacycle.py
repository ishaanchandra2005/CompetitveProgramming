n, m = map(int, input().split())
adj = {}
for i in range(1, n + 1):
    adj[i] = []
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
vis = [-1] * (n + 1)
for i in range(1, n + 1):
    if vis[i] == -1:
        q = deque()
        q.append((i, -1))
        vis[i] = 0
        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if vis[nei] == 0 or vis[nei] == 1:
                    print(True)
                if vis[nei] == -1:
                    vis[nei] = 0
                    q.append((nei, node))
            vis[node] = 1
print(False)

