t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if n % i == 0:
            M = float('-inf')
            m = float('inf')
            for j in range(0, n, i):
                M = max(M, sum(arr[j : j + i]))
                m = min(m, sum(arr[j : j + i]))
            ans = max(ans, M - m)
    print(ans)

