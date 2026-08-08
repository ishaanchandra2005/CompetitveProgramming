t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    l = 0
    r = n - 1
    m = 1
    M = n
    ok = True
    while l < r:
        if arr[l] == m:
            l += 1
            m += 1
        elif arr[l] == M:
            l += 1
            M -= 1
        elif arr[r] == m:
            r -= 1
            m += 1
        elif arr[r] == M:
            r -= 1
            M -= 1
        else:
            print(l + 1, r + 1)
            ok = False
            break
    if ok:
        print(-1)

