t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = list(map(int, input().split()))

    prefs = [0] * n
    prefm = [0] * n
    prefs[0] = a[0]
    prefm[0] = a[0]
    for i in range(1, n):
        prefs[i] = prefs[i - 1] + a[i]
        prefm[i] = max(prefm[i - 1], a[i])
    
    ans = []
    for x in k:
        l = 0
        r = n - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if prefm[mid] <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        if res == -1:
            ans.append(0)
        else:
            ans.append(prefs[res])
    print(*ans)

    
    


