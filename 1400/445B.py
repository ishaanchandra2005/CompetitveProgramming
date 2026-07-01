n, m = map(int, input().split())
parent = list(range(n))
size = [1] * n
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])   
    return parent[x]
def union(x, y):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return
    if size[rx] < size[ry]:
        rx, ry = ry, rx
    parent[ry] = rx
    size[rx] += size[ry]
for _ in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)
ans = 1
for i in range(n):
    if find(i) == i:
        ans *= 2 ** (size[i] - 1)
print(ans)

