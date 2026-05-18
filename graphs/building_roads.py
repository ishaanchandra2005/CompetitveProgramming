import sys
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
adj = {}
for i in range(1, n + 1):
    adj[i] = []
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
visited = set()
road = []
def dfs(node):
        visited.add(node)
        for nei in adj[node]:
            if nei not in visited:
                dfs(nei)
for node in range(1, n + 1):
    if node not in visited:
        road.append(node)
        dfs(node)
print(len(road) - 1)
for i in range(1, len(road)):
    print(road[i - 1], road[i])
