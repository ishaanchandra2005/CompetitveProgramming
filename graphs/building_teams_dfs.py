n, m = map(int, input().split())
adj = {}
for i in range(1, n + 1):
    adj[i] = []
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
visited = set()
def dfs(node):
        visited.add(node)
        for nei in adj:
            if nei not in visited:
                dfs(nei)
        


     

