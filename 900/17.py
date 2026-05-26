from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    m = 1
    curr = 1
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            curr += 1
            m = max(m, curr)
        else:
            curr = 1
    ans = 0
    while m < n:
        req = n - m
        take = min(m, req)
        ans += 1
        ans += take       
        m += take
    print(ans)