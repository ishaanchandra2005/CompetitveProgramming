t = int(input())
for _ in range(t):
    n = int(input())
    s = []
    for _ in range(n):
        L, R = map(int, input().split())
        s.append((L, R))
    def check(k):
        l = 0
        r = 0
        for L, R in s:
                l = max(l - k, L)
                r = min(r + k, R)
                if l > r:
                    return False
        return True

    low = 0
    high = 10**9
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            high = mid - 1
        else:
            low = mid + 1
    print(low)
            
