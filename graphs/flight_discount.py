# import sys
# input = sys.stdin.readline
# import heapq
# n, m = map(int, input().split())
# adj = [[] for _ in range(n + 1)]
# for _ in range(m):
#     u, v, wt = map(int, input().split())
#     adj[u].append((v, wt))
# INF = 10**18
# dist1 = [INF] * (n + 1)
# dist2 = [INF] * (n + 1)
# dist1[1] = 0
# pq = []
# heapq.heappush(pq, (0, 1, 0))
# while pq:
#     d, node, state = heapq.heappop(pq)
#     if state == 0:
#         if d > dist1[node]:
#             continue
#     else:
#         if d > dist2[node]:
#             continue
#     for nei, wt in adj[node]:
#         if state == 0:
#             if d + wt < dist1[nei]:
#                 dist1[nei] = d + wt
#                 heapq.heappush(pq, (dist1[nei], nei, 0))
#             if d + wt // 2 < dist2[nei]:
#                 dist2[nei] = d + wt // 2
#                 heapq.heappush(pq, (dist2[nei], nei, 1))    
#         else:
#             if d + wt < dist2[nei]:
#                 dist2[nei] = d + wt
#                 heapq.heappush(pq, (dist2[nei], nei, 1))
# print(dist2[n])
                
                 
import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
rev = [[] for _ in range(n + 1)]
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    rev[v].append((u, w))
    edges.append((u, v, w))
INF = 10**18
dist1 = [INF] * (n + 1)
dist1[1] = 0
pq = [(0, 1)]
while pq:
    d, node = heapq.heappop(pq)
    if d > dist1[node]:
        continue
    for nei, wt in adj[node]:
        nd = d + wt
        if nd < dist1[nei]:
            dist1[nei] = nd
            heapq.heappush(pq, (nd, nei))
dist2 = [INF] * (n + 1)
dist2[n] = 0
pq = [(0, n)]
while pq:
    d, node = heapq.heappop(pq)
    if d > dist2[node]:
        continue
    for nei, wt in rev[node]:
        nd = d + wt
        if nd < dist2[nei]:
            dist2[nei] = nd
            heapq.heappush(pq, (nd, nei))
ans = INF
for u, v, w in edges:
    ans = min(ans, dist1[u] + w // 2 + dist2[v])
print(ans)
        