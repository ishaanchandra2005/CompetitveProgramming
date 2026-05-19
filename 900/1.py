t = int(input())
for _ in range(t):
    u, v = map(int, input().split())
    kx, ky = map(int, input().split())
    qx, qy = map(int, input().split())
    dirs = [(u, v), (-u, v), (u, -v), (-u, -v), (v, u), (-v, u), (v, -u), (-v, -u)]
    k = 0
    s = set()
    for a, b in dirs:
        for x, y in dirs:
            if kx + a + x == qx and ky + b + y == qy:
                s.add((kx + a, ky + b))
    k = len(s)
    print(k)
    