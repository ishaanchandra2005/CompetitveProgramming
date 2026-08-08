from collections import defaultdict
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    pos = defaultdict(list)
    for i in range(n):
        pos[arr[i]].append(i)
    def check(x):
        for color in range(1, k + 1):
            prev = -1
            M = 0 
            m = 0
            if color in pos:
                for idx in pos[color]:
                    gap = idx - prev - 1
                    if gap > M:
                        m = M
                        M = gap
                    elif gap > m:
                        m = gap
                    prev = idx
            gap = n - prev - 1
            if gap > M:
                m = M
                M = gap
            elif gap > m:
                m = gap
            if max(m, M // 2) <= x:
                return True
        return False
    
    l = 0
    r = n
    ans = n
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    print(ans)
    



