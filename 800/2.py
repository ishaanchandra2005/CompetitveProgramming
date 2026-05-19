t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = arr[0]
    for i in range(n - 1):
        ans = max(ans, arr[i + 1] - arr[i])
    ans = max(ans, 2 * (x - arr[n - 1]))
    print(ans)