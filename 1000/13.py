t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    segments = [(arr[i] - x, arr[i] + x) for i in range(n)]
    ans = 0
    l, r = segments[0]
    for i in range(1, n):
        l = max(l, segments[i][0])
        r = min(r, segments[i][1])
        if l > r:
            ans += 1
            l, r = segments[i]
    print(ans)


    


    