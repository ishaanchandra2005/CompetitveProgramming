import math
t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    arr = list(map(int, input().split()))
    def sumboy(f):
        m = f - k + 1
        return m * (m + 1) // 2
    y = 0
    ans = 0
    for i in range(n):
        if arr[i] <= q:
            y += 1
        else:
            if y >= k:
                ans += sumboy(y)
            y = 0
    if y >= k:
        ans += sumboy(y)
    print(ans)
                
            
        
        