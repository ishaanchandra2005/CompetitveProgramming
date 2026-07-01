t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    health = []
    for i in range(n):
        rem = arr[i] % k
        if rem == 0:
            rem = k
        health.append((-rem, i + 1))
    health.sort()
    ans = []
    for i in range(n):
        ans.append(health[i][1])
    print(*ans)