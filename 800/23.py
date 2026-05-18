t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    if d < b:
        print(-1)
        continue
    m = d - b
    a += m
    if a < c:
        print(-1)
        continue
    m += (a - c)
    print(m)
    
