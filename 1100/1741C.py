t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = n
    target = 0
    for i in range(n):
        L = 0
        target += arr[i]
        cs = 0
        cl = 0
        ok = True
        for x in arr:
            cs += x
            cl += 1
            if cs == target:
                L = max(L, cl)
                cs = 0
                cl = 0
            elif cs > target:
                ok = False
                break
        if ok and cs == 0:
            ans = min(ans, L)
    print(ans)