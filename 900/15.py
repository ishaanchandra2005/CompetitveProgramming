t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    k = True
    for i in range(n - 1, 0, -1):
        while arr[i - 1] >= arr[i] and arr[i - 1] > 0:
            arr[i - 1] //= 2
            ans += 1
        if arr[i - 1] >= arr[i]:
            k = False
            break
    if k:
        print(ans)
    else:
        print(-1)