from collections import deque
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
q = deque()
arr = [-1] * (n + 1)
mom = [-1] * (n + 1)
q.append(1)
arr[1] = 0
while q:
    node = q.popleft()

    for nei in adj[node]:
        if arr[nei] == -1:
            arr[nei] = arr[node] + 1
            mom[nei] = node
            q.append(nei)
path = []

curr = n
while curr != -1:
    path.append(curr)
    curr = mom[curr]
path.reverse()
if arr[n] == -1:
    print("IMPOSSIBLE")
else:
    print(arr[n] + 1)
    print(*path)
    







