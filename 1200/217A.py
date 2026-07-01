n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
parent = list(range(n))
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parent[pb] = pa
for i in range(n):
    for j in range(i + 1, n):
        if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
            union(i, j)
roots = set()
for i in range(n):
    roots.add(find(i))
components = len(roots)
print(components - 1)