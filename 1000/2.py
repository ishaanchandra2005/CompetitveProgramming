t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if k != 4:
        ans = float('inf')
        for x in arr:
            ans = min(ans, (k - x % k) % k)
        print(ans)
    else:
        ans = float('inf')
        even = 0
        for x in arr:
            ans = min(ans, (4 - x % 4) % 4)
            if x % 2 == 0:
                even += 1
        if even >= 2:
            ans = 0
        elif even == 1:
            ans = min(ans, 1)
        else:
            ans = min(ans, 2)
        print(ans)