t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s1 = 0
    s2 = 0
    for i in range(n):
        s1 += max(a[i], b[i])
        s2 = max(s2, min(a[i], b[i]))
    print(s1 + s2)