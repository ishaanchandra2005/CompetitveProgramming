t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    f = 1
    ans = 1
    for i in range(n - 1):
        if abs(arr[i] - arr[i + 1]) <= k:
            f += 1
            ans = max(f, ans)
        else:
            f = 1
    ans = n - ans
    print(ans)
            