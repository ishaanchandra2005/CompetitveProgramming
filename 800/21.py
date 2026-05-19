t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    i = 0
    while i < n:
        if arr[i] == 0:
            l = 0
            while i < n and arr[i] == 0:
                l += 1
                i += 1
            ans = max(ans, l)
        else:
            i += 1
    print(ans)