from heapq import heappush, heappop
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    h = list(map(int, input().split()))
    def check(f):
        w = 0
        for num in h:
            if num < f:
                w += f - num
        return w <= x
    l = 1
    r = max(h) + x + 1
    ans = 1
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    print(ans)
        
