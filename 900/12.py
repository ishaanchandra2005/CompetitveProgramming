t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(0)
        continue
    ans = arr[n - 1] - arr[0]
    for i in range(n - 1):
        ans = max(ans, arr[n - 1] - arr[i])
    for i in range(1, n):
        ans = max(ans, arr[i] - arr[0])
    for i in range(n - 1):
        ans = max(ans, arr[i] - arr[i + 1])
    print(ans)