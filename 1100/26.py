t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    l, r = 0, n - 1
    ans = []
    L = arr[0]
    R = arr[n - 1]
    while l < r:
        if L > R:
            r -= 1
            R += arr[r]
        elif L < R:
            l += 1
            L += arr[l]
        else:
            ans.append(l + 1 + n - r)
            l += 1
            L += arr[l]
    if len(ans) == 0:
        print(0)
    else:
        print(max(ans))


